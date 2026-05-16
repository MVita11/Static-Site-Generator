import unittest
from markdown_block import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
            
        def test_headings(self):
            self.assertEqual(block_to_block_type("# Hello"), BlockType.HEADING)
            self.assertEqual(block_to_block_type("## Hello"), BlockType.HEADING)
            self.assertEqual(block_to_block_type("### Hello"), BlockType.HEADING)
            self.assertEqual(block_to_block_type("#### Hello"), BlockType.HEADING)
            self.assertEqual(block_to_block_type("##### Hello"), BlockType.HEADING)
            self.assertEqual(block_to_block_type("###### Hello"), BlockType.HEADING)

        def test_heading_no_space(Self):
            self.assertEqual(block_to_block_type("#Hello"), BlockType.PARAGRAPH)