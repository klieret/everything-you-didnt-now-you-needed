# Everything you didn't know you needed

[![PR welcome](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg)](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)
[![gh actions](https://github.com/klieret/everything-you-didnt-now-you-needed/actions/workflows/deploy.yml/badge.svg)](https://github.com/klieret/everything-you-didnt-now-you-needed/actions)

> **Note**
> 👉 [**Click here for rendered slides!**](https://klieret.github.io/everything-you-didnt-now-you-needed/) 👈

A collection of tips and tricks revolving around python, the command line and more.

Slides originally created for the [CoDaS-HEP 2022 school](https://indico.cern.ch/event/1151367/).

## ✔️ Content

* pre-commit
* Hot code reloading
* cookiecutter
* SSH config
* SSH escape sequences
* Autojump
* Command line kung-fu
* Tracking Jupyter notebooks with git
* Lockfiles and locking package managers
* Task runners
* PyTest tricks
* Type checking
* Textualize
* WebAssembly
* Packaging
* Binary packaging



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
