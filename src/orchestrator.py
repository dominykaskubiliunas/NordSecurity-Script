"""
Orchestrator class manages the contract notification workflow by coordinating data loading, rule evaluation and notification tracking.
"""

from src.decision_rules import DecisionRules
from src.contract import Contract
from src.contract_notification_decision import evaluate_contract
from src.serializer import Serializer
from utils.utils import load_json, save_json
from common.constants import *


class Orchestrator():
    def __init__(self, config_input_path: str, contracts_input_path: str):
        self.config = load_json(config_input_path)
        self.contracts = load_json(contracts_input_path)
        self.decision_rules = DecisionRules(rules = self.config[KEY_RULES], priority = self.config[KEY_PRIORITY])
        self.serializer = Serializer()
        self.current_notifications = []

    def add_current_datetime_str(self, current_datetime_str: str) -> None:
        """Adds current datetime to the class"""
        self.current_datetime = current_datetime_str

    def load_notifications(self, notification_file_path: str = NOTIFICATION_LOG_FILE_PATH) -> None:
        """Loads the most recent notification log"""
        self.notifications = load_json(notification_file_path)

    def clear_current_notifications(self) -> None:
        """Clear current notifications"""
        self.current_notifications = []

    def check_contracts(self) -> None:
        """Goes through each contract, updates notifications log and prints out new notifications"""
        for contract in self.contracts:
            current_contract = Contract(data = contract)
            current_contract.compute_days_to_expiry(current_date=self.current_datetime)
            
            is_notified, reason = evaluate_contract(contract=current_contract, decision_rules=self.decision_rules, notification_log=self.notifications)
            
            if is_notified:
                self.notifications[current_contract.get_id_str()] = self.serializer.notification_log_entry(notified_on=self.current_datetime, reason=reason)
                self.current_notifications.append(self.serializer.notification_output(contract=current_contract, reason=reason))
        
        print(self.current_notifications)
        save_json(self.notifications, file_path=NOTIFICATION_LOG_FILE_PATH)

    
if __name__ == "__main__":
    pass
