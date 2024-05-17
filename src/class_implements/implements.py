from typing import Protocol


class Implements[Interface: Protocol]:
    def __init__(self, interface: type[Interface], /):
        pass

    def __call__(self, class_definition: type[Interface]):
        return class_definition

    def on(self, class_definition: type[Interface]):
        return class_definition


class Interface[Interface: Protocol]:
    """
    Hint the type checker that the class must implement the interface of the provided
    protocol.

    A side effect of this is that the type of your class will be widened to that of the
    protocol's. If this is not ideal, then you may want to use the `typecheck` method
    instead.
    """

    runtime: bool = True
    __interface: type[Interface]

    def __init__(self, interface: type[Interface], /, *, runtime: bool = __debug__):
        """
        The protocol that this class must match its interface with.
        """
        self.runtime = runtime
        self.__interface = interface

    def __call__(self, class_definition: type[Interface]):
        """
        Type check the class to the protocol
        """
        return class_definition

    def __lshift__(self, class_instance: Interface) -> Interface:
        """
        Widen the type of the given object to the type of the protocol.

        Note that this does not do anything at runtime, and is merely a hint for type
        checkers to act upon. For runtime behavior, see `debug_check`
        """
        return class_instance

    def enforced_on(self, class_definition: type[Interface]):
        """
        Type check the class to the protocol, enforcing it at runtime regardless if the
        runtime flag is set to true or not.
        """
        assert issubclass(class_definition, self.__interface)
        return class_definition

    def implemented_by(self, class_definition: type[Interface]):
        return class_definition

    def off[This](self, class_definition: This) -> This:
        """
        Hint the type checker that it should no longer enforce that the class should
        implement the interface of the provided protocol. THIS SHOULD NOT BE USED AS A
        PERMANENT SOLUTION.
        """
        return class_definition

    def typecheck(self, class_instance: Interface) -> Interface:
        """
        Hint the type checker that the passed object must implement the interface of the
        provided protocol.
        """
        if self.runtime:
            assert isinstance(class_instance, self.__interface)
        return class_instance


implements = Implements
interface = Interface


__all__ = ("implements", "interface")
