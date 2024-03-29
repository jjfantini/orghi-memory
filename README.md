<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">orghi-memory</h3>

<div align="center">

  [![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/jjfantini/orghi-memory)
  [![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=450509735)
  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/jjfantini/orghi-memory.svg)](https://github.com/jjfantini/orghi-memory/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/jjfantini/orghi-memory.svg)](https://github.com/jjfantini/orghi-memory/pulls)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
  [![Python](https://img.shields.io/badge/Python-3.12.1-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
  ![License](https://img.shields.io/badge/License-Proprietary-black)
  [![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brighgreen.svg)](http://commitizen.github.io/cz-cli/)
</div>

---
testing memory properties of MemGPT for personal AI. mistral backend via perplexityAI

## 📝 __Table of Contents__

- [Usage](#Usage)
- [Features](#features)
- [Roadmap](../roadmap.md)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🏁 __Getting Started__ <a name = "getting_started"></a>

_Python package_: to add and install this package as a dependency of your project, run `poetry add orghi-memory`.

_Python CLI_: to view this app's CLI commands once it's installed, run `orghi-memory --help`.

_Python application_: to serve this REST API, run `docker compose up app` and open [localhost:8000](http://localhost:8000) in your browser. Within the Dev Container, this is equivalent to running `poe api`.

<details>
<summary>Prerequisites</summary>

<details>
<summary>1. Set up Git to use SSH</summary>

1. [Generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) and [add the SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
1. Configure SSH to automatically load your SSH keys:

    ```sh
    cat << EOF >> ~/.ssh/config
    Host *
      AddKeysToAgent yes
      IgnoreUnknown UseKeychain
      UseKeychain yes
    EOF
    ```

</details>

<details>
<summary>2. Install Docker</summary>

1. [Install Docker Desktop](https://www.docker.com/get-started).
    - Enable _Use Docker Compose V2_ in Docker Desktop's preferences window.
    - _Linux only_:
        - Export your user's user id and group id so that [files created in the Dev Container are owned by your user](https://github.com/moby/moby/issues/3206):

            ```sh
            cat << EOF >> ~/.bashrc
            export UID=$(id --user)
            export GID=$(id --group)
            EOF
            ```

</details>

<details>
<summary>3. Install VS Code or PyCharm</summary>

1. [Install VS Code](https://code.visualstudio.com/) and [VS Code's Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Alternatively, install [PyCharm](https://www.jetbrains.com/pycharm/download/).
2. _Optional:_ install a [Nerd Font](https://www.nerdfonts.com/font-downloads) such as [FiraCode Nerd Font](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode) and [configure VS Code](https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions) or [configure PyCharm](https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions) to use it.

</details>

</details>

<details open>
<summary>Development environments</summary>

The following development environments are supported:


1. ⭐️ _GitHub Codespaces_: click on _Code_ and select _Create codespace_ to start a Dev Container with [GitHub Codespaces](https://github.com/features/codespaces).
1. ⭐️ _Dev Container (with container volume)_: click on [Open in Dev Containers](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/jjfantini/orghi-memory) to clone this repository in a container volume and create a Dev Container with Cursor AI/VS Code.
1. _Dev Container_: clone this repository, open it with Cursor AI/VS Code, and run <kbd>Ctrl/⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> → _Dev Containers: Reopen in Container_.
1. _PyCharm_: clone this repository, open it with PyCharm, and [configure Docker Compose as a remote interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote) with the `dev` service.
1. _Terminal_: clone this repository, open it with your terminal, and run `docker compose up --detach dev` to start a Dev Container in the background, and then run `docker compose exec dev zsh` to open a shell prompt in the Dev Container.

</details>

## __Features__ <a name = "features"></a>

- 🧑‍💻 Quick and reproducible development environments with VS Code's [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers), PyCharm's [Docker Compose interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote), and [GitHub Codespaces](https://github.com/features/codespaces)
- 🌈 Cross-platform support for Linux, macOS (Apple silicon and Intel), and Windows
- 🐚 Modern shell prompt with [Starship](https://github.com/starship/starship)
- 📦 Packaging and dependency management with [Poetry](https://github.com/python-poetry/poetry)
- 🌍 Environment management with [Micromamba](https://github.com/mamba-org/mamba)
- 📖 Comprehensive documentation generation with [Sphinx](https://www.sphinx-doc.org/en/master/) or [pdoc](https://pdoc.dev/)
- 🚚 Installing from and publishing to private package repositories and [PyPI](https://pypi.org/)
- ⚡️ Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
- ✍️ Code formatting with [Ruff](https://github.com/charliermarsh/ruff)
- ✅ Code linting with [Pre-commit](https://pre-commit.com/), [Mypy](https://github.com/python/mypy), and [Ruff](https://github.com/charliermarsh/ruff)
- 🏷 Optionally follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
- 💌 Verified commits with [GPG](https://gnupg.org/)
- ♻️ Continuous integration with [GitHub Actions](https://docs.github.com/en/actions) or [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- 🧪 Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy)
- 🏗 Scaffolding updates with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and [Cruft](https://github.com/cruft/cruft)
- 🧰 Dependency updates with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)

## 🚗 __Roadmap__ <a name = "roadmap"></a>

- [ ] Add support for [Nox](https://nox.thea.codes/en/stable/) for automated testing across various platforms and python versions.

## 🏗️ __Development Setup__ <a name = "development_setup"></a>



- This project follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen).
- Run `poe` from within the development environment to print a list of [Poe the Poet](https://github.com/nat-n/poethepoet) tasks available to run on this project.
- Run `poetry add {package}` from within the development environment to install a run time dependency and add it to `pyproject.toml` and `poetry.lock`. Add `--group test` or `--group dev` to install a CI or development dependency, respectively.
- Run `poetry update` from within the development environment to upgrade all dependencies to the latest versions allowed by `pyproject.toml`.
- Run `cz bump` to bump the package's version, update the `CHANGELOG.md`, and create a git tag, settings can be made in both `cz-config.js` and `bumpversion.yml`.

### 🎣 Hooks

This project uses two hooks, `pre_gen_project.py` and `post_gen_project.py`, which are scripts that run before and after the project generation process, respectively.

This section shows users how to setup your environment using your `micromamba` file and `poetry`.
<details>
<summary><b>Setup Mamba Environment (w/Poetry)</b></summary>
<p>

This project uses a micromamba environment. The micromamba environment will be automatically setup for you after generating the project from the template using a `post_gen_project` hook. The following steps are for reference only (if you need to recreate the environment). This assumes you use `bash` as your shell.

#### Prerequisites
<details>
<summary><b>1. Installing <a href="https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html#operating-system-package-managers">`micromamba`</a></b></summary>
<p>

```bash
# Windows (Powershell)
Invoke-Expression ((Invoke-WebRequest -Uri https://micro.mamba.pm/install.ps1).Content)
```

```bash
# Linux and macOS
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```


</p>
</details>

#### Creating Micromamba Environment

1. I created the environment with a `--prefix` and not a name, to ensure that it installed in my project directory, not the default path. This is executed in the project root dir.

    ```bash
    micromamba env create --file micromamba_env.yml
    ```

2. To avoid displaying the full path when using this environment, modify the `.condarc` file to show the environment name as the last directory where the environment is located. This can be done manually or by running the command `micromamba config --set env_prompt '({name})'`. 

    ```bash
    micromamba config --set env_prompt '({name})'
    ```

    After the modification, your `.condarc` file should look like this:

    ```yaml
    channels:
      - conda-forge
      - defaults
    env_prompt: ({name})
    repodata_threads: 2
    change_ps1: false
    envs_dirs:
      - ~/micromamba/envs
    ```

3. Activate the environment

    ```bash
    micromamba init bash / micromamba init zsh
    micromamba activate ./menv
    ```

4. Check if poetry is installed

    ```bash
    poetry --version
    # make sure it is the latest version
    # can use mamba search -f poetry
    ```
5. If poetry is showing any errors like:

    - `Failed to create process`
    - `No Python at <path>`

    You can simply run:
    ```bash
    micromamba remove -p ./menv poetry 
    micromamba install -p ./menv poetry 
    ```
6. If the python version doesnt match, just install the version you would like:

    ```bash
    micromamba install -p ./menv python=3.12.1
    ```

6. Install Packages from `poetry.lock` / `pyproject.toml`

    ```bash
    poetry install
    ```
</p>
</details>

<details>
<summary><b>Setting Up `Commitizen`</b></summary>
<p>
I am using the `vscode-commmitizen` extension to integrate `commitizen` into my workflow.
This allows for nice keyboard shortcuts and UI integration. I have also installed `cz_customizable` globally to allow me to customize the commit message template using `cz-config.js`.

The `pyproject.toml` file has the specifications for `cz_customizable` and `commitizen` to work together.

Follow the [quickstart guide](https://github.com/leoforfree/cz-customizable) and use the 'Quick Start' section to setup `cz-customizable`. You need to install
`cz-customizable` globally in order for the vscode extension to work along with the settings provided in the `pyproject.toml` file.

- [x] make sure you have a `pre-commit-config.yml`
- [x] make sure you have a `bumpversion.yml` in `.github/workflows`

</p>
</details>

## ⚡️ __GitHub Workflow Setup__ <a name = "development_setup"></a>

There are 5 pre-made github actions that are used with this template. SOme require API_KEYS/TOKENS to work. Add your tokens to the secrets manager in your repo settings.

1. `bump.yml`: This workflow automates the versioning of the project using bumpversion.
   - Uses a GitHub `GH_PAT`
2. `deploy.yml`:
   - This workflow is responsible for deploying the project. It is triggered on push events that include tags in the format "v*._._" and also manually through the GitHub Actions UI.
   - The workflow runs on an Ubuntu-latest environment and only if the GitHub reference starts with 'refs/tags/v'.
   - The steps involved in this workflow include:
       - Checking out the repository.
       - Logging into the Docker registry.
       - Setting the Docker image tag.
       - Building and pushing the Docker image.
   - The tokens/secrets used in this workflow include:
       - `GITHUB_TOKEN`: This is a GitHub secret used for authentication.
       - `DOCKER_REGISTRY`: This is an environment variable set to 'ghcr.io'.
       - `DEFAULT_DEPLOYMENT_ENVIRONMENT`: This is an environment variable set to 'feature'.
       - `POETRY_HTTP_BASIC__USERNAME`: This is a secret used for authentication with the private package repository.
       - `POETRY_HTTP_BASIC__PASSWORD`: This is a secret used for authentication with the private package repository.
3. `publish.yml`: This workflow is responsible for publishing the project. It is triggered when a new release is created. The workflow runs on an Ubuntu-latest environment.
   - The steps involved in this workflow include:
       - Checking out the repository.
       - Setting up Python with the specified version.
       - Installing Poetry, a tool for dependency management and packaging in Python.
       - Publishing the package using Poetry. If a private package repository is specified, the package is published there. Otherwise, it is published to PyPi.
   - The tokens/secrets used in this workflow include:
       - `GITHUB_TOKEN`: This is a GitHub secret used for authentication.
       - `POETRY_HTTP_BASIC__USERNAME`: This is a secret used for authentication with the private package repository.
       - `POETRY_HTTP_BASIC__PASSWORD`: This is a secret used for authentication with the private package repository.
       - `POETRY_PYPI_TOKEN_PYPI`: This is a secret used for authentication with PyPi, if the package is being published there.
9. `test.yml`:
   - This workflow is responsible for testing the project. It is triggered on push events to the main and master branches, and on pull requests.
   - The workflow runs on an Ubuntu-latest environment and uses the specified Python version.
   - The steps involved in this workflow include:
       - Checking out the repository.
       - Setting up Node.js with the specified version.
       - Installing @devcontainers/cli.
       - Starting the Dev Container.
       - Linting the package.
       - Testing the package.
       - Uploading coverage.
   - The tokens/secrets used in this workflow include:
       - `GITHUB_TOKEN`: This is a GitHub secret used for authentication.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system. This project is setup for using `nox`.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://python.org/) - Programming Language

## ✍️ Authors <a name = "authors"></a>

- [@jjfantini](https://github.com/jjfantini) - Template Maker
- [@jjfantini](https://github.com/jjfantini) - Initial work

See also the list of [contributors](https://github.com/jjfantini/orghi-memory/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Thank you to [@mattdl-radix](https://github.com/mattdl-radix) for the original template.
- Hat tip to anyone whose code was used
- Inspiration
- References

# ----- Extra Info -----

## Python Project Template

This project is a template for creating Python projects that follows the Python Standards declared in PEP 621. It uses a pyproject.yaml file to configure the project and poetry to simplify the build process and publish to PyPI. You can manage all relevant configurations within the pyproject.toml file, streamlining development and promoting maintainability by centralizing project metadata, dependencies, and build specifications in one place.

## Project Organization

- `.github/workflows`: Contains GitHub Actions used for building, testing, and publishing.
- `.devcontainer/Dockerfile`: Contains Dockerfile to build a development container for VSCode with all the necessary extensions for Python development installed.
- `.devcontainer/devcontainer.json`: Contains the configuration for the development container for VSCode, including the Docker image to use, any additional VSCode extensions to install, and whether or not to mount the project directory into the container.
- `.vscode/settings.json`: Contains VSCode settings specific to the project, such as the Python interpreter to use and the maximum line length for auto-formatting.
- `src`: Place new source code here.
- `tests`: Contains Python-based test cases to validate source code.
- `pyproject.toml`: Contains metadata about the project and configurations for additional tools used to format, lint, type-check, and analyze Python code.
- `.prompts/`: Contains useful prompts to use during development for modifying and generating code and tests.
