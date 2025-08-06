"""
Orchestrator class manages the contract notification workflow by coordinating data loading, rule evaluation and notification tracking.
"""

from src.decision_rules import DecisionRules
from src.contract import Contract
from src.evaluator import Evaluator
from utils.utils import load_json
from common.constants import KEY_NOTIFIED_ON, KEY_REASON, KEY_ID, KEY_RULES, KEY_PRIORITY, NOTIFICATION_LOG_FILE_PATH


class Orchestrator():
    def __init__(self, config_input_path: str, contracts_input_path: str):
        self.config = load_json(config_input_path)
        self.contracts = load_json(contracts_input_path)
        self.decision_rules = DecisionRules(rules = self.config[KEY_RULES], priority = self.config[KEY_PRIORITY])
        self.evaluator = Evaluator()
        self.current_notifications = []

    def add_current_datetime_str(self, current_datetime_str: str) -> None:
        """Adds current datetime to the class"""
        self.current_datetime = current_datetime_str

    def load_notifications_log(self, notification_file_path: str = NOTIFICATION_LOG_FILE_PATH) -> None:
        """Loads the most recent notification log"""
        self.notifications = load_json(notification_file_path)

    def check_contracts(self) -> dict[str, dict[str, str]]:
        """Goes through each contract and updates to notifications. Prints out new updates for the notification log"""
        for contract in self.contracts:
            current_contract = Contract(data = contract)
            current_contract.add_days_to_expiry(current_date=self.current_datetime)
            
            is_notified, reason = self.evaluator.evaluate_contract(contract=current_contract, decision_rules=self.decision_rules, notification_log=self.notifications)
            
            if is_notified:
                notification = {
                    KEY_NOTIFIED_ON: self.current_datetime,
                    KEY_REASON: reason
                }
                contract_id_str = current_contract.get_id_str()
                self.notifications[contract_id_str] = notification
                self.current_notifications.append({
                    **notification,
                    KEY_ID: contract_id_str
                })
        
        print(self.current_notifications)
        return self.notifications

    
if __name__ == "__main__":
    pass
