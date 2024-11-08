#!/usr/bin/env python3
'''Understanding knowledge of tests'''
import unittest
from typing import Any, Mapping, Sequence, Tuple
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''Tests to access the nested map'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(
            self,
            nested_map: Mapping[str, Any],
            path: Sequence[str],
            expected: Any) -> None:
        '''Tests that the method returns what is supposed to'''
        self.assertEqual(access_nested_map(nested_map, path), expected)
