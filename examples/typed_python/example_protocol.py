import typing
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
