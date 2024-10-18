import reflex as rx

from typing import Callable

from .components.navbar import navbar_icons as nvi

from .components.footer import footer_newsletter as ft

#from .components.switch import dark_mode_toggle as dk


def template( page: Callable[[], rx.Component]) -> rx.Component:
    return rx.vstack(
        nvi(),
        rx.hstack(
            rx.text("Template"),
            rx.container(page())
        ),
        ft(),
        width="100%"
    )