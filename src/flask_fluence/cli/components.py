from flask.cli import with_appcontext
from flask_super.cli import command

from flask_fluence.component import component_registry


@command(short_help="Show config")
@with_appcontext
def components() -> None:
    """Show registered components"""
    classes = component_registry.lookup("")
    for cls in classes:
        print(cls)
