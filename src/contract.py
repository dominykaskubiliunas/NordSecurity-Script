import json
from datetime import datetime

class Contract:
    def __init__(self, data: dict):
        self.data = data
        self.id = data["id"]
        self.renewal_date = datetime.strptime(data["renewal_date"], "%Y-%m-%d")
        self.annual_cost_eur = data["annual_cost_eur"]

    def add_days_to_expiry(self, current_date: datetime) -> int:
        """
        Calculates days to expiry for a single contract
        """
        self.days_to_expiry = (self.renewal_date - current_date).days

    def get_days_to_expiry(self, current_date: datetime) -> int:
        """
        Returns days to expiry 
        """
        return self.days_to_expiry

    def get_id(self) -> int:
        """
        Returns ID of the contract
        """
        return self.id


if __name__ == "__main__":
    example_contract = {
        "id": 1,
        "software_name": "GitHub Enterprise Cloud",
        "owner": "Ava Chen",
        "organization": "Nord Security",
        "annual_cost_eur": 25200.00,
        "renewal_date": "2025-08-02"
    }
    contract = Contract(data = example_contract)
