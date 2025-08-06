"""
Evaluator class determines if a contract should be notified.
Even though this class is not necessary, it is implemented for future scalability
"""

from src.decision_rules import DecisionRules
from src.contract import Contract
from common.constants import KEY_ID, KEY_REASON, NO_MATCH, KEY_PREVIOUS_NOTIFICATION, ALREADY_NOTIFIED

class Evaluator():
    def __init__(self):
        pass
    
    def notification_check(self, notification_log: dict, contract: Contract) -> bool:
        """Checks, if this contract was notified previously"""
        
        if not notification_log or not str(contract.data[KEY_ID]) in notification_log.keys():
            return False
        else: 
            contract.add_previous_notification(notification_log[str(contract.data[KEY_ID])][KEY_REASON])
            return True

    def evaluate_contract(self, contract: Contract, decision_rules: DecisionRules, notification_log: str) -> tuple[bool, str]:
        """Evaluates a single contract and decides if it should be notified"""
        
        top_reason = decision_rules.find_top_reason(contract=contract)
        
        if top_reason == NO_MATCH:
            return (False, NO_MATCH)
        
        notification_check = self.notification_check(notification_log=notification_log, contract=contract)
        
        if not notification_check:
            return (True, top_reason)
        else:
            if decision_rules.priority.index(contract.data[KEY_PREVIOUS_NOTIFICATION]) > decision_rules.priority.index(top_reason):
                return (True, top_reason)
            else:
                return (False, ALREADY_NOTIFIED)

    


if __name__ == "__main__":
    pass