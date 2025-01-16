from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        opening_tag = f"<{self.tag}{self.props_to_html()}>" if self.tag is not None else ""
        closing_tag = f"</{self.tag}>" if self.tag is not None else ""
        return f"{opening_tag}{self.value}{closing_tag}"