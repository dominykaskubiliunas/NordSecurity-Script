import pytest
from contract_notification_decision import evaluate_contract
from src.decision_rules import DecisionRules
from src.contract import Contract

@pytest.fixture
def decision_rules():
    return DecisionRules(
        rules = [
            {"reason": "Urgent", "days_to_expiry": 3},
            {"reason": "High-Cost", "days_to_expiry": 30, "min_annual_cost": 10000},
            {"reason": "Upcoming", "days_to_expiry": 14}
        ],
        priority = ["Urgent", "High-Cost", "Upcoming"]
    )

def test_new_notification_urgent(decision_rules):
    contract = Contract({"id": 1, "days_to_expiry": 2, "annual_cost_eur": 12000})
    notification_log = {}
    is_notify, reason = evaluate_contract(contract, decision_rules, notification_log)
    assert is_notify is True
    assert reason == "Urgent"

def test_no_duplicate_notification(decision_rules):
    contract = Contract({"id": 1, "days_to_expiry": 2, "annual_cost_eur": 12000})
    notification_log = {"1": {"notified_on": "2025-07-20", "reason": "Urgent"}}
    is_notify, reason = evaluate_contract(contract, decision_rules, notification_log)
    assert is_notify is False
    assert reason == "Already Notified"

def test_escalate_notification(decision_rules):
    contract = Contract({"id": 2, "days_to_expiry": 2, "annual_cost_eur": 12000})
    notification_log = {"2": {"notified_on": "2025-07-20", "reason": "Upcoming"}}
    is_notify, reason = evaluate_contract(contract, decision_rules, notification_log)
    assert is_notify is True
    assert reason == "Urgent"

def test_no_notification_outside_rule_window(decision_rules):
    contract = Contract({"id": 3, "days_to_expiry": 40, "annual_cost_eur": 5000})
    notification_log = {}
    is_notify, reason = evaluate_contract(contract, decision_rules, notification_log)
    assert is_notify is False
    assert reason == "No Match"

def test_highest_priority_rule_selected(decision_rules):
    contract = Contract({"id": 4, "days_to_expiry": 2, "annual_cost_eur": 15000})
    notification_log = {}
    is_notify, reason = evaluate_contract(contract, decision_rules, notification_log)
    assert is_notify is True
    assert reason == "Urgent"

def test_previously_notified_higher_priority(decision_rules):
    contract = Contract({"id": 5, "days_to_expiry": 10, "annual_cost_eur": 15000})
    notification_log = {"5": {"notified_on": "2025-07-20", "reason": "Urgent"}}
    is_notify, reason = evaluate_contract(contract, decision_rules, notification_log)
    assert is_notify is False
    assert reason == "Already Notified"

def test_high_cost_threshold_not_met(decision_rules):
    contract = Contract({"id": 6, "days_to_expiry": 10, "annual_cost_eur": 9999.99})
    notification_log = {}
    is_notify, reason = evaluate_contract(contract, decision_rules, notification_log)
    assert is_notify is True
    assert reason == "Upcoming"

def test_missing_fields_in_contract(decision_rules):
    contract = Contract({"id": 7})
    notification_log = {}
    is_notify, reason = evaluate_contract(contract, decision_rules, notification_log)
    assert is_notify is False
    assert reason == "No Match"
