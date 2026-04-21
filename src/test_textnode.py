import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, url=None)
        node2 = TextNode("This is a text node", TextType.BOLD, url=None)
        self.assertEqual(node, node2)
    
    def test_not_eq_text(self):
        node = TextNode("hello", TextType.BOLD, url=None)
        node2 = TextNode("goodbye", TextType.BOLD, url=None)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_text_type(self):
        node = TextNode("hello", TextType.BOLD, url=None)
        node2 = TextNode("hello", TextType.ITALIC, url=None)
        self.assertNotEqual(node, node2)
        
    def test_not_eq_url(self):
        node = TextNode("hello", TextType.BOLD, url="https://boot.dev")
        node2 = TextNode("hello", TextType.BOLD, url="https://google.com")
        self.assertNotEqual(node, node2)
        
    def test_not_eq_url_none(self):
        node = TextNode("hello", TextType.BOLD, url=None)
        node2 = TextNode("hello", TextType.BOLD, url="https://google.com")
        self.assertNotEqual(node, node2)
    
        

if __name__ == "__main__":
    unittest.main()