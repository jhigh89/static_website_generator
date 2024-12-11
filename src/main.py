from textnode import TextNode,TextType
from htmlnode import HTMLNode

def main():
    test_textnode = TextNode("It's me, the text node!",TextType.TEXT)
    test_htmlnode = HTMLNode(props={
    "href": "https://www.google.com", 
    "target": "_blank",
    })

    print(test_htmlnode.props_to_html())
    print(test_htmlnode)

if __name__ == "__main__":
    main()