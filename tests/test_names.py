# Copyright (c) 2021-2025, Abilian SAS

from __future__ import annotations

from flask_fluence.lib.names import fqdn, to_kebab_case, to_snake_case


def test_to_kebab_case() -> None:
    assert to_kebab_case("FooBar") == "foo-bar"


def test_to_snake_case() -> None:
    assert to_snake_case("FooBar") == "foo_bar"


def test_fqdn() -> None:
    class Foo:
        pass

    assert fqdn(Foo) == "tests.test_names.Foo"
