from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag missing.")

        if not self.children:
            raise ValueError("Childrens Missing.")
        
        parent = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            child_html = child.to_html()
            parent += child_html
        
        parent += f"</{self.tag}>"

        return parent
