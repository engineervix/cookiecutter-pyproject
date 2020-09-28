from contextlib import contextmanager
import shlex
import os
import sys

# More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b404-import-subproces
import subprocess  # nosec
import yaml
import datetime
from cookiecutter.utils import rmtree

from click.testing import CliRunner

import importlib


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))  # nosec ([B404:blacklist])


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))  # nosec ([B404:blacklist])


def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join("LICENSE")
        now = datetime.datetime.now()
        # More Info: https://bandit.readthedocs.io/en/latest/plugins/b101_assert_used.html
        assert str(now.year) in license_file_path.read()  # nosec ([B101:assert_used])


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()  # nosec
        assert result.exit_code == 0  # nosec
        assert result.exception is None  # nosec

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "python_project" in found_toplevel_files  # nosec
        assert "tests" in found_toplevel_files  # nosec


def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()  # nosec
        run_inside_dir("pytest", str(result.project)) == 0
        print("test_bake_and_run_tests path", str(result.project))


def test_bake_withspecialchars_and_run_tests(cookies):
    """Ensure that a `full_name` with double quotes does not break the project"""
    with bake_in_temp_dir(
        cookies, extra_context={"full_name": 'name "quote" name'}
    ) as result:
        assert result.project.isdir()  # nosec
        run_inside_dir("pytest", str(result.project)) == 0


def test_bake_with_apostrophe_and_run_tests(cookies):
    """Ensure that a `full_name` with apostrophes does not break the project"""
    with bake_in_temp_dir(cookies, extra_context={"full_name": "O'connor"}) as result:
        assert result.project.isdir()  # nosec
        run_inside_dir("pytest", str(result.project)) == 0


def test_bake_selecting_license(cookies):
    license_strings = {
        "MIT license": "MIT ",
        "BSD license": "Redistributions of source code must retain the "
        + "above copyright notice, this",
        "ISC license": "ISC License",
        "Apache Software License 2.0": "Licensed under the Apache License, Version 2.0",
        "GNU General Public License v3": "GNU GENERAL PUBLIC LICENSE",
        "GNU Lesser General Public License v3": "GNU LESSER GENERAL PUBLIC LICENSE",
    }
    for license, target_string in license_strings.items():
        with bake_in_temp_dir(
            cookies, extra_context={"open_source_license": license}
        ) as result:
            assert target_string in result.project.join("LICENSE").read()  # nosec


def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": "Not open source"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "LICENSE" not in found_toplevel_files  # nosec


def test_running_pytest(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()  # nosec
        test_file_path = result.project.join("tests/test_python_project.py")
        lines = test_file_path.readlines()
        assert "import pytest" in "".join(lines)  # nosec
        # Test the new pytest target
        run_inside_dir("pytest", str(result.project)) == 0


def test_running_pytest_with_argparse(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"command_line_interface": "argparse"}
    ) as result:
        assert result.project.isdir()  # nosec
        test_file_path = result.project.join("tests/test_python_project.py")
        lines = test_file_path.readlines()
        assert "import pytest" in "".join(lines)  # nosec
        # Test the new pytest target
        run_inside_dir("pytest", str(result.project)) == 0


# def test_project_with_hyphen_in_module_name(cookies):
#     result = cookies.bake(
#         extra_context={'project_name': 'something-with-a-dash'}
#     )
#     assert result.project is not None


def test_bake_with_no_console_script(cookies):
    context = {"command_line_interface": "No command-line interface"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" not in found_project_files  # nosec


def test_bake_with_console_script_files(cookies):
    context = {"command_line_interface": "click"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" in found_project_files  # nosec


def test_bake_with_argparse_console_script_files(cookies):
    context = {"command_line_interface": "argparse"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" in found_project_files  # nosec


def test_bake_with_console_script_cli(cookies):
    context = {"command_line_interface": "click"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    module_path = os.path.join(project_dir, "cli.py")
    module_name = ".".join([project_slug, "cli"])
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = CliRunner()
    noarg_result = runner.invoke(cli.main)
    assert noarg_result.exit_code == 0  # nosec
    noarg_output = " ".join(
        ["Replace this message by putting your code into", project_slug]
    )
    assert noarg_output in noarg_result.output  # nosec
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0  # nosec
    assert "Show this message" in help_result.output  # nosec


def test_bake_with_argparse_console_script_cli(cookies):
    context = {"command_line_interface": "argparse"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    module_path = os.path.join(project_dir, "cli.py")
    module_name = ".".join([project_slug, "cli"])
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = CliRunner()
    noarg_result = runner.invoke(cli.main)
    assert noarg_result.exit_code == 0  # nosec
    noarg_output = " ".join(
        ["Replace this message by putting your code into", project_slug]
    )
    assert noarg_output in noarg_result.output  # nosec
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0  # nosec
    assert "Show this message" in help_result.output  # nosec


def test_bake_circleci(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"continuous_integration": "CircleCI"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert ".gitlab-ci.yml" not in found_toplevel_files  # nosec


def test_bake_gitlab_ci(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"continuous_integration": "Gitlab CI"}
    ) as result:
        project_path, project_slug, project_dir = project_info(result)
        found_project_files = os.listdir(project_path)
        assert ".circleci" not in found_project_files  # nosec
