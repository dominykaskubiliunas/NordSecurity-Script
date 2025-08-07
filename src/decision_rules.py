"""
Decision Rules class is responsible for managing and applying rules from config.json
"""
from src.contract import Contract
from common.constants import KEY_REASON, KEY_DAYS_TO_EXPIRY, KEY_MIN_ANNUAL_COST, NO_MATCH

class DecisionRules:
    def __init__(self, rules: list[dict], priority: list[str]):    
        self.priority = priority
        self.rules = self._sort_rules_by_priority(rules)
    
    def _sort_rules_by_priority(self, rules: list[dict]) -> list[dict]:
        """Sort rules according to the priority list."""
        
        def get_priority_index(rule):
            rule_type = rule.get(KEY_REASON, '')
            try:
                return self.priority.index(rule_type)
            except ValueError:
                return len(self.priority)
        
        return sorted(rules, key=get_priority_index)
    
    def _rule_matches(self, rule: dict, contract: Contract) -> bool:
        """Check if ALL conditions in a rule are satisfied by the contract."""
        
        try:
            if contract.get_days_to_expiry() > rule.get(KEY_DAYS_TO_EXPIRY, float('inf')):
                return False
            
            if KEY_MIN_ANNUAL_COST in rule:
                annual_cost = contract.get_annual_cost()
                if annual_cost < rule[KEY_MIN_ANNUAL_COST]:
                    return False
            
            return True
        
        except KeyError:
            print("Contract doesn't have needed features to evaluate it according to the decision rules")
            return False


    def find_top_reason(self, contract: Contract) -> str:
        """Find the first applicable rule based on priority order."""
        
        for rule in self.rules:
            if self._rule_matches(rule, contract):
                return rule[KEY_REASON]
        
        return NO_MATCH

if __name__ == "__main__":
    pass
