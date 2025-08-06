import pytest
from src.evaluator import Evaluator
from src.decision_rules import DecisionRules
from src.contract import Contract

@pytest.fixture
def decision_rules():
    return DecisionRules(
        rules = [
            {"reason": "Urgent", "days_to_expiry": 3},
            {"reason": "Upcoming", "days_to_expiry": 14}
        ],
        priority = ["Urgent", "Upcoming"]
    )

def test_new_notification(decision_rules):
    evaluator = Evaluator()
    contract = Contract({"id": 1, "days_to_expiry": 2})
    notification_log = {}
    is_notify, reason = evaluator.evaluate_contract(contract, decision_rules, notification_log)
    assert is_notify is True
    assert reason == "Urgent"

def test_no_duplicate_notification(decision_rules):
    evaluator = Evaluator()
    contract = Contract({"id": 1, "days_to_expiry": 2})
    notification_log = {"1": {"notified_on": "2025-07-20", "reason": "Urgent"}}
    is_notify, reason = evaluator.evaluate_contract(contract, decision_rules, notification_log)
    assert is_notify is False
    assert reason == "Already Notified"

def test_escalate_notification(decision_rules):
    evaluator = Evaluator()
    contract = Contract({"id": 2, "days_to_expiry": 2})
    notification_log = {"2": {"notified_on": "2025-07-20", "reason": "Upcoming"}}
    is_notify, reason = evaluator.evaluate_contract(contract, decision_rules, notification_log)
    assert is_notify is True
    assert reason == "Urgent"

    