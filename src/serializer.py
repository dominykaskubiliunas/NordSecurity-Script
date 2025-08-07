from common.constants import *
from src.contract import Contract

class Serializer:
    @staticmethod
    def notification_output(contract: Contract, reason: str) -> dict:
        return {
            KEY_SOFTWARE_NAME: contract.data.get(KEY_SOFTWARE_NAME, "Unknown Software Name"),
            KEY_OWNER: contract.data.get(KEY_OWNER, "Unknown Owner"),
            KEY_ORGANIZATION: contract.data.get(KEY_ORGANIZATION, "Unknown Organization"),
            KEY_ANNUAL_COST: contract.data.get(KEY_ANNUAL_COST, "Unknown Annual Cost"),
            KEY_RENEWAL_DATE: contract.data.get(KEY_RENEWAL_DATE, "Unknown Annual Cost"),
            KEY_REASON: reason
        }

    @staticmethod
    def notification_log_entry(notified_on: str, reason: str) -> dict:
        return {
            KEY_NOTIFIED_ON: notified_on,
            KEY_REASON: reason
        }

