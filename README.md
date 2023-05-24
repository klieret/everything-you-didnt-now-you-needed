<div align="center">
<h1><a href="https://klieret.github.io/everything-you-didnt-now-you-needed/">Everything you didn't know you needed</a></h1>
<p><em>Tips and tricks for python, the command line, and more.</em></p>
<p align="center"><a href="https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project"><img src="https://img.shields.io/badge/PR-Welcome-%23FF8300.svg" alt="PR welcome"></a>
<a href="https://github.com/klieret/everything-you-didnt-now-you-needed/actions"><img src="https://github.com/klieret/everything-you-didnt-now-you-needed/actions/workflows/deploy.yml/badge.svg" alt="gh actions"></a>
<a href="https://results.pre-commit.ci/latest/github/klieret/everything-you-didnt-now-you-needed/main"><img src="https://results.pre-commit.ci/badge/github/klieret/everything-you-didnt-now-you-needed/main.svg" alt="pre-commit.ci status"></a>
<a href="https://github.com/klieret/everything-you-didnt-now-you-needed/actions/workflows/check-links.yaml"><img src="https://github.com/klieret/everything-you-didnt-now-you-needed/actions/workflows/check-links.yaml/badge.svg" alt="Check Markdown links"></a>
</p>
</div>

---

> **Note**
> 👉 [**Click here for rendered slides!**](https://klieret.github.io/everything-you-didnt-now-you-needed/) 👈

Did you every wonder about all the small productivity hacks that others use?
Then you've come to the right place!
These slides are a mixed bag of everything related to productivity with python, the command line, and more.

Slides originally created for the [CoDaS-HEP 2022 school](https://indico.cern.ch/event/1151367/).
A PDF version of the slides is available in the corresponding release.

<a href="https://klieret.github.io/everything-you-didnt-now-you-needed/"><img width="450" alt="Screenshot of slides" src="https://user-images.githubusercontent.com/13602468/201179879-741020d5-b526-4829-b0ca-a416136098f4.png"></a>


## ✔️ Content

* Command line and more:
    * `!$`, `fc`, autojump, ...
    * `tldr`, explainshell.com,
    * `grep` replacements, `fzf`, ...
    * Terminal file managers
    * SSH config
    * SSH escape sequences
* Python:
    * Hot code reloading in python
    * Task runners (`nox`)
    * PyTest tricks
    * Best practices for tracking Jupyter notebooks with git
    * `nbqa` to apply static code quality tools to Jupyter notebooks
    * Textualize
    * WebAssembly
    * Packaging
    * Type checking in python
* Software engineering:
    * pre-commit
    * cookiecutter
    * Binary packaging
    * ACT for GitHub Actions
    * Lockfiles and locking package managers

## 🔧 Note for participants

Please also clone [this repository](https://github.com/klieret/python-pre-commit-demo-tutorial) before the start of the session.

## 🌐 Other resources

* [Removing tedium from Princeton University](https://github.com/PrincetonUniversity/removing_tedium): While some small parts are specific to the setup in Princeton, the majority are very useful tips that can help everywhere!
* [Scikit-HEP developer guide](https://scikit-hep.org/developer): A very complete set of tips on how to set up your python package for success
* [Levelling up your python](https://henryiii.github.io/level-up-your-python/notebooks/0%20Intro.html): Various bits of intermediate and advanced python

Less related training material built with the same markdown-based framework:

* [Collaborative Programming with GitHub](https://github.com/klieret/collaborative-programming-github)

## 🧰 Local development

The slides are built with [Slidev](https://github.com/slidevjs/slidev).

To start the slide show locally:

- `npm install`
- `npm run dev`
- visit http://localhost:3030

Edit the [slides.md](./slides.md) to see the changes.

Learn more about Slidev on [documentations](https://sli.dev/).

When contributing, please also set up the pre-commit hooks with

```bash
pre-commit install
```
