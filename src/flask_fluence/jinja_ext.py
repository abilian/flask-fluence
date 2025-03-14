from jinja2_simple_tags import ContainerTag

from flask_fluence import render_component
from flask_fluence.component import get_component


class ComponentTag(ContainerTag):
    tags = {"component"}  # noqa: RUF012

    def render(self, component_name, **kwargs):  # noqa: PLR6301
        cls = get_component(component_name)
        obj = cls()
        return render_component(obj, **kwargs)
