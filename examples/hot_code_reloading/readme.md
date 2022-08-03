# Hot code reloading!

Create a file `library.py` with the content `a = 4` or clone this repository
and change to this directory.

Open a Jupyter notebook or ipython console

```bash
jupyter notebook
# or
ipython3
```

Enable autoreloading: Add the following to your console/notebook:

```python
%load_ext autoreload
%autoreload 2
```

Now import the `library` module

```python
import library
library.a  # <-- should print 4
```

Now change the content of `library`, e.g., set `a = 15`.
Check that the changes were automatically applied:

```python
library.a  # <-- should print 15
```
