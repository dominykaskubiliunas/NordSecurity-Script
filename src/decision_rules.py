from contract import Contract

class DecisionRules:
    def __init__(self, rules: list[dict], priority: list[str]):    
        self.priority = priority
        self.rules = self._sort_rules_by_priority(rules)
    
    def _sort_rules_by_priority(self, rules: list[dict]) -> list[dict]:
        """Sort rules according to the priority list."""
        
        def get_priority_index(rule):
            rule_type = rule.get('type', '')
            try:
                return self.priority.index(rule_type)
            except ValueError:
                return len(self.priority)
        
        return sorted(rules, key=get_priority_index)
    
    def find_reasons(self, contract: Contract) -> list[str]:

        reasons = []
        for rule in rules:
            if rule
                


