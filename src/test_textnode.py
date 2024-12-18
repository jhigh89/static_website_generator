import unittest
from textnode import TextNode,TextType,text_node_to_html_node

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

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
	unittest.main()
