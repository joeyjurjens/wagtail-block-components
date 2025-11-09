"""
Register test components via Wagtail hooks.
"""

from wagtail import hooks

from . import blocks


@hooks.register("register_components")
def register_test_components():
    """Register test components"""
    return [
        blocks.AccordionBlock,
        blocks.AccordionItemBlock,
    ]
