import unittest

from scripts.validate_repository import validate


class RepositoryValidationTest(unittest.TestCase):
    def test_repository_validation_passes(self):
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
