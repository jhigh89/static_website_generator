from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode

def main():
    test_textnode = TextNode("It's me, the text node!",TextType.TEXT)
    test_htmlnode = HTMLNode(props={
    "href": "https://www.google.com", 
    "target": "_blank",
    })
    
    test_parentnode = ParentNode("div",[test_textnode,test_htmlnode])
    print(test_parentnode.to_html())
    print(test_parentnode)

if __name__ == "__main__":
    main()