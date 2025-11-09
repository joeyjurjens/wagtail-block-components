from wagtail import hooks

from . import blocks


@hooks.register("register_components")
def register_test_components():
    return [
        blocks.AccordionBlock,
        blocks.AccordionItemBlock,
    ]
