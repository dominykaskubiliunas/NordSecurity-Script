"""Contract Class - responsible for operations with a single contract data"""

from datetime import datetime
from common.constants import DATE_FORMAT, KEY_RENEWAL_DATE, KEY_PREVIOUS_NOTIFICATION, KEY_DAYS_TO_EXPIRY, KEY_ID

class Contract:
    def __init__(self, data: dict):
        self.data = data

    def add_days_to_expiry(self, current_date: str) -> int:
        """Calculates days to expiry for a single contract"""
        current_date = datetime.strptime(current_date, DATE_FORMAT)
        renewal_date = datetime.strptime(self.data[KEY_RENEWAL_DATE], DATE_FORMAT)
        self.data[KEY_DAYS_TO_EXPIRY] = (renewal_date - current_date).days

    def add_previous_notification(self, notification: str) -> None:
        """Adds previous notification reason"""
        self.data[KEY_PREVIOUS_NOTIFICATION] = notification

    def get_id_str(self) -> str:
        """Returns ID of the contract as a string"""
        return str(self.data[KEY_ID])


if __name__ == "__main__":
    pass