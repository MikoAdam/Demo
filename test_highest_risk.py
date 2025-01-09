import unittest
import os
from highest_risk import Asset, get_highest_risk_by_asset

class TestAsset(unittest.TestCase):
    def test_asset_highest_risk(self):
        """
        Check that an Asset object returns the correct highest risk level
        after adding multiple risks.
        """
        asset = Asset("TestAsset")
        asset.add_risk("Risk1", "Low")
        asset.add_risk("Risk2", "Medium")
        asset.add_risk("Risk3", "High")

        self.assertEqual(asset.get_highest_risk_level(), "High")

class TestGetHighestRiskByAsset(unittest.TestCase):
    def test_example_data(self):

        csv_data = """Asset,Risk,Risk Level
Asset1,Risk1,Medium
Asset2,Risk1,Low
Asset1,Risk3,High
Asset1,Risk4,Low
"""
        test_csv_path = "test_example_data.csv"
        with open(test_csv_path, "w", encoding="utf-8") as f:
            f.write(csv_data)

        result = get_highest_risk_by_asset(test_csv_path)

        os.remove(test_csv_path)

        self.assertIn("Asset1", result)
        self.assertIn("Asset2", result)
        self.assertEqual(result["Asset1"], "High")
        self.assertEqual(result["Asset2"], "Low")

if __name__ == '__main__':
    unittest.main()
