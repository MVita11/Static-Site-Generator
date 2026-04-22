import unittest

from htmlnode import HTMLNode

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
        
if __name__ == "__main__":
    unittest.main()
