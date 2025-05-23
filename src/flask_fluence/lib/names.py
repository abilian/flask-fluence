# Copyright (c) 2021-2025, Abilian SAS

from __future__ import annotations

import re


def fqdn(cls: type) -> str:
    return f"{cls.__module__}.{cls.__name__}"


def dense_fqdn(cls: type) -> str:
    path = fqdn(cls).split(".")
    for i in range(len(path) - 1):
        path[i] = path[i][0]
    return ".".join(path)


def to_snake_case(name: str) -> str:
    """Convert CamelCase to snake_case

    >>> to_snake_case("CamelCase")
    'camel_case'
    """
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def to_kebab_case(name: str) -> str:
    """Convert CamelCase to kebab-case

    >>> to_kebab_case("CamelCase")
    'camel-case'
    """
    return re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()
