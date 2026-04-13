from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props={}):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.tag is None:
            return self.value
        if self.value is None:
            # only img tags can be empty
            if self.tag != "img":
                raise ValueError("leaf nodes must have a value", self)
            return f"<{self.tag}{self.props_to_html()} />"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
