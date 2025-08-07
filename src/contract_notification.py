"""
Functions that cover all decision-making processes and other factors apart from rules in config.json
"""

from src.decision_rules import DecisionRules
from src.contract import Contract
from common.constants import KEY_REASON, NO_MATCH, ALREADY_NOTIFIED

def notification_check(notification_log: dict, contract: Contract) -> bool:
    """Checks, if this contract was notified previously"""
    
    if not notification_log or not contract.get_id_str() in notification_log.keys():
        return False
    else: 
        contract.set_previous_notification(notification_log[contract.get_id_str()][KEY_REASON])
        return True

def evaluate_contract(contract: Contract, decision_rules: DecisionRules, notification_log: str) -> tuple[bool, str]:
    """Evaluates a single contract and decides if it should be notified"""
    
    top_reason = decision_rules.find_top_reason(contract=contract)
    
    if top_reason == NO_MATCH:
        return (False, NO_MATCH)
    
    was_notified = notification_check(notification_log=notification_log, contract=contract)
    
    if not was_notified:
        return (True, top_reason)
    else:
        if decision_rules.priority.index(contract.get_previous_notification()) > decision_rules.priority.index(top_reason):
            return (True, top_reason)
        else:
            return (False, ALREADY_NOTIFIED)

    


if __name__ == "__main__":
    pass