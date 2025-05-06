
from flask_fluence import Component, component

__all__ = []


@component
class HelloWorld(Component):
    template = """
    <div class="mx-auto mt-8 max-w-2xl">
        <div class="border rounded p-3">
            Hello World!
        </div>
    </div>
    """


@component
class Hello(Component):
    name = "Monde"
    template = """
    <div class="mx-auto mt-8 max-w-2xl">
        <div class="border rounded p-3">
            Hello {{ this.name }}!
        </div>
    </div>
    """


@component
class Hello2(Component):
    name = "Mundo"

    def render(self, **kwargs):
        result = f"""
            <div class="mx-auto mt-8 max-w-2xl">
                <div class="border rounded p-3">
                    Hello {self.name}!
                </div>
            </div>
        """
        return result
