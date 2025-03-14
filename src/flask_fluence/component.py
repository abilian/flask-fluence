from collections.abc import Callable


class Component:
    template: str | None = None
    render: Callable | None = None


def component(cls: type) -> type:
    return cls
