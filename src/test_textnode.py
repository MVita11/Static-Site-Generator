import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, split_nodes_image
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
    
    def test_extract_markdown_images_single(self):
        matches = extract_markdown_images("This is an ![mountain](https://example.com/mountain.png)")
        self.assertListEqual([("mountain", "https://example.com/mountain.png")], matches)
        
    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "Here is ![one](https://example.com/1.png) and ![two](https://example.com/2.png)"
        )
        self.assertListEqual([
            ("one", "https://example.com/1.png"),
            ("two", "https://example.com/2.png"),
        ], matches)
    
    def test_extract_markdown_images_multiple_links(self):
        matches = extract_markdown_images(
            "Here is ![Boot.dev](https://www.boot.dev) and ![Google](https://www.google.com)"   
        )
        self.assertListEqual([
            ("Boot.dev", "https://www.boot.dev"),
            ("Google", "https://www.google.com"),
            
        ], matches)
        
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )
        
if __name__ == "__main__":
    unittest.main()