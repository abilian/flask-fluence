from .templates import get_template


def render_component(obj, **kwargs):
    if render := getattr(obj, "render", None):
        return render(**kwargs)

    template = get_template(obj)
    return template.render(this=obj, **kwargs)
