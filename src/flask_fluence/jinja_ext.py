from jinja2_simple_tags import ContainerTag

from .component import get_component
from .render import render_component


class ComponentTag(ContainerTag):
    tags = {"component"}  # noqa: RUF012

    def render(self, component_name, **kwargs):
        cls = get_component(component_name)
        obj = cls()
        return render_component(obj, **kwargs)
