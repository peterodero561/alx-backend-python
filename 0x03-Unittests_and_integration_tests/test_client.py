import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class"""
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected: dict, mock_get_json) -> None:
        """Test that GithubOrgClient.org returns the correct value"""
        # Set up the mock return value
        mock_get_json.return_value = expected
        # Initialize the client and call the org method
        client = GithubOrgClient(org_name)
        result = client.org
        # Assert get_json is called once with the correct URL
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")
        # Assert the org method returns the expected value
        self.assertEqual(result, expected)
