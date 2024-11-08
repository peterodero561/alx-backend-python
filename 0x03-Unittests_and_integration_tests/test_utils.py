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
        '''Tests access_nested_map with nested_map and path'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping[str, Any],
            path: Sequence[str]) -> None:
        '''Test access_nested_map raises with invalid path'''
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")
