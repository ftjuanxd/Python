import reflex as rx 

from ..template import template

@rx.page(route="/Page2")
@template
def index() -> rx.Component:
    return rx.vstack(
        rx.text("PAgina 2"),
    )