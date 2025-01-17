from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)


    def to_html(self):
        if self.tag is None or len(self.tag) <= 0:
            raise ValueError("Missing Tag")

        if self.children is None or len(self.children) <= 0:
            raise ValueError("Missing Children")
        return f"<{self.tag}{self.props_to_html()}>{"".join(map(lambda child: child.to_html(), self.children))}</{self.tag}>"