class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        result = []
        for key, value in self.props.items():
            result.append(f'{key}="{value}"')
        return " " + " ".join(result)
    
    def __repr__(self):
        return f'HTMLnode{self.tag, self.value, self.children, self.props}'
    

class LeafNode(HTMLnode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value,children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        if self.props:
            return f'<{self.tag}{self.props}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode{self.tag, self.value, self.props}'