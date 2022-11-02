from __future__ import annotations


def f(x: int) -> list[int]:
    return list(range(x))


def g(x: str | int) -> str:
    if isinstance(x, str):
        return x.lower()
    else:
        return x
