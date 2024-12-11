import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
	def test_eq_props(self):
		node = HTMLNode(props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		node2 = HTMLNode(props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		self.assertEqual(node.props,node2.props)

	def test_neq_props(self):
		node = HTMLNode(props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		node2 = HTMLNode(props={
            "href": "https://www.bing.com", 
            "target": "_blank",
        })
		self.assertNotEqual(node.props,node2.props)

	def test_eq_tag(self):
		node = HTMLNode(tag="h1",props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		node2 = HTMLNode(tag="h1",props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		self.assertEqual(node.tag,node2.tag)

	def test_neq_tag(self):
		node = HTMLNode(tag="h1",props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		node2 = HTMLNode(tag="p",props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		self.assertNotEqual(node.tag,node2.tag)

	def test_eq_value(self):
		node = HTMLNode(tag="h1",value="I'm ready!",props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		node2 = HTMLNode(tag="h1",value="I'm ready!",props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		self.assertEqual(node.value,node2.value)

	def test_neq_value(self):
		node = HTMLNode(tag="h1",value="I am not ready!",props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		node2 = HTMLNode(tag="h1",value="I'm ready!",props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		self.assertNotEqual(node.value,node2.value)

	def test_repr(self):
		node = HTMLNode(props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
		self.assertEqual(
            "HTMLNode(None, None, None, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node)
        )

if __name__ == "__main__":
	unittest.main()
