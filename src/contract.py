"""Contract Class - responsible for operations with a single contract data"""

from datetime import datetime
from common.constants import *
from typing import Optional

class Contract:
    def __init__(self, data: dict):
        self.data = data

    def compute_days_to_expiry(self, current_date: str) -> int:
        """Calculates days to expiry for a single contract"""
        current_date = datetime.strptime(current_date, DATE_FORMAT)
        renewal_date = datetime.strptime(self.data[KEY_RENEWAL_DATE], DATE_FORMAT)
        self.data[KEY_DAYS_TO_EXPIRY] = (renewal_date - current_date).days

    def set_previous_notification(self, notification: str) -> None:
        """Adds previous notification reason"""
        self.data[KEY_PREVIOUS_NOTIFICATION] = notification
   
    def get_id_str(self) -> str:
        """Gets ID of the object as a string"""
        return str(self.data[KEY_ID] )

    def get_annual_cost(self) -> float:
        """Gets annual cost of the object"""
        return self.data[KEY_ANNUAL_COST]

    def get_days_to_expiry(self) -> int:
        """Gets days to expiry of the object"""
        return self.data[KEY_DAYS_TO_EXPIRY]

    def get_previous_notification(self) -> Optional[str]:
        """Gets previous notifications"""
        return self.data.get(KEY_PREVIOUS_NOTIFICATION)