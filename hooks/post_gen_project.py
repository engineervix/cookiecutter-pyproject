#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_directory(dir_path):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dir_path))


if __name__ == "__main__":

    # rename this directory so that it isn't included in version control
    vscode = os.path.join(PROJECT_DIRECTORY, "#vscode/")

    # the renamed version is in the .gitignore file
    shutil.move(vscode, os.path.join(PROJECT_DIRECTORY, ".vscode/"))

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    if "Gitlab CI" == "{{ cookiecutter.continuous_integration }}":
        remove_directory(".circleci")
        remove_file(".deepsource.toml")
        remove_file(".coveragerc")

    if "CircleCI" == "{{ cookiecutter.continuous_integration }}":
        remove_file(".gitlab-ci.yml")
