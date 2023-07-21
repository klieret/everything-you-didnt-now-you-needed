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

CoDaS-HEP school 2023

Slides available as [<mdi-github/> open source](https://github.com/klieret/everything-you-didnt-now-you-needed), contributions welcome.

---
layout: center
---

# Git & starting new projects

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
  rev: '4.4.0'
  hooks:
  - id: check-added-large-files
  - id: check-case-conflict
  - id: check-merge-conflict
  - id: detect-private-key
  - id: end-of-file-fixer
  - id: trailing-whitespace

- repo: https://github.com/codespell-project/codespell  # the spell checker with ~0 false positives
  rev: 'v2.2.5'
  hooks:
  - id: codespell
    # args: ["-I", "codespell.txt"]  # Optional to add exceptions

ci:
    autoupdate_schedule: monthly # default is weekly
```

See [Scientific Python Development Guidelines](https://learn.scientific-python.org/development/guides/style) for many more, updated weekly!

---

# Pre-commit hooks for python!

```yaml
    # Reformat code without compromises!
-   repo: https://github.com/psf/black
    rev: '23.7.0'
    hooks:
    -   id: black
    # Static checks
-   repo: https://github.com/astral-sh/ruff-pre-commit
    rev: 'v0.0.278'
    hooks:
    -   id: ruff
        args: [--fix, --show-fixes]
    # Check typing (slightly more advanced)
-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: 'v1.4.1'
    hooks:
    -   id: mypy
```

* **Try it out**: Go [here](https://github.com/klieret/python-pre-commit-demo-tutorial) for a quick step-by-step tutorial

---
layout: two-cols
---

# Cookiecutter


* **⁉️ Problem:** Setting up a python package with unit testing/CI/CD, pre-commits, license, packaging information, etc., is a lot of "scaffolding" to be added.

<v-click>

* **💡Solution:** Creating templates
* **🧰 Making it practical:** [cookiecutter](https://pypi.org/project/cookiecutter/) is a command line utility for project templates

</v-click>

::right::

<v-click>

* **Example**: [Scientific Python Cookie](https://github.com/scientific-python/cookie): All the features, all the best-practices
* **💡 Pro-tip**: [cruft](https://cruft.github.io/cruft/) is a cookiecutter extension that allows to propagate updates to the template back to the projects that use it
* **💡 Pro-tip**: [copier](https://copier.readthedocs.io) is another powerful tool that supports updates (and works with the template above).

* **Trying it out**:

```bash
pipx install cookiecutter
# alternative: cruft or copier
cookiecutter gh:scientific-python/cookie
# e.g., select project type = hatchling
# for a very simple start that grows with you.
```

</v-click>

---
layout: center
---

# SSH & Terminal Kung-fu

---

# SSH Config

* **⁉️ Problem:** Typing long server names and potentially tunnelling can be tiresome

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
   * 🔥 Install [fzf](https://github.com/junegunn/fzf) as a plugin to your shell
     to get an interactive fuzzy finding pop-up instead (interactively filter through list of results rather than just seeing one)

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

* 💡 If you're using `bash`, consider switching to [`zsh`](https://en.wikipedia.org/wiki/Z_shell) (almost completely compatible) and install [`oh-my-zsh`](https://ohmyz.sh/) to get beautiful prompts, autocomplete on steroids and many small benefits

```bash
$ ~/D/P/x⇥
~/Document/Projects/xonsh/
$ part⇥
this-is-part-of-a-filename
```

</v-click>

---

# How to shell...

* **⁉️ Problem:** `man` pages are wasting your time?

<v-click>

* **💡Solution:**   Try [`tldr`](https://tldr.sh/) (`pipx install tldr`). Compare:


<div style="align: center">
&nbsp;
<figure class="half" style="display:flex">
<img src="/man.png" style="width:  35%"/>
<img src="/tldr.png" style="width:  35%"/>
</figure>
</div>

</v-click>

---

# How to shell...

* **⁉️ Problem:** Understanding cryptic bash commands

<v-click>

* **💡Solutions:** Go to [explainshell.com](https://explainshell.com/explain?cmd=%3A%28%29%7B+return+1%3B+%7D%3B%3A+%7C%7C+echo+test)

<img src="/explainshell.png" style="height: 80%; margin: auto;"/>

</v-click>

---

# File navigation and completion

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

# File navigation and completion

* **⁉️ Problem:** I like visual file managers, but I'm working on a server...

<v-click>

* **💡Solution:**  Use a terminal file manager, e.g., [`ranger`](https://github.com/ranger/ranger)

<img src="/ranger.png" style="width: 50%; margin: auto;"/>
</v-click>

<v-click>

* **⁉️ Problem**: I search through files a lot, but `grep` is slow/inconvenient...

</v-click>
<v-click>

* **💡Solution:** There are faster and more feature-rich alternatives. Example: [ripgrep](https://github.com/BurntSushi/ripgrep), [`ag`](https://github.com/ggreer/the_silver_searcher), ...

</v-click>

<v-click>

* **⁉️ Problem:**  Even with tab completion, completing file names is cumbersome.

</v-click>
<v-click>

* **💡Solution:**  Try type-ahead-searching/fuzzy matching, e.g., with [`fzf`](https://github.com/junegunn/fzf) with [shell integration](https://github.com/junegunn/fzf#fuzzy-completion-for-bash-and-zsh), e.g., `vim ../**`<kbd>Tab</kbd> starts searching with `fzf` in parent dir

</v-click>

---
layout: center
---

# Python + Jupyter

---
layout: two-cols
---

# Hot code reloading

* **⁉️ Problem:**
  1. I have some code in a notebook and some code in a python file/library.
  2. I update my python file/library.
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

# Tracking Jupyter notebooks with git

* **⁉️ Problem:** Tracking & collaborating on Jupyter notebooks with git is a mess because of binary outputs (images) and additional metadata:
  * `git diff` becomes unreadable
  * merge conflicts appear often

<v-click>

* **💡Solutions:** You have several options
  1. Always strip output from notebooks before committing (easy but half-hearted)
  2. Synchronize Jupyter notebooks and python files; only track python files (slightly more advanced but best option IMO)
  3. Do not change how you *track* Jupyter notebooks; change how you *compare* them (use if you *really* want to track outputs). Example: [`nbdime`](https://nbdime.readthedocs.io/en/latest/)
  4. Avoid large amounts of code in notebooks so that the issue is less important; create python packages and use hot code reloading instead

</v-click>

---

# Tracking Jupyter notebooks with git

**Option 1:** Track notebooks but strip outputs before committing. Add the following pre-commit hook:

```yaml
- repo: https://github.com/kynan/nbstripout
  rev: 0.6.1
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

# Static code checkers and Jupyter notebooks

* **⁉️ Problem:** I still have lots of code in my notebooks. I still want to apply tools on notebooks.

<v-click>

* **💡Solution:**: Black and Ruff support jupyter notebooks natively!

* **💡 Pro-tip**: [`nbqa`](https://github.com/nbQA-dev/nbQA) allows other tools to be applied, as well.

```yaml
    # Reformat code without compromises!
-   repo: https://github.com/psf/black
    rev: '23.7.0'
    hooks:
    -   id: black-jupyter
    # Static checks
-   repo: https://github.com/astral-sh/ruff-pre-commit
    rev: 'v0.0.278'
    hooks:
    -   id: ruff
        types_or: [python, pyi, jupyter]
        args: [--fix, --show-fixes]
```

</v-click>

---

# Various tricks with Jupyter

* **⁉️ Problem:** I want to preview/run Jupyter notebooks in my terminal.
* **💡Solution:**
  * `pipx run nbpreview` if you're only interested in previewing
  * `pipx run rich-cli` also works
  * `pipx run nbterm` for interactively executing notebooks in the terminal

---
layout: center
---

# Python

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

* **💡Solution:**
  * A task runner (nox, tox, hatch) can create a reproducible environment with no setup.
  * Nox is nice because it uses Python for configuration, and prints what it is doing.

&nbsp;

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

</v-click>

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

# pytest: Make testing fun

## Basics

`pytest` discovers test functions named `test_...` in files `test_...`. For example:

```python
def test_funct():
    assert 4 == 2**2
```

To run: `pip install pytest` and then `pytest` to discover & run them all.


<v-click>

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

</v-click>

---

# pytest: Make testing fun

* `--showlocals`: Show all the local variables on failure
* `--pdb`: Drop directly into a debugger on failure
* `--trace --lf`: Run the last failure & start in a debugger
* You can also add `breakpoint()` in your code to get into a debugger


&nbsp;

Reminder: https://learn.scientific-python.org/development/guides/pytest is a great place to look for tips!

---
layout: two-cols
---

# pytest: Make testing fun

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

<v-click>

### Fixtures allow reuse, setup, etc

There are quite a few built-in fixtures. And you can write more:

```python
@pytest.fixture
def my_complex_object():
    mco = MyComplexObject(...)
    mco.xyz = "asf"
    ...
    return mco

def test_get_value(my_complex_object):
    assert my_complex_object.get_value() == ...

def test_other_property(my_complex_object):
    assert my_complex_object.property == ...
```

</v-click>
<v-click>

### Monkeypatching

System IO, GUIs, hardware, slow processes; there are a lot of things that are hard to test! Use monkeypatching to keep your tests fast and "unit".

</v-click>

---

# Type checking

* **⁉️ Problem:** Compilers catch lots of errors in compiled languages that are runtime errors in Python! Python can't be used for lots of code!

<v-click>

* **💡Solution:** Add types and run a type checker.

```python
def f(x: float) -> float:
    y = x**2
    return y
```

* Functions always have types in and out
* Variable definitions rarely have types

</v-click>
<v-click>

How do we use it? (requires `pipx install mypy`)

```bash
mypy --strict tmp.py
  Success: no issues found in 1 source file
```

Some type checkers: MyPy (Python), Pyright (Microsoft), Pytype (Google), or Pyre (Meta).

👉 Example files available [here](https://github.com/klieret/everything-you-didnt-now-you-needed/tree/main/examples/typed_python).

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
  rev: "v1.4.1"
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
        uses: actions/configure-pages@v3

      # Static site generation, latex, etc. here

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
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
        uses: actions/deploy-pages@v2
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

* **💡Solution:** Use the browser to _run_ the code with a WebAssembly distribution, like Pyodide. Python 3.11 officially supports it now too!

</v-click>

<v-click>

## Pyodide

A distribution of CPython 3.11 including ~100 binary packages like SciPy, Pandas, boost-histogram (Hist), etc.

Examples:

* https://learn.scientific-python.org/development/guides/repo-review

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
  <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
  <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head>
<body>
  <script type="py-script">
    print("Hello, World!")
  </script>
</body>
</html>
```

https://docs.pyscript.net/latest/tutorials/getting-started.html

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

* https://learn.scientific-python.org/development/guides/packaging-simple/
* https://packaging.python.org/en/latest/tutorials/packaging-projects

`scientific-python/copier` supports 12 backends; hatching is recommended for pure Python. For compiled extensions: See next slides(s). 😀

</v-click>

---

# Binary packaging


* **⁉️ Problem:** Making a package with binaries is hard.

<v-click>

* **💡Solution:** I've been working on making it easy!

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

I'm funded to work on scikit-build for three years! CMake for Python packaging.


::right::

Org of several packages:

* Scikit-build
* Scikit-build-core
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
    - uses: actions/checkout@v3

    - name: Build wheels
      uses: pypa/cibuildwheel@v2.14

    - uses: actions/upload-artifact@v3
      with:
        path: ./wheelhouse/*.whl
```

---
layout: two-cols
---

## CMake example

You can make a working example with just three files!

### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_core MODULE src/main.cpp)
install(TARGETS _core DESTINATION ${SKBUILD_PROJECT_NAME})
```

::right::

### pyproject.toml

```toml
[build-system]
requires = ["scikit-build-core", "pybind11"]
build-backend = "scikit_build_core.build"

[project]
name = "package"
version = "0.1.0"
```

### src/main.cpp

```cpp
#include <pybind11/pybind11.h>

int add(int i, int j) { return i + j; }

namespace py = pybind11;

PYBIND11_MODULE(_core, m) {
  m.def("add", &add);
}
```
