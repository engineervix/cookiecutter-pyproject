"""Console script for {{cookiecutter.project_slug}}."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="{{ cookiecutter.project_slug }}",
        description="{{ cookiecutter.project_short_description }}",
    )
    parser.add_argument('_', nargs='*')
    args = parser.parse_args(args)

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_slug}}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
