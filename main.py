from src.orchestrator import Orchestrator
from utils.utils import empty_file
from common.constants import NOTIFICATION_LOG_FILE_PATH, CONFIG_FILE_PATH, CONTRACTS_FILE_PATH

def main():

    orchestrator = Orchestrator(config_input_path=CONFIG_FILE_PATH, contracts_input_path=CONTRACTS_FILE_PATH)
    print("Internal tool for expiring contracts renewal.")

    while True:
        cmd = input("Enter your command (\"s\" - start, \"q\" - quit or \"c\" - clean notification log): ")
        match cmd:
            case "s":
                orchestrator.load_notifications()
                orchestrator.clear_current_notifications()
                current_date_str = input("Enter the current date in format YYYY-MM-DD: ")
                try:
                    print(f"Date entered: {current_date_str}")
                    orchestrator.add_current_datetime_str(current_date_str)
                    orchestrator.check_contracts()
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD format (e.g., 2025-08-04)")
            case "q":
                print("Exiting the tool")
                break
            case "c":
                print("Clearing out notification_log.json")
                empty_file(file_path=NOTIFICATION_LOG_FILE_PATH)
            case _:
                print("Invalid command")

if __name__ == "__main__":
    main()