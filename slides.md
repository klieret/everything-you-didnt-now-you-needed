---
# try also 'default' to start simple
theme: default
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

* **Making it practical:**
  * The [pre-commit framework](https://pre-commit.com/) is a python package that makes configuring pre-commit hooks easy!
  * All hooks are configured with a single `.pre-commit-config.yaml` file
  * Few-clicks GitHub integration availble: [pre-commit.ci](https://pre-commit.ci/) 



* **🏗️ Setting it up:**
  1. `pip3 install pre-commit`
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

# Hot code reloading

* **⁉️ Problem:** 
  1. I have some code in a notebook and some code in a python file. 
  2. I update my python file. 
  3. Do I have to restart the kernel and rerun to see the changes?
* **💡Solution:** No! Python supports a number of ways to "reload" imported code.

Add

```python
%load_ext autoreload
%autoreload 2
```

to your notebook (or IPython environment).


---

# Cookiecutter

---

# SSH config

Aliases for servers with Ssh_config , aliases for common git commands with git_config

---

# Autojump

---

# oh-my-zsh!

zsh, oh-my-zsh  for auto-complete on steroids (or fish?)

---

# Jupyter and git

Making Jupyter and git play together nicely

---

# GitHub autopilot

---

# Lockfiles and locking package managers

---

# Task runners (nox, possibly hatch)

---

# PyTest tricks

---

# Python libraries: Rich

