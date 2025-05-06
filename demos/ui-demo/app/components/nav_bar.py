from dataclasses import dataclass, field

from flask_fluence import Component, component

__all__ = []


@component
class NavBar(Component):

    @property
    def context(self):
        return NavBarContext(
            items=["Toto", "Tata", "Titi"],
        )


@dataclass
class NavBarContext:
    logo: str = "Logo"
    # logo_img: str = "https://example.com/logo.png"

    items: list = field(default_factory=list)
