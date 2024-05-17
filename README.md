# class-implements

For developers coming from statically typed object oriented programming languages, you may be familiar with the concept of the `implements` keyword...

```typescript
interface Duck {
  quack(): void;
}

class Goose implements Duck {
  quack() {
    // Implementation details...
  }
}
```

... and notice Python does not have this feature in its syntax. Luckily, this feature can be implemented into Python without hacking the keyword into the interpreter.

```python
from abc import abstractmethod
from typing import Protocol

from class_implements import interface


class Quackable(Protocol):
    @abstractmethod
    def quack(self):
        """Documentation string."""


class Walkable(Protocol):
    @abstractmethod
    def walk(self):
        """Documentation string."""


# This is the syntax you should use when creating intersection types.
class Duck(Quackable, Walkable, Protocol):
    pass


# Type safe.
@interface(Duck)
class Goose:
    def quack(self):
        pass

    def walk(self):
        pass


# Your static type checker reports an error.
@interface(Duck)
class Human:
    def walk(self):
        pass
```

Additionally, this is not limited to just class declarations

```python
IDuck = interface(Duck)
goose = Goose()
human = Human()

IDuck >> goose
IDuck >> human  # Type checker error.

# Alternatively, use a method based syntax
IDuck.check(goose)
IDuck.check(human)  # Type checker error
```

All while having zero cost at runtime by tricking your respective static type checker into doing the work at build time instead.

For runtime type checking, either [Beartype](https://github.com/beartype/beartype) or [Typical](https://github.com/seandstewart/typical) are recommended for this purpose. It is outside this utility library's scope to implement fast, boilerplate free runtime type checking.
