# Forecasting Python

This repository holds all Python software development related to the Forecasting project.

It contains several python packages, which can be built and distributed independently from each other.

## Prerequisites

This repository leverages [`poetry`](https://python-poetry.org/docs/basic-usage/), a python dependency management tool in order to install and build all packages.

Make sure you have [`poetry`](https://python-poetry.org/docs/) installed before going further.

> Note: You can install `poetry` following the [official documentation](https://python-poetry.org/docs/#installation).

To make sure that you're ready, open a terminal, and type the command:

```bash
poetry --version
```

> Warning: Never install `poetry` using `pip` as it will break your environment !

Once you've got `poetry` installed, make sure it is configured to **NOT** create virtual environments:

```bash
poetry config virtualenvs.create false
```

### Installing the development tools:

#### Creating a virtual environment.

You can now create a dedicated environment for development:

```
python -m venv .venv
```

You then need to enable this environment:

- On Windows:

```powershell
./venv/Scripts/activate
```

- On Linux:

```bash
. .venv/bin/activate
```

Install the monorepo tools using `poetry`:

```bash
poetry install
```

Finally install `pre-commit` hooks and the `nbstripout` git filter:

```bash
# Install pre-commit git hooks
pre-commit install
# Install commit-msg git hooks
pre-commit install -t commit-msg
# Install git filters for jupyter notebooks
nbstripout --install --attributes .gitattributes
```

#### Install libraries and applications

To install a specific library/application, got to the corresponding folder and install it via `poetry`:

```bash
cd librairies/my-lib
poetry install
```

## Developing libraries

### Create a new library

You can use the `poetry new` command to create a new library:

```bash
cd librairies
poetry new forecasting-something
```

It will create a directory named `forecasting-something` into the [`./libraries/`](./libraries) directory

### Adding dependencies to a library

You need to use `poetry` directly in order to add a dependency. First navigate to the project you want to add dependencies for:

```bash
cd libraries/forecasting-something
```

And add a dependency using poetry. For example let's add `mlflow`:

```bash
poetry add mlflow
```

#### Adding development dependencies

Not all dependencies should be installed at runtime. When you want to use a dependency during develomment only, consider using the `--dev` option:

```bash
poetry add --dev ipykernel
```

## Building libraries and applications

It is possible to build the packages into `wheel` archives using the `poetry build` command:


```bash
cd libraries/forecasting-something
poetry build
```

## Ensuring code quality

#### Use `k format` to format code

You can use `black` and `isort` commands to format the code. Simply run:

```bash
black librairies/forecasting-something
isort librairies/forecasting-something
```

> Note: If you're working with Visual Studio, `black` should be executed on saving files.

#### Using `pylint` to lint code

You can use the `pylint` command to lint the code. To lint all projects (slow), simply run:

```bash
pylint librairies
```

Or lint a single project:

```bash
pylint libraries/forecasting-something
```

#### Using `pytest` to run tests

> Note: For the moment, no unit test is available.

You can run tests for a single project:

```bash
pytest librairies/forecasting-something
```

## Commiting changes

### Preparing the commit

Use `git` to stage changes you want to include in your commit:

```bash
git add <concerned_files>
```

Once you added everything, you can use `pre-commit` to make sure your commit passes commit hooks verifications:

```bash
pre-commit
```

If any modification is performed by the commit hooks, don't forget to run `git add <modified_files>` to stage them again.

Once you're ready to commit your changes:

```bash
git commit
```