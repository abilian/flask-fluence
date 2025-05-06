from flask_fluence import component
from flask_fluence.component import get_component


def test_registry() -> None:
    @component
    class Hello:
        pass

    cls = get_component(Hello)
    assert cls is Hello
