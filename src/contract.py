"""Contract Class - responsible for operations with a single contract data"""

from datetime import datetime
from common.constants import *
from typing import Optional

class Contract:
    def __init__(self, data: dict):
        self._data = data

    def compute_days_to_expiry(self, current_date: str) -> int:
        """Calculates days to expiry for a single contract"""
        current_date = datetime.strptime(current_date, DATE_FORMAT)
        renewal_date = datetime.strptime(self._data[KEY_RENEWAL_DATE], DATE_FORMAT)
        self._data[KEY_DAYS_TO_EXPIRY] = (renewal_date - current_date).days

    def set_previous_notification(self, notification: str) -> None:
        """Adds previous notification reason"""
        self._data[KEY_PREVIOUS_NOTIFICATION] = notification
   
    def get_id(self) -> int:
        return self._data[KEY_ID] 

    def get_id_str(self) -> str:
        return str(self.get_id())

    def get_software_name(self) -> str:
        return self._data[KEY_SOFTWARE_NAME]

    def get_owner(self) -> str:
        return self._data[KEY_OWNER]

    def get_organization(self) -> str:
        return self._data[KEY_ORGANIZATION]

    def get_annual_cost(self) -> float:
        return self._data[KEY_ANNUAL_COST]

    def get_renewal_date(self) -> str:
        return self._data[KEY_RENEWAL_DATE]
    
    def get_days_to_expiry(self) -> int:
        return self._data[KEY_DAYS_TO_EXPIRY]

    def get_previous_notification(self) -> Optional[str]:
        return self._data.get(KEY_PREVIOUS_NOTIFICATION)