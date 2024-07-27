#!/usr/bin/env python3
""" Test utils.access_nested_map function
"""

import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Any

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ This class implements the test methods for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a", 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any], path: Tuple[str, ...], expected: Any) -> None:
        """Test the access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
