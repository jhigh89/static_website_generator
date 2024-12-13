from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode

def main():
    test_textnode = TextNode("It's me, the text node!",TextType.TEXT)
    test_htmlnode = HTMLNode(props={
    "href": "https://www.google.com", 
    "target": "_blank",
    })

if __name__ == "__main__":
    main()