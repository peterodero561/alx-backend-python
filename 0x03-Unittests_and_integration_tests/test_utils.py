#!/usr/bin/env python3
'''Understanding knowledge of tests'''
import unittest
from unittest.mock import patch, Mock
from typing import Any, Mapping, Sequence, Tuple, Dict
from utils import access_nested_map, get_json
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


class TestGetJson(unittest.TestCase):
    @patch('utils.requests.get')
    def test_get_json(self, mock_get) -> None:
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
        
        for test_url, test_payload in test_cases:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            
            # Call get_json and check results
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            
            # Verify that requests.get was called once with the test_url
            mock_get.assert_called_once_with(test_url)
            
            # Reset the mock for the next iteration
            mock_get.reset_mock()
