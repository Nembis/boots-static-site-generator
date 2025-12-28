import unittest

from textnode import TextNode, TextType

class TextNodeTest(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Image Node", TextType.IMAGE, "http://image-link.com/v1")
        node2 = TextNode("Image Node", TextType.IMAGE, "http://image-link.com/v2")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("Text", TextType.TEXT)
        node2 = TextNode("Text", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()

