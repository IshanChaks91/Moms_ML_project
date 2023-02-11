# pythontemplate
Python repository template

# python repository template

To use the template for a new repo simply copy all the files to a new directory. Feel free to not use of discard whatever component you do not care for in your repository.

As of this writing there are two places with the template name, that need to be changed:

- project name in `pyproject.toml`
- doc site name in `mdocs.yml`

## [poetry](https://python-poetry.org/)

This project is managed with poetry. See official documentation on how to install it.

### install / development

To install the project

```term
poetry install
```

If a python environment was activated, the project will be installed into it allowing cross-repo devlopment.

### update dependency

To update changes to dependencies in `pyproject.toml` you can specifically update the lock file and limit `poetry`'s to necessary changes to speed up the process.

```term
poetry lock
poetry lock --no-update  # only updates what is necessary

poetry install
```

## tools

The list of tools implemented and recommended by this repository.

### [pylint](https://pylint.pycqa.org/en/latest/)

A python code linter identifying potential problems or deviations from common python code guidelines or standards.

### [black](https://black.readthedocs.io/en/stable/)

An opinionated python code formatter, that, among other things, tries to minimize git commit diffs.

### [mypy](https://mypy.readthedocs.io/en/stable/)

A python static type checker making use of type hints.

### isort

A python import sort order reformatter and checker. Basically sorts imports in a file into three distrinct blocks

- standard library
- third party libraries
- imports local to this repo

### [mkdocs](https://www.mkdocs.org/)

Markdown based package documentation tool.

#### [mkdocstings](https://mkdocstrings.github.io/)

Enables use of docstrings for automatic documentation generation in mkdocs.

### [nox](https://nox.thea.codes/en/stable/)

Defines common tasks like linting and testing and, per default, executes them in their own virtual environments.

Having sessions run in isolated environments is convenient to verify behaviour outside your potentially dirty local environment.

All tools present have a nox session defined.

#### common nox commands

Run all default sessions by

```termin
nox
```

List sessions along with a short description of what they do with

```term
nox -l
```

Run specific sessions with the session parameter

```term
nox -s [session name]
```

Reuse existing virtual-environments to execute sessions faster locally. Careful that this may use an environment that does not match the current set dependencies.

```term
nox -r
```

### [pip-licenses](https://github.com/raimon49/pip-licenses)

A python package which collects and prints the licenses used in the present environment.

### html output

Running `nox` generates a number of interesting html pages, which can be easily served
remotely.

```term
nox
nox -s serve
# or
python -m http.server -d html
```

These pages will also be available via gitlab pages, when the CI/CD runs.

## gitlab

### Continous Integration/Deployment

The `.gitlab-ci.yml` contains the specification for gitlab runners to execute when commits are pushed. They basically run most nox sessions to avoid duplications.

### gitlab pages

The CI/CD jobs where applicable generate html pages that will be accesible via [gitlab pages](https://iais-nm-cv.pages.fraunhofer.de/python-template/). The URL depends on the repository.
