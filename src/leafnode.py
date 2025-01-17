from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props, children=None)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None.")
        
        if self.tag == "img":  # Special handling for 'img' tags
            return f"<{self.tag}{self.props_to_html()}>"
        
        if self.value.strip() == "" and self.tag:  # Only raise if tag exists
            raise ValueError("LeafNode value cannot be empty.")

        opening_tag = f"<{self.tag}{self.props_to_html()}>" if self.tag else ""
        closing_tag= f"</{self.tag}>" if self.tag else ""
        return f"{opening_tag}{self.value}{closing_tag}"