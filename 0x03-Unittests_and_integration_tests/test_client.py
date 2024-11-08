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

    def test_public_repos_url(self):
        """Test that GithubOrgClient._public_repos_url returns the
        expected URL"""
        # Define a mock payload for the `org` property
        expected_repos_url = "https://api.github.com/orgs/test_org/repos"
        mock_payload = {"repos_url": expected_repos_url}
        # Use patch as a context manager to mock `org` property
        with patch.object(GithubOrgClient, 'org', return_value=mock_payload):
            # Instantiate GithubOrgClient and access
            client = GithubOrgClient("test_org")
            result = client._public_repos_url
            # Assert the _public_repos_url returns the repos_url
            self.assertEqual(result, expected_repos_url)


if __name__ == "__main__":
    unittest.main()
