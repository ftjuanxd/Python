import reflex as rx 

from ..template import template

@rx.page(route="/")
@template
def index() -> rx.Component:
    return rx.vstack(
        rx.text("Hi World Sad?"),
    )