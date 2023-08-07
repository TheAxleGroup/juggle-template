from wagtail.core.blocks import StructBlock, CharBlock


class BaseBlock(StructBlock):
    block_id = CharBlock(required=False)

    class Meta:
        abstract = True
