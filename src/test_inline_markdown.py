import unittest
from textnode import TextNode, TextType
from inline_markdown import text_to_textnodes


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
        