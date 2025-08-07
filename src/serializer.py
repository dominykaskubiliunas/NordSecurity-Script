from common.constants import *
from src.contract import Contract

class Serializer:
    @staticmethod
    def contract_notification_output(contract: Contract, reason: str) -> dict:
        return {
            KEY_SOFTWARE_NAME: contract.get_software_name(),
            KEY_OWNER: contract.get_owner(),
            KEY_ORGANIZATION: contract.get_organization(),
            KEY_ANNUAL_COST: contract.get_annual_cost(),
            KEY_RENEWAL_DATE: contract.get_renewal_date(),
            KEY_REASON: reason
        }

    @staticmethod
    def contract_log_entry(notified_on: str, reason: str) -> dict:
        return {
            KEY_NOTIFIED_ON: notified_on,
            KEY_REASON: reason
        }

