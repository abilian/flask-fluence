from __future__ import annotations

from typing import TYPE_CHECKING

from flask_super.registry import Registry

if TYPE_CHECKING:
    from collections.abc import Callable


class Component:
    template: str | None = None
    render: Callable | None = None


component_registry = Registry()


def component(cls: type) -> type:
    return component_registry.register(cls)


def get_component(name) -> type[Component]:
    lookup_result = component_registry.lookup(name)
    if not lookup_result:
        msg = f"Component {name} not found"
        raise ValueError(msg)
    if len(lookup_result) > 1:
        msg = f"Multiple components found for {name}"
        raise ValueError(msg)
    return lookup_result[0]
