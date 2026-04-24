import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("h1", "click me", None, {"href": "https://google.com"})
        node.props_to_html()
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')
    
    def test_init_defaults(self):
        node = HTMLNode("h1", "click me")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_repr_(self):
        node = HTMLNode("h1", "hello", None, None)
        self.assertEqual(repr(node), "HTMLNode(h1, hello, children: None, None)")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
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
        
if __name__ == "__main__":
    unittest.main()
