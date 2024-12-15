from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from inline_markdown import text_to_textnodes

def main():
    test_textnode = TextNode("It's me, the text node!",TextType.TEXT)
    test_htmlnode = HTMLNode(props={
    "href": "https://www.google.com", 
    "target": "_blank",
    })

    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))

if __name__ == "__main__":
    main()