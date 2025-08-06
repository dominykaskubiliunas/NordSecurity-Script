from datetime import datetime
from src.orchestrator import Orchestrator
from utils.utils import save_json, empty_file

def main():

    orchestrator = Orchestrator(config_input_path="inputs/config.json", contracts_input_path="inputs/contracts.json")
    print("Internal tool for identifying and categorize expiring contracts for renewal.")

    while True:
        cmd = input("Enter your command (\"s\" - start, \"q\" - quit or \"c\" - clean notification log): ")
        
        match cmd:
            case "s":
                orchestrator.load_notifications_log()
                current_date_str = input("Enter the current date in format YYYY-MM-DD: ")
                try:
                    print(f"Date entered: {current_date_str}")
                    orchestrator.add_current_datetime_str(current_date_str)
                    orchestrator.load_notifications_log()
                    notification_dict = orchestrator.check_contracts()
                    save_json(notification_dict, file_path="inputs/notification_log.json")
                
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD format (e.g., 2025-08-04)")
            case "q":
                print("Exiting the tool")
                break
            case "c":
                print("Clearing out notification_log.json")
                empty_file(file_path="inputs/notification_log.json")
            case _:
                print("Invalid command")





if __name__ == "__main__":
    main()