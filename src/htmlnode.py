class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
   
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return None
        
        string = ""
        for key, value in self.props.items():
            string += f' {key}="{value}"'
        return string
            
    def __repr__(self):
        return print(f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})")
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        
        props_html = ""
        if self.props:
            for prop, value in self.props.items():
                props_html += f' {prop}="{value}"'
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>" 
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode must have children") 
        
        return f"<{self.tag}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
        
        
 