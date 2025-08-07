import json
import os
from typing import Dict, Set

def filter_keys(data: Dict, keys_to_exclude: Set) -> Dict:
    """Returns a new dictionary with specified keys excluded"""
    return {key: value for key, value in data.items() if key not in keys_to_exclude}

def load_json(file_path: str) -> dict:
    """Load JSON file into a dictionary, return empty dict if file is empty or doesn't exist."""
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return {}
    
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_json(data: dict, file_path: str, indent: int = 4) -> None:
    """Save dictionary data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=indent)

def empty_file(file_path: str) -> None:
    """Clears the content of the JSON file"""
    open(file_path, 'w').close()

