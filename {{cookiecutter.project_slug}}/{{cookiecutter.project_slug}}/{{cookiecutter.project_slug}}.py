#!/usr/bin/env python3

"""
{{cookiecutter.project_slug}}.py

{{cookiecutter.project_short_description}}
"""

# import os

__author__ = '{{ cookiecutter.full_name|e }}'
__copyright__ = 'Copyright {% now 'local', '%Y' %}, {{ cookiecutter.full_name|e }}'
{% if cookiecutter.open_source_license == 'MIT license' -%}
__license__ = 'MIT'
{% elif cookiecutter.open_source_license == 'BSD license' %}
__license__ = 'BSD-3-Clause'
{% elif cookiecutter.open_source_license == 'ISC license' %}
__license__ = 'ISC'
{% elif cookiecutter.open_source_license == 'Apache Software License 2.0' %}
__license__ = 'Apache-2.0'
{% elif cookiecutter.open_source_license == 'GNU General Public License v3' -%}
__license__ = 'GPL-3.0-or-later'
{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}
__license__ = 'LGPL-3.0-or-later'
{% endif %}
__version__ = '{{ cookiecutter.version }}'
__maintainer__ = '{{ cookiecutter.full_name|e }}'
__email__ = '{{ cookiecutter.email }}'
__status__ = 'Development'


def add(first_term, second_term):
    """Example trivial function which returns the sum of two numbers.

    Args:
        first_term (int):  The first parameter.
        second_term (str): The second parameter.

    Returns:
        int: The sum of the two parameters.
    """
    sum = first_term + second_term
    return sum


def subtract(first_term, second_term):
    """Example trivial function which returns the difference of two numbers.

    Args:
        first_term (int):  The first parameter.
        second_term (str): The second parameter.

    Returns:
        int: The difference between the two parameters.
    """
    difference = first_term - second_term
    return difference
