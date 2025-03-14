# Copyright (c) 2021-2025, Abilian SAS

from __future__ import annotations

from .render import render_component
from .templates import get_template
from .component import Component, component

__all__ = ["get_template", "render_component", "Component", "component"]
