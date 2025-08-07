import pytest
from src.decision_rules import DecisionRules
from src.contract import Contract

@pytest.fixture
def rules_config():
    return {
        "rules": [
            {"reason": "Urgent", "days_to_expiry": 3},
            {"reason": "High-Cost", "days_to_expiry": 30, "min_annual_cost": 10000},
            {"reason": "Upcoming", "days_to_expiry": 14}
        ],
        "priority": ["Urgent", "High-Cost", "Upcoming"]
    }

def test_priority(rules_config):
    rules_config["rules"] = [
        {"reason": "Upcoming", "days_to_expiry": 14},
        {"reason": "Urgent", "days_to_expiry": 3},
        {"reason": "High-Cost", "days_to_expiry": 30, "min_annual_cost": 10000},
        {"reason": "Critical", "days_to_expiry": 1},
        {"reason": "Medium-Cost", "days_to_expiry": 30, "min_annual_cost": 5000},
        {"reason": "Low-Cost", "days_to_expiry": 30, "min_annual_cost": 1000},
        {"reason": "Long-Term Expiry", "days_to_expiry": 60},
        {"reason": "Very High-Cost", "days_to_expiry": 60, "min_annual_cost": 20000}
    ]
    rules_config["priority"] = [
        "Critical",
        "Urgent",
        "Very High-Cost",
        "High-Cost",
        "Medium-Cost",
        "Low-Cost",
        "Upcoming",
        "Long-Term Expiry"
    ]

    rules = DecisionRules(rules_config["rules"], rules_config["priority"])
  
    for i in range(len(rules.priority)):
        if i < len(rules.rules):
            assert rules.priority[i] == rules.rules[i]["reason"]

def test_rule_match_high_cost(rules_config):
    rules = DecisionRules(rules_config["rules"], rules_config["priority"])
    contract = Contract({
        "id": 1,
        "annual_cost_eur": 15000,
        "days_to_expiry": 10
    })
    reason = rules.find_top_reason(contract)
    assert reason == "High-Cost"

def test_rule_match_urgent(rules_config):
    rules = DecisionRules(rules_config["rules"], rules_config["priority"])
    contract = Contract({
        "id": 2,
        "annual_cost_eur": 12000,
        "days_to_expiry": 2
    })
    reason = rules.find_top_reason(contract)
    assert reason == "Urgent"

def test_no_match_rule(rules_config):
    rules = DecisionRules(rules_config["rules"], rules_config["priority"])
    contract = Contract({
        "id": 3,
        "annual_cost_eur": 5000,
        "days_to_expiry": 40
    })
    reason = rules.find_top_reason(contract)
    assert reason == "No Match"