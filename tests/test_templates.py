from flask import Flask

from flask_fluence.templates import get_template


def test_get_template_embedded() -> None:
    class Hello:
        template = "Hello world!"

    obj = Hello()

    app = Flask(__name__)
    with app.app_context():
        template = get_template(obj)
        assert template


def test_get_template_external() -> None:
    from tests.components.hello import Hello

    obj = Hello()

    app = Flask(__name__)
    with app.app_context():
        template = get_template(obj)
        assert template
