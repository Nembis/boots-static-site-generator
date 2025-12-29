from textnode import TextNode, TextType
from leafnode import LeafNode

def main():
    example = TextNode("This is some anchor text", TextType.LINK, "https://boot.dev")
    print(example)


if __name__ == "__main__":
    main()

