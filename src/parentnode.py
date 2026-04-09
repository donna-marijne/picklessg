from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children=[], props={}):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent nodes must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("parent nodes must have one or more children")
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
