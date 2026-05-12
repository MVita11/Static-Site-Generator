import unittest
from textnode import TextNode, TextType
from inline_markdown import text_to_textnodes, split_nodes_delimiter, split_nodes_image, split_nodes_link, extract_markdown_images, extract_markdown_links


class TestInlineMarkdown(unittest.TestCase):
    def test_plain_text(self):
        nodes = text_to_textnodes(("Hello World"))
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Hello World")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        
    def test_bold_only(self):
        nodes = text_to_textnodes("**Hello World**")
        print(nodes)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Hello World")
        self.assertEqual(nodes[0].text_type, TextType.BOLD)
        
    def test_eq_mixed_inline(self):
        nodes = text_to_textnodes(("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))
        self.assertEqual(nodes,
                        [
                            TextNode("This is ", TextType.TEXT),
                            TextNode("text", TextType.BOLD),
                            TextNode(" with an ", TextType.TEXT),
                            TextNode("italic", TextType.ITALIC),
                            TextNode(" word and a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" and an ", TextType.TEXT),
                            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                            TextNode(" and a ", TextType.TEXT),
                            TextNode("link", TextType.LINK, "https://boot.dev"),
                            
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
       
    def test_one_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )    
        new_nodes = split_nodes_image([node])
        self.assertEqual([
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ],
        new_nodes,
    )
    
    def test_one_link(self):
        node = TextNode(
            "[Boot.dev](https://boot.dev)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),        
        ],
        new_nodes,
    )
        
    def test_split_image_only(self):
        node = TextNode(
        "![logo](https://example.com/logo.png)",
        TextType.TEXT,
    )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("logo", TextType.IMAGE, "https://example.com/logo.png"),
        ],
        new_nodes,
    )
    
    def test_split_links_multiple(self):
        node = TextNode(
        "Visit [Boot.dev](https://boot.dev) and [Google](https://www.google.com)",
        TextType.TEXT,
    )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
        [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://www.google.com"),
        ],
        new_nodes,
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
       
    def test_one_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )    
        new_nodes = split_nodes_image([node])
        self.assertEqual([
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ],
        new_nodes,
    )
    
    def test_one_link(self):
        node = TextNode(
            "[Boot.dev](https://boot.dev)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),        
        ],
        new_nodes,
    )
        
    def test_split_image_only(self):
        node = TextNode(
        "![logo](https://example.com/logo.png)",
        TextType.TEXT,
    )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("logo", TextType.IMAGE, "https://example.com/logo.png"),
        ],
        new_nodes,
    )
    
    def test_split_links_multiple(self):
        node = TextNode(
        "Visit [Boot.dev](https://boot.dev) and [Google](https://www.google.com)",
        TextType.TEXT,
    )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
        [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://www.google.com"),
        ],
        new_nodes,
    )
        
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