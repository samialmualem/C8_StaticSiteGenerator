import unittest

from htmlnode import *
from textnode import *

from main import text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_propsToHTML(self):
        node = HTMLNode() 
        self.assertEqual(node.props_to_html(), None)

    def test_propsToHTML2(self):
        node = HTMLNode('someTag', 'someValue', ['child1', 'child2'], {'prop1': 'value1', 'prop2': 'value2'})
        self.assertEqual(node.props_to_html(), " prop1=\"value1\" prop2=\"value2\"")

    def test_propsToHTML2(self):
        prop = {
                    "href": "https://www.google.com",
                    "target": "_blank",
                }
        node = HTMLNode('someTag', 'someValue', ['child1', 'child2'], prop)
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
 
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    # Test the text_node_to_html_node function
    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()