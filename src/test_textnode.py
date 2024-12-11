import unittest

from textnode import TextNode,TextType

class TestTextNode(unittest.TestCase):
	def test_eq_bold(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node,node2)

	def test_neq_text(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node again", TextType.BOLD)
		self.assertNotEqual(node,node2)

	def test_eq_italic(self):
		node = TextNode("should", TextType.ITALIC)
		node2 = TextNode("should", TextType.ITALIC)
		self.assertEqual(node,node2)

	def test_neq_text_type(self):
		node = TextNode("This is a text node", TextType.LINK)
		node2 = TextNode("This is a text node", TextType.IMAGE)
		self.assertNotEqual(node,node2)

	def test_eq_link(self):
		node = TextNode("This is a text node", TextType.LINK)
		node2 = TextNode("This is a text node", TextType.LINK)
		self.assertEqual(node,node2)

	def test_url_property_none(self):
		node = TextNode("This is a text node", TextType.BOLD)
		self.assertIsNone(node.url)

	def test_repr(self):
		node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
		self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
	unittest.main()
