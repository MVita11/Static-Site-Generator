import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter, extract_markdown_images
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
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")  
        
    def test_happy_path(self):
        node = TextNode("This is a `code` word", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            split_node,
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]             
        )
    
if __name__ == "__main__":
    unittest.main()