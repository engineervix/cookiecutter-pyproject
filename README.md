<h1 align="center">Welcome to cookiecutter-pyproject 👋</h1>
<p>
  <a href="https://python3statement.org/#sections50-why" target="_blank">
    <img alt="python3" src="https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-brightgreen.svg" />
  </a>
  <a href="https://circleci.com/gh/engineervix/cookiecutter-pyproject/tree/master" target="_blank">
    <img alt="CircleCI" src="https://circleci.com/gh/engineervix/cookiecutter-pyproject/tree/master.svg?style=svg" />
  </a>
  <a href="https://coveralls.io/github/engineervix/cookiecutter-pyproject?branch=master" target="_blank">
    <img alt="Coverage Status" src="https://coveralls.io/repos/github/engineervix/cookiecutter-pyproject/badge.svg?branch=master" />
  </a>
  <a href="https://github.com/engineervix/cookiecutter-pyproject/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/engineervix/cookiecutter-pyproject/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/engineervix/cookiecutter-pyproject" />
  </a>
  <a href="https://requires.io/github/engineervix/cookiecutter-pyproject/requirements/?branch=master" target="_blank">
    <img alt="Requirements Status" src="https://requires.io/github/engineervix/cookiecutter-pyproject/requirements.svg?branch=master" />
  </a>
  <a href="https://dependabot.com/" target="_blank">
    <img alt="dependabot" src="https://badgen.net/dependabot/engineervix/cookiecutter-pyproject/?icon=dependabot" />
  </a>
  <a href="https://github.com/PyCQA/bandit" target="_blank">
    <img alt="security: bandit" src="https://img.shields.io/badge/security-bandit-yellow.svg" />
  </a>
  <a href="http://commitizen.github.io/cz-cli/" target="_blank">
    <img alt="Commitizen friendly" src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg" />
  </a>
  <a href="https://twitter.com/engineervix" target="_blank">
    <img alt="Twitter: engineervix" src="https://img.shields.io/twitter/follow/engineervix.svg?style=social" />
  </a>
</p>

> A simple Cookiecutter template to quickly bootstrap a new python project

## Features

- Always up-to-date dependencies with the help of [dependabot](https://dependabot.com/)
- Python 3.6+
- Testing using [`pytest`](https://docs.pytest.org/en/stable/)
- Uses [pip-tools](https://github.com/jazzband/pip-tools) for dependency management
- Continuous Integration options: [Gitlab CI](https://docs.gitlab.com/ee/ci/) or [Circle CI](https://circleci.com/)
- Pre-commit hooks via [pre-commit](https://pre-commit.com/).
- [Conventional commits](https://www.conventionalcommits.org/) courtesy of the [Commitizen tool](https://github.com/commitizen-tools/commitizen), which is also useful for:
  - Bumping versions automatically using [semantic versioning](https://semver.org/) based on the commits
  - Generating a changelog using [Keep a changelog](https://keepachangelog.com/)
- Code formatting using [black](https://github.com/psf/black)
- Linting using [flake8](https://flake8.pycqa.org/en/latest/)
- Choice of various licenses
- Optional CLI using [Click](https://click.palletsprojects.com/) or [argparse](https://docs.python.org/3/library/argparse.html)
- Generates a simple [VSCode](https://code.visualstudio.com/) `settings.json` (Just change the `python.pythonPath`)

## Getting started

Ensure that you have [cookiecutter](https://github.com/audreyr/cookiecutter) installed on your computer:

```sh
pip install -U cookiecutter
```

Bootstrap your new python project:

```sh
cookiecutter https://github.com/engineervix/cookiecutter-pyproject.git
```

You'll be prompted for some values, such as **project_name**, **project_slug**, **email**, **license**, etc.

Once you're done, `cd` into your the new project folder created above, and you're ready to roll :sunglasses:!

### Other steps

- Create a virtual environment for your project
- Install project dependencies: `pip install -r requirements.txt`
- `pre-commit install`
- `pre-commit install --hook-type commit-msg`
- add any additional requirements in the `requirements.in` file, then
  - `pip-compile requirements.in` to generate an updated `requirements.txt` file
  - `pip-sync` to update your virtual environment to reflect exactly what's in the `requirements.txt` file.

It goes without saying that you'll want to create a repo for your new project. If you're using *Circle CI*, ensure that you add your repo to your [CircleCI](https://circleci.com/) account. Optionally register your repo with [dependabot](https://app.dependabot.com/), [requires.io](https://requires.io), [coveralls](https://coveralls.io), [codeclimate](https://codeclimate.com/) and [deepsource](https://deepsource.io/) (Don't forget to add the Code Climate, Coveralls and Deepsource Environment Variables to your Project's Settings in your CircleCI Dashboard). If you don't want to use any of these services

- remove them (coveralls, codeclimate and deepsource) from the CircleCI configuration file
- remove the respective badges in your project's `README.md` file

### Tests

Simply run `pytest`. For more detailed output, including test coverage:

```sh
pytest -vv --cov=. --cov-report term-missing
```

## Author

👤 **Victor Miti**

* Twitter: [@engineervix](https://twitter.com/engineervix)
* Github: [@engineervix](https://github.com/engineervix)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/engineervix/cookiecutter-pyproject/issues).

## Show your support

Give a ⭐️if this project helped you!

## 📝 License

Copyright © 2020 [Victor Miti](https://github.com/engineervix).<br />
This project is [MIT](https://github.com/engineervix/cookiecutter-pyproject/LICENSE) licensed.

## Credits

Inspired by:

- [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
- [wemake-services/wemake-python-package](https://github.com/wemake-services/wemake-python-package)
- [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter)
- [ionelmc/cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary)

## TODO

- [ ] Add other CI options: [Github Actions](https://github.com/features/actions), [AppVeyor](https://www.appveyor.com/) and perhaps [Travis CI](https://travis-ci.org/)
- [ ] Add [packaging](https://packaging.python.org/guides/distributing-packages-using-setuptools/) options
- [ ] Include options for [coveralls](https://coveralls.io), [codeclimate](https://codeclimate.com/) and [deepsource](https://deepsource.io/) in Gitlab CI.
- [ ] Working with [dependabot](https://dependabot.com/) on Gitlab

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
