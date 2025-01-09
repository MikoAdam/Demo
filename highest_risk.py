import csv
from natsort import natsorted

# Dictionary to be able to compare risks levels
RISK_PRIORITY = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

# I store assets as one data unit, as a class
class Asset:
    def __init__(self, name):
        self.name = name
        self.risks = {}

    # adding risk here: I assume that risk_name is uniq ID, thus, I overwrite the value is the same rosk_name comes twice
    def add_risk(self, risk_name, risk_level):
        self.risks[risk_name] = risk_level

    def get_highest_risk_level(self):

        # if empty return to prevent null pointer exception
        if not self.risks:
            return None

        risk_levels = list(self.risks.values())
        highest_risk = risk_levels[0]

        for level in risk_levels[1:]:
            if RISK_PRIORITY[level] > RISK_PRIORITY[highest_risk]:
                highest_risk = level
        
        return highest_risk

def get_highest_risk_by_asset(csv_file_path):
    assets_map = {}

    with open(csv_file_path, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            asset_name, risk_name, risk_level = row

            if asset_name not in assets_map:
                assets_map[asset_name] = Asset(asset_name)

            assets_map[asset_name].add_risk(risk_name, risk_level)

    highest_risk_dict = {}
    for asset_name, asset_obj in assets_map.items():
        highest_risk_dict[asset_name] = asset_obj.get_highest_risk_level()

    return highest_risk_dict

def main():

    csv_file_path = r"C:\Users\Adam Miko\Desktop\Demo\risks.csv"

    highest_risks = get_highest_risk_by_asset(csv_file_path)

    for asset_name, risk_level in natsorted(highest_risks.items()):
        print(f"{asset_name}: {risk_level}")

if __name__ == "__main__":
    main()
