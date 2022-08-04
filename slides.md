---
# try also 'default' to start simple
theme: academic
# show line numbers in code blocks
lineNumbers: true
# some information about the slides, markdown enabled
info: |
  ## Everything you didn't know you needed

  Tipps and tricks for python, shell and more
---

# Everything\* you didn't know you needed
\*well, some things

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
* **💡Solution:**
  * *git hooks* allow you to run scripts that are triggered by certain actions
  * a pre-commit hook is triggered every time you run `git commit`
    * in principle you can set them up yourself by placing scripts into `.git/hooks`

::right::

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

---

# Pre-commit hooks 🪝
A config that will always be useful

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
    -   id: check-added-large-files
    -   id: check-case-conflict
    -   id: check-merge-conflict
    -   id: detect-private-key
    -   id: end-of-file-fixer
    -   id: trailing-whitespace

-   repo: https://github.com/codespell-project/codespell  # the spell checker with ~0 false positives
    rev: 'v2.1.0'
    hooks:
    -   id: codespell
        # uncomment and add a codespell.txt file to catch exceptions
        # args: ["-I", "codespell.txt"]

# Make a github bot open PRs to update the `rev` field periodically
ci:
    autoupdate_schedule: monthly

```

---

# Pre-commit hooks for python!

```yaml
-   repo: https://github.com/psf/black  # Reformat code without compromises!
    rev: 22.6.0
    hooks:
    -   id: black
    -   id: black-jupyter
-   repo: https://github.com/PyCQA/flake8  # Simple static checks
    rev: '4.0.1'
    hooks:
    -   id: flake8
        additional_dependencies: ['flake8-bugbear']
-   repo: https://github.com/pre-commit/mirrors-mypy  # Check typing (slightly more advanced)
    rev: 'v0.971'
    hooks:
    -   id: mypy
-   repo: https://github.com/asottile/pyupgrade  # Automatically switch to using the newest python features
    rev: v2.37.2
    hooks:
    -   id: pyupgrade
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
* **💡Solution:** No! Python supports a number of ways to "reload" imported code.
* **Easiest example**: Add the following to your Jupyter notebook<sup>1</sup> to reload all (!) modules every time you execute code

```python
%load_ext autoreload
%autoreload 2
```


<Footnotes separator>
  <Footnote :number=1>or any IPython system</Footnote>
</Footnotes>

::right::

* **More granular**:

```python
import mymodule
import imp

# change mymodule

imp.reload(mymodule)
```

* **Warning:** These tricks don't *always* work and there's some additional tricks (e.g., you might need to re-run `from mymodule import X` lines)
* **Try it out!** Follow our instructions [here](https://github.com/klieret/everything-you-didnt-now-you-needed/tree/main/examples/hot_code_reloading).

---
layout: two-cols
---

# Cookiecutter

* **⁉️ Problem:** Setting up e.g., a python package with unit testing/CI/CD, pre-commits, license, packaging information, etc., is a lot of "scaffolding" to be added.
* **💡Solution:** Creating templates
* **🧰 Making it practical:** [cookiecutter](https://pypi.org/project/cookiecutter/) is a command line utility for project templates

::right::

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

---

# SSH Config

* **⁉️ Problem:** Typing long servernames and potentially tunnelling can be tiresome
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
    ProxyCommand ssh tigressgateway -W %h:%p
```

Now you can use `ssh tiger` or `ssh tiger-t` depending on whether to tunnel or not.

---

# SSH Escape Sequences

* **⁉️ Problem:** I already have an SSH session. How can I quickly forward a port.
* **💡Solution:** SSH Escape Sequences:
  * Hit <kbd>Enter</kbd> <kbd>~</kbd> <kbd>C</kbd> (now you should see a `ssh>` prompt)
  * Add `-L 8000:localhost:8000` <kbd>Enter</kbd> to forward port 8000
  * You can add any other option (e.g., `-X`) to modify your existing connection

---

# Autojump

* **⁉️ Problem:** Changing directories in the terminal is cumbersome.
* **💡Solution:** Autojump learns which directories you visit often. Hit `j <some part of directory name>` to directly jump there
* Installation instructions on [github](https://github.com/wting/autojump)

Usage:

```bash
cd codas-hep  # <-- autojump remembers this

cd ../../my-directory
cd some-subfolder

j codas  # <-- get back to codas-hep folder
```

---

# Terminal kung-fu

* 💡 You can quickly search through your terminal history with <kbd>Ctrl</kbd> <kbd>R</kbd>
* 💡 You can reference the last word of the previous command with `!$`

```bash
mkdir /path/to/some/directory/hello-world
cd !$
```

* 💡 Many more tricks! Read up on your shell!
* 💡 If you're using `bash`, consider switch to `zsh` (almost completely compatible) and install `oh-my-zsh` to get beautiful prompts, autocomplete on steroids and many small benefits

```bash
$ ~/D/P/x⇥
~/Document/Projects/xonsh/
$ part⇥
this-is-part-of-a-filename
```


---

# Tracking Jupyter notebooks with git

* **⁉️ Problem:** Tracking & collaborating on Jupyter notebooks with git is a mess because of binary outputs (images) and additional metadata:
  * `git diff` becomes unreadable
  * merge conflicts appear often
* **💡Solutions:** You have several options
  1. Always strip output from notebooks before committing (easy but half-hearted)
  2. Synchronize Jupyter notebooks and python files; only track python files (slightly more advanced but best option IMO)
  3. Do not change how you *track* Jupyter notebooks; change how you *compare* them (use if you *really* want to track outputs)
  4. Avoid large amounts of code in notebooks so that the issue is less important; create python packages and use hot code reloading instead


---

# Tracking Jupyter notebooks with git

**Option 1:** Track notebooks but strip outputs before committing. Add the following pre-commit hook:

```yaml
-   repo: https://github.com/kynan/nbstripout
    rev: 0.5.0
    hooks:
    -   id: nbstripout
```

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

---

# Lockfiles and locking package managers

---

# Task runners (nox, possibly hatch)

---

# PyTest tricks

---

# Python libraries: Rich
