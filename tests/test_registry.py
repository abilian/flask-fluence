from flask_fluence import component
from flask_fluence.component import get_component


def test_registry():
    @component
    class Hello:
        pass

    cls = get_component(Hello)
    assert cls is Hello
