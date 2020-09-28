#!/usr/bin/env python3

"""Tests for `{{ cookiecutter.project_slug }}`"""

import pytest
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
{%- endif %}

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from {{ cookiecutter.project_slug }} import cli
{%- endif %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/engineervix/cookiecutter-pyproject')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
{%- if cookiecutter.command_line_interface|lower == 'click' %}


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def test_command_line_interface(capsys):
    """Test the CLI."""
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        cli()
    captured = capsys.readouterr()
    result = captured.out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 42
    assert '{{ cookiecutter.project_slug }}.cli.main' in result

    with pytest.raises(SystemExit) as pytest_wrapped_f:
        cli(["-h"])
    captured_02 = capsys.readouterr()
    help_result = captured_02.out
    assert pytest_wrapped_f.type == SystemExit
    assert pytest_wrapped_f.value.code == 42
    assert '-h, --help            show this help message and exit' in help_result
{%- endif %}


class Test{{ cookiecutter.project_slug|title }}():
    """Tests the {{ cookiecutter.project_slug }} module"""

    @staticmethod
    def test_addition():
        """tests for addition"""
        assert {{ cookiecutter.project_slug }}.add(2, 2) == 4  # nosec

    @staticmethod
    def test_subtraction():
        """tests for subtraction"""
        assert {{ cookiecutter.project_slug }}.subtract(4, 2) == 2  # nosec
