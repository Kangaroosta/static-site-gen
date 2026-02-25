import unittest

from htmlnode import *


class TestHTMLnode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLnode(props={"href": "https://www.boot.dev"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.boot.dev"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


if __name__ == "__main__":
    unittest.main()