---
# try also 'default' to start simple
theme: academic
# show line numbers in code blocks
lineNumbers: true
# some information about the slides, markdown enabled
info: |
  ## Everything you didn't know you needed

  Tips and tricks for python, shell and more
---

# Everything\* you didn't know you needed
\*blatant marketing nonsense

Kilian Lieret and Henry Schreiner

Princeton University

CoDaS-HEP school 2022

Slides available as [<mdi-github/> open source](https://github.com/klieret/everything-you-didnt-now-you-needed), contributions welcome.

---
layout: two-cols
---

# Pre-commit hooks 🪝
Run small checks *before* you commit


* **⁉️ Problem:** How can I stop myself from committing low-quality code?

<v-click>

* **💡Solution:**
  * *git hooks* allow you to run scripts that are triggered by certain actions
  * a pre-commit hook is triggered every time you run `git commit`
    * in principle you can set them up yourself by placing scripts into `.git/hooks`

</v-click>

::right::

<v-click>

* **🧰 Making it practical:**
  * The [pre-commit framework](https://pre-commit.com/) is a python package that makes configuring pre-commit hooks easy!
  * All hooks are configured with a single `.pre-commit-config.yaml` file
  * Few-clicks GitHub integration available: [pre-commit.ci](https://pre-commit.ci/)
* **🏗️ Setting it up:**
  1. `pipx install pre-commit`
  2. `cd <your repo>`
  3. `touch .pre-commit-config.yaml`
  3. `pre-commit install`
  4. Profit 🎉

</v-click>
---

# Pre-commit hooks 🪝
A config that will always be useful. Optional pre-commit.ci CI service.

```yaml
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: 'v4.3.0'
  hooks:
  - id: check-added-large-files
  - id: check-case-conflict
  - id: check-merge-conflict
  - id: detect-private-key
  - id: end-of-file-fixer
  - id: trailing-whitespace

- repo: https://github.com/codespell-project/codespell  # the spell checker with ~0 false positives
  rev: 'v2.1.0'
  hooks:
  - id: codespell
    # args: ["-I", "codespell.txt"]  # Optional to add exceptions

ci:
    autoupdate_schedule: monthly # default is weekly
```

See https://scikit-hep.org/developer/style for many more, updated weekly!

---a

# Pre-commit hooks for python!

```yaml
-   repo: https://github.com/psf/black  # Reformat code without compromises!
    rev: '22.6.0'
    hooks:
    -   id: black
    # or, if you also work with Jupyter notebooks
    # -   id: black-jupyter
-   repo: https://github.com/PyCQA/flake8  # Simple static checks
    rev: '5.0.1'
    hooks:
    -   id: flake8
        additional_dependencies: ['flake8-bugbear']
-   repo: https://github.com/pre-commit/mirrors-mypy  # Check typing (slightly more advanced)
    rev: 'v0.971'
    hooks:
    -   id: mypy
-   repo: https://github.com/asottile/pyupgrade  # Automatically upgrade old Python syntax
    rev: 'v2.37.2'
    hooks:
    -   id: pyupgrade
        args: [--py37-plus]
```

* **Try it out**: Go [here](https://github.com/klieret/python-pre-commit-demo-tutorial) for a quick step-by-step tutorial

---
layout: two-cols
---

# Hot code reloading

* **⁉️ Problem:**
  1. I have some code in a notebook and some code in a python file.
  2. I update my python file.
  3. Do I have to restart the kernel and rerun to see the changes?

<v-click>

* **💡Solution:** No! Python supports a number of ways to "reload" imported code.
* **Easiest example**: Add the following to your Jupyter notebook<sup>1</sup> to reload all (!) modules every time you execute code

```python
%load_ext autoreload
%autoreload 2  # reload everything
```


<Footnotes separator>
  <Footnote :number=1>or any IPython system</Footnote>
</Footnotes>

</v-click>

::right::

<v-click>

* **More granular**:

```python
%load_ext autoreload
%autoreload 1  # <-- reload only some modules

# Mark for reloading
%aimport foo
```

* **Warning:** These tricks don't *always* work, but it should save you from a lot of restarts
* **Try it out!** Follow our instructions [here](https://github.com/klieret/everything-you-didnt-now-you-needed/tree/main/examples/hot_code_reloading).
* **More information**: See the [autoreload documentation](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html)

</v-click>

---
layout: two-cols
---

# Cookiecutter


* **⁉️ Problem:** Setting up e.g., a python package with unit testing/CI/CD, pre-commits, license, packaging information, etc., is a lot of "scaffolding" to be added.

<v-click>

* **💡Solution:** Creating templates
* **🧰 Making it practical:** [cookiecutter](https://pypi.org/project/cookiecutter/) is a command line utility for project templates

</v-click>

::right::

<v-click>

* **Examples**:
  * [scikit-hep project template](https://github.com/scikit-hep/cookie/): All the features, all the best-practices
  * [my personal python template](https://github.com/scikit-hep/cookie/): Fewer options, easier to read (I think ;))
* **💡 Pro-tip**: [cruft](https://cruft.github.io/cruft/) is a cookiecutter extension that allows to propagate updates to the template back to the projects that use it

* **Trying it out**:

```bash
pipx install cookiecutter
# alternative: cruft https://...
cookiecutter https://github.com/scikit-hep/cookie/
# e.g., select project type = setuptools
# for the "traditional" way to set up your python
# package
```

</v-click>

---

# SSH Config

* **⁉️ Problem:** Typing long servernames and potentially tunnelling can be tiresome

<v-click>

* **💡Solution:** Create configuration in  `~/.ssh/config`. You can even add pattern matching!

```bash
# Server I want to connect to
Host tiger*
    Hostname tiger.princeton.edu
    User kl5675

# Tunnel that I might use sometimes
Host tigressgateway
    Hostname tigressgateway.princeton.edu
    User kl5675

Host *-t
    ProxyJump tigressgateway
```

Now you can use `ssh tiger` or `ssh tiger-t` depending on whether to tunnel or not.

</v-click>

---

# SSH Escape Sequences

* **⁉️ Problem:** I already have an SSH session. How can I quickly forward a port?

<v-click>

* **💡Solution:** SSH Escape Sequences:

  * Hit <kbd>Enter</kbd> <kbd>~</kbd> <kbd>C</kbd>  (now you should see a `ssh>` prompt)
  * Add `-L 8000:localhost:8000` <kbd>Enter</kbd> to forward port 8000
  * More escape sequences available! [More information.](https://www.microfocus.com/documentation/rsit-server-client-unix/8-4-0/unix-guide/ssh_escape_ap.html)

* **Caveat**: <kbd>C</kbd> option not available in multiplexed sessions.

</v-click>

---

# Terminal kung-fu

<v-click>

* 💡 You can quickly search through your terminal history with <kbd>Ctrl</kbd> <kbd>R</kbd> - start typing
   * Hit <kbd>Ctrl</kbd> <kbd>R</kbd> to navigate between different hits

</v-click>
<v-click>

* 💡 You can reference the last word of the previous command with `!$`

```bash
mkdir /path/to/some/directory/hello-world
cd !$
```

</v-click>
<v-click>

* 💡 Want to fix up a complicated command that just failed? Type `fc` to edit the command in your `$EDITOR`

</v-click>
<v-click>

* 💡 If you're using `bash`, consider switching to `zsh` (almost completely compatible) and install `oh-my-zsh` to get beautiful prompts, autocomplete on steroids and many small benefits

```bash
$ ~/D/P/x⇥
~/Document/Projects/xonsh/
$ part⇥
this-is-part-of-a-filename
```

</v-click>

---

# Autojump

* **⁉️ Problem:** Changing directories in the terminal is cumbersome.

<v-click>

* **💡Solution:** Autojump learns which directories you visit often. Hit `j <some part of directory name>` to directly jump there
* Installation instructions on [github](https://github.com/wting/autojump)

Usage:

```bash
cd codas-hep  # <-- autojump remembers this

cd ../../my-directory
cd some-subfolder

j codas  # <-- get back to codas-hep folder
```

</v-click>


---

# More tools for the terminal

*

---

# Tracking Jupyter notebooks with git

* **⁉️ Problem:** Tracking & collaborating on Jupyter notebooks with git is a mess because of binary outputs (images) and additional metadata:
  * `git diff` becomes unreadable
  * merge conflicts appear often

<v-click>

* **💡Solutions:** You have several options
  1. Always strip output from notebooks before committing (easy but half-hearted)
  2. Synchronize Jupyter notebooks and python files; only track python files (slightly more advanced but best option IMO)
  3. Do not change how you *track* Jupyter notebooks; change how you *compare* them (use if you *really* want to track outputs)
  4. Avoid large amounts of code in notebooks so that the issue is less important; create python packages and use hot code reloading instead

</v-click>

---

# Tracking Jupyter notebooks with git

**Option 1:** Track notebooks but strip outputs before committing. Add the following pre-commit hook:

```yaml
- repo: https://github.com/kynan/nbstripout
  rev: 0.5.0
  hooks:
  - id: nbstripout
```

<v-click>

**Option 2:** Synchronize Jupyter notebooks (untracked) to python files (tracked)

```bash
pipx install jupytext
echo "*.ipynb" >> ~/.gitignore  # <-- tell git to ignore noteboks
jupytext --to py mynotebook.ipynb
# Now you have mynotebook.py
git commit mynotebook.py -m "..."
git push
# People modify the file online
git pull  # <-- mynotebook.py got updated
jupytext --sync  # <-- update mynotebook.ipynb
# Now make changes to your mynotebook.ipynb
jupytext --sync  # <-- now mynotebook.py got updated
git commit ... && git push ...
```

</v-click>

---

# Avoiding dependency hell

* **⁉️ Problem:** Python packages depend on other packages depending on other packages causing a conflict.
* **💡Solution:** Use conda or virtual environments (`venv`, `virtualenv`, `virtualenvwrapper`);


The first environment should be named `.venv`

* The Python Launcher for Unix, `py` picks up `.venv` automatically!
* Visual Studio Code does too, as do a growing number of other tools.

&nbsp;

<v-click>

* **⁉️ Problem:** What about `pip`-installable executables?
* **💡Solution:** Install them with `pipx` instead of `pip`! Examples:
  * `pre-commit` • `black` • `cookiecutter` • `uproot-browser`

You can also use `pipx run` to install & execute in one step, cached for a week!

</v-click>

---

# Lockfiles

* **⁉️ Problem:** Upgrades _can_ break things.

<v-click>

* **⛔️Not a solution:** Don't add upper caps to _everything_! Only things with 50%+ chance of breaking.
* **💡Solution:** Use lockfiles.

Your CI and/or application (including an analysis) should have a _completely pinned environment_ that works.
This is not your install requirements for a library!

```bash
pip install pip-tools
pip-compile requirements.in  # -> requirements.txt
```

Now you get a locked requirements file that can be installed:

```bash
pip install -r requirements.txt
```

</v-click>

---

# Locking package managers


Locking package managers (`pdm`, `poetry`, `pipenv`) give you this with a nice all-in-one CLI:

```bash
pdm init # Setup environment using existing lockfile or general requirements

# Modify pyproject.toml as needed

pdm add numpy  # Shortcut for adding to toml + install in venv
```

You'll also have a `pdm.lock` file tracking the environment it created.
You can update the locks:

```bash
pdm update
```

Read up on how to use the environment that this makes to run your app.

---

# Task runners

* **⁉️ Problem:** There are lots of way to setup environments, lots of ways to run things.

<v-click>

* **💡Solution:** A task runner (nox, tox, hatch) can create a reproducible environment with no setup.
* Nox is nice because it uses Python for configuration, and prints what it is doing.


```python
import nox

@nox.session
def tests(session):
    session.install(".[test]")
    session.run("pytest")
```

</v-click>

---

# Task runners

* **⁉️ Problem:** There are lots of way to setup environments, lots of ways to run things.


* **💡Solution:** A task runner (nox, tox, hatch) can create a reproducible environment with no setup.
* Nox is nice because it uses Python for configuration, and prints what it is doing.

```python
import nox

@nox.session
def tests(session: nox.Session) -> None:
    """
    Run the unit and regular tests.
    """
    session.install(".[test]")
    session.run("pytest", *session.posargs)
```


---
layout: two-cols
---

# Task runners

Example 1: adapted from `PyPA/manylinux`

```python
@nox.session(python=["3.9", "3.10", "3.11"])
def update_python_dependencies(session):
    session.install("pip-tools")
    session.run(
        "pip-compile", # Usually just need this
        "--generate-hashes",
        "requirements.in", # and this
        "--upgrade",
        "--output-file",
        f"requirements{session.python}.txt",
    )
```

Example 2: `python.packaging.org`

```python
@nox.session(py="3")
def preview(session):
    session.install("sphinx-autobuild")
    build(session, autobuild=True)
```

::right::


```python
@nox.session(py="3")
def build(session, autobuild=False):
    session.install("-r", "requirements.txt")
    shutil.rmtree(target_build_dir,
                  ignore_errors=True)

    if autobuild:
        command = "sphinx-autobuild"
        extra_args = "-H", "0.0.0.0"
    else:
        command = "sphinx-build"
        extra_args = (
            "--color",
            "--keep-going",
        )

    session.run(
        command, *extra_args,
        "-j", "auto",
        "-b", "html",
        "-n", "-W",
        *session.posargs,
        "source", "build",
    )
```

---

# pytest tricks (config)

Reminder: https://scikit-hep.org/developer/pytest is a great place to look for tips!

## Basics

`pytest` discovers test functions named `test_...` in files `test_...`. For example:

```python
def test_funct():
    assert 4 == 2**2
```

To run: `pip install pytest` and then `pytest` to discover & run them all.


## First tip: your `project.toml` file

```toml
[tool.pytest.ini_options]
minversion = "6.0"  # minimal version of pytest
# report all; check that markers are configured; check that config is OK
addopts = ["-ra", "--strict-markers", "--strict-config"]
xfail_strict = true  # tests marked as failing must fail
filterwarnings = ["error"]
log_cli_level = "info"
testpaths = ["tests"]  # search for tests in "test" directory
```

---

# pytest tricks (running)

* `--showlocals`: Show all the local variables on failure
* `--pdb`: Drop directly into a debugger on failure
* `--trace --lf`: Run the last failure & start in a debugger
* You can also add `breakpoint()` in your code to get into a debugger


---
layout: two-cols
---

# pytest tricks (running)

### Approx

```python
def test_approx():
    0.3333333333333 == pytest.approx(1 / 3)
```

This works natively on arrays, as well!

### Test for errors

```python
def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

### Marks


```python
@pytest.mark.skipif("sys.version_info >= (3, 7)")
def test_only_on_37plus():
    x = 3
    assert f"{x = }" == "x = 3"
```

::right::

### Fixtures allow reuse, setup, etc

There are quite a few built-in fixtures. And you can write more:

```python
@pytest.fixture(
    params=["Linux", "Darwin", "Windows"],
    autouse=True)
def platform_system(request, monkeypatch):
    monkeypatch.setattr(
        platform, "system", lambda _: request.param)

def test_thing(platform_system: str):
    assert platform in {"Linux", "Darwin", "Windows"}
```

### Monkeypatching

System IO, GUIs, hardware, slow processes; there are a lot of things that are hard to test! Use monkeypatching to keep your tests fast and "unit".

---

# Type checking

* **⁉️ Problem:** Compilers catch lots of errors in compiled languages that are runtime errors in Python! Python can't be used for lots of code!

<v-click>

* **💡Solution:** Add types and run a type checker.

Typed code looks like this:

```python
def f(x: float) -> float:
    y = x**2
    return y
```

* Functions always have types in and out
* Variable definitions rarely have types

How do we use it?

```bash
mypy --strict tmp.py
  Success: no issues found in 1 source file
```

Some type checkers: MyPy (Python), Pyright (Microsoft), Pytype (Google), or Pyre (Meta).

</v-click>

---

# Type checking (details)

* Adds text - but adds _checked content_ for the reader!
* External vs. internal typing
* Libraries need to provide typing _or_ stubs can be written
* Many stubs are available, and many libraries have types (numpy, for example)
* An _active_ place of development for Python & libraries!


```python
from __future__ import annotations


def f(x: int) -> list[int]:
    return list(range(x))


def g(x: str | int) -> None:
    if isinstance(x, str):
        print("string", x.lower())
    else:
        print("int", x)
```
---

# Type checking (Protocol)

But Python is duck-typed! Nooooooo!

<v-click>

Duck typing can be formalized by a Protocol:

```python {all|3-5|7-8|10-12|14-15}
from typing import Protocol  # or typing_extensions for < 3.8

class Duck(Protocol):
    def quack(self) -> str:
        ...

def pester_duck(a_duck: Duck) -> None:
    print(a_duck.quack())

class MyDuck:
    def quack(self) -> str:
        return "quack"

# Check explicitly that MyDuck is implementing the Duck protocol
if typing.TYPE_CHECKING:
    _: Duck = typing.cast(MyDuck, None)
```

</v-click>

---

# Type checking (pre-commit)

```yaml
- repo: https://github.com/pre-commit/mirrors-mypy
  rev: "v0.971"
  hooks:
    - id: mypy
      files: src
      args: []
      additional_dependencies: [numpy==1.22.1]
```

* Args should be empty, or have things you add (pre-commit's default is poor)
* Additional dependencies can exactly control your environment for getting types

## Benefits

* Covers all your code without writing tests
  * Including branches that you might forget to run, cases you might for forget to add, etc.
* Adds vital information for your reader following your code
* All mistakes displayed at once, good error messages
* Unlike compiled languages, you can lie if you need to
* You can use `mypyc` to compile (2-5x speedup for mypy, 2x speedup for black)

---
layout: two-cols
---

# GitHub Actions: pages deploy

Bonus: About a week ago GitHub Actions added direct deploy to pages!

```yaml
on:
  workflow_dispatch:
  pull_request:
  push:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

::right::

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v1

      # Static site generation, latex, etc. here

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          path: dist/

  deploy:
    if: github.ref == 'refs/heads/main'
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v1
```

---

# ACT (for GitHub Actions)

* **⁉️ Problem:** You use GitHub Actions for everything. But what if you want to test the run out locally?

<v-click>

* **💡Solution:** Use ACT (requires Docker)!

```bash
# Install with something like brew install act

act  # Runs on: push

act pull_request -j test  # runs the test job as if it was a pull request
```

If you use a task runner, like nox, you should be able to avoid this most of the time. But it's handy in a pinch! https://github.com/nektos/act

</v-click>

---

# Python libraries: Rich, Textual, Rich-cli

Textualize is one of the fastest growing library families. Recently Rich was even vendored into Pip!

<v-click>

### progress bar demo (Using Python 3.11 TaskGroups, because why not)

```python
from rich.progress import Progress
import asyncio

async def lots_of_work(n: int, progress: Progress) -> None:
    for i in progress.track(range(n), description=f"[red]Computing {n}..."):
        await asyncio.sleep(.1)

async def main():
    with Progress() as progress:
        async with asyncio.TaskGroup() as g:
            g.create_task(lots_of_work(40, progress))
            g.create_task(lots_of_work(30, progress))

asyncio.run(main())
```
</v-click>

---
layout: two-cols
---

## Rich: Beautiful terminal output

Rich is not just a "color terminal" library.

- Color and styles
- Console markup
- Syntax highlighting
- Tables, panels, trees
- Progress bars and live displays
- Logging handlers
- Inspection
- Traceback formatter
- Render to SVG

::right::

![](https://rich.readthedocs.io/en/stable/_images/svg_export.svg)

---

## Textual: GUI? No, TUI!

New "CSS" version coming soon!

![](https://github.com/Textualize/textual/raw/main/imgs/textual.png)

---
layout: two-cols
---

## Rich-cli: Rich as a command line tool


<img src="https://raw.githubusercontent.com/Textualize/rich-cli/main/imgs/syntax1.png" style="width:95%;"/>

<img src="https://raw.githubusercontent.com/Textualize/rich-cli/main/imgs/markdown1.png" style="width:95%;"/>

::right::

![](https://raw.githubusercontent.com/Textualize/rich-cli/main/imgs/rich-cli-splash.jpg)

---

# WebAssembly

* **⁉️ Problem:** Distributing code is hard. Binder takes time to start & requires running the code one someone else's machine.

<v-click>

* **💡Solution:** Use the browser to _run_ the code with a WebAssembly distribution, like Pyodide. Python 3.11 officially supports it now too! Binaries may be provided around 3.12!

</v-click>

<v-click>

## Pyodide

A distribution of CPython 3.10 including ~100 binary packages like SciPy, Pandas, boost-histogram (Hist), etc.

Examples:

* https://henryiii.github.io/level-up-your-python/live/lab/index.html
* https://scikit-hep.org/developer/reporeview

</v-click>

<v-click>

## PyScript

An Python interface for Pyodide in HTML.

</v-click>
---

# WebAssembly - PyScript


```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hello, World!</title>
  <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
<body>
  <py-script>print("Hello, World!")</py-script>
</body>
</html>
```

https://realpython.com/pyscript-python-in-browser

---

# Modern packaging

* **⁉️ Problem:** Making a package is hard.

<v-click>

* **💡Solution:** It's not hard anymore. You just need to use modern packaging and avoid old examples.


```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "package"
version = "0.0.1"
```

Other metadata should go there too, but that's the minimum. See links:

* https://scikit-hep.org/developer/pep621
* https://packaging.python.org/en/latest/tutorials/packaging-projects

`scikit-hep/cookie` supports 11 backends; hatching is recommended for pure Python. For compiled extensions: See next slides(s). 😀

</v-click>

---

# Binary packaging


* **⁉️ Problem:** Making a package with binaries is hard.

<v-click>

* **💡Solution:** Some parts are easy, and I'm working on making the other parts easy too!

</v-click>

---

## Making the code

Use a tool like pybind11, Cython, or MyPyC. It's hard to get the C API right!

```cpp
#include <pybind11/pybind11.hpp>

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(example, m) {
    m.def("add", &add);
}
```

Header only, pure C++! No dependencies, no pre-compile step, no new language.

---
layout: two-cols
---

## Configuring the build

I'm working on scikit-build for the next three years! CMake for Python packaging.

Currently based on distutils & setuptools - but will be rewritten!


::right::

Org of several packages:

* Scikit-build
* CMake for Python
* Ninja for Python
* moderncmakedomain
* Examples

---
layout: two-cols
---

## Building the binaries

Redistributable wheel builder.

* Targeting macOS 10.9+
* Apple Silicon cross-compiling 3.8+
* All variants of manylinux (including emulation)
* musllinux
* PyPy 3.7-3.9
* Repairing and testing wheels
* Reproducible pinned defaults (can unpin)


Local runs supported too!

```bash
pipx run cibuildwheel --platform linux
```

::right::

### GitHub actions example

```yaml
on: [push, pull_request]

jobs:
  build_wheels:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os:
        - ubuntu-22.04
        - windows-2022
        - macos-11

    steps:
    - uses: actions/checkout@v4

    - name: Build wheels
      uses: pypa/cibuildwheel@v2.8.1

    - uses: actions/upload-artifact@v3
      with:
        path: ./wheelhouse/*.whl
```
