# Wi-Fi Password Extractor

This Python script allows you to retrieve Wi-Fi network names and their associated passwords on a Windows system using the `netsh` command. The extracted data is stored in an SQLite database for future reference.

## Prerequisites

Before using this script, make sure you have the following prerequisites installed:

- Python 3.x
- SQLite3 (included with Python)
- Windows operating system (tested on Windows)

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script (`wifi_passwords.py`) and the SQLite database (`wifi_passwords.db`).

3. Run the script using the following command:

4. The script will execute the necessary `netsh` commands to retrieve Wi-Fi network profiles and their passwords.

5. The extracted data will be stored in the `wifi_passwords.db` SQLite database in a table called `wifi_passwords`.

6. You can access the Wi-Fi network names and passwords by querying the database using SQL commands or by using an SQLite database viewer.

## Notes

- If you encounter any issues or errors while running the script, please make sure that you have administrative privileges on your Windows system.

- This script is intended for educational purposes and should only be used on your own Windows computer or with proper authorization.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
