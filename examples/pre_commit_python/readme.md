# Python pre-commit

Clone the demo repository

```bash
git clone https://github.com/klieret/python-pre-commit-demo-tutorial.git
cd python-pre-commit-demo-tutorial.git
```

If you haven't done already, install the `pre-commit` package:

```bash
pip3 install pre-commit
```

Let's take a look at the `pre-commit` configuration from the repository:

```bash
cat .pre-commit-config.yaml
```

Let's install these hooks:

```bash
pre-commit install
```

Now let's open the `test.py` file in your favorite editor.

Try one of the following and then try to commit (`git commit -a`):

1. Replace `return a + b` with `return None` (`mypy` will complain!)
2. Remove spaces between `+` (`black` will automatically reformat the file and add the spaces back)
3. Change `the` to `teh` in the docstring (`codespell` will flag it as a spelling mistake)
4. Import `math` (`flake8` will complain about an unused iport)

If you ever get stuck, run `git stash` ("stashes" away your changes).
