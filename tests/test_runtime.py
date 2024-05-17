from abc import abstractmethod
from typing import Protocol, runtime_checkable

from src.class_implements import interface


def test_decorator():
    @runtime_checkable
    class Speakable(Protocol):
        @abstractmethod
        def speak(self):
            """Documentation string."""

    @runtime_checkable
    class Walkable(Protocol):
        @abstractmethod
        def walk(self):
            """Documentation string."""

    @runtime_checkable
    class Animal(Speakable, Walkable, Protocol):
        pass

    @interface(Animal)
    class Goose:
        def speak(self):
            pass

        def walk(self):
            pass

    @interface(Animal).enforced_on
    class Duck:
        def speak(self):
            pass

        def walk(self):
            pass

    Goose()
    Duck()


def test_method():
    @runtime_checkable
    class Speakable(Protocol):
        @abstractmethod
        def speak(self):
            """Documentation string."""

    @runtime_checkable
    class Walkable(Protocol):
        @abstractmethod
        def walk(self):
            """Documentation string."""

    @runtime_checkable
    class Animal(Speakable, Walkable, Protocol):
        pass

    class Duck:
        def __init__(self):
            interface(Animal).typecheck(self)

        def speak(self):
            pass

        def walk(self):
            pass

    duck = interface(Animal) << Duck()
    interface(Animal).typecheck(duck)
    interface(Animal).typecheck(Duck())
