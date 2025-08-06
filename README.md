### Prerequisites
- Python 3.11 or higher

### Running the Application

1. **Navigate to the project directory:**
   ```bash
   cd NordSecurity-Script
   ```

2. **Run the main application:**
   ```bash
   python main.py
   ```

3. **Follow the interactive prompts:**
   - Enter `s` to start contract evaluation
   - Enter current date in YYYY-MM-DD format
   - Enter `c` to clear notification log
   - Enter `q` to quit

### Running Unit Tests

To run the test suite:
```bash
python -m pytest tests/
```

For verbose output:
```bash
python -m pytest tests/ -v
```

## Configuration

- **Contracts**: Place contract data in `inputs/contracts.json`
- **Rules**: Configure decision rules in `inputs/config.json`
- **Notifications**: Historical notifications are stored in `inputs/notification_log.json`

### Installation
Script was built with Standard Python Libraries, thus there is no need for installing requirements

```bash
# For development (including test dependencies)
pip install -r requirements-dev.txt
```
