# Wi-Fi Password Extraction Script

This Python script allows you to extract Wi-Fi network names and their associated passwords from a Windows system using the `netsh` command-line tool. The extracted data is stored in an SQLite database for future reference.

## Usage

1. **Clone or Download the Repository**

   Start by cloning this repository or downloading the script and database file to your local machine.

2. **Prerequisites**

   - **Python 3.x**: Make sure you have Python 3.x installed on your system.
   - **SQLite3**: SQLite3 is included with Python, so you typically don't need to install it separately.
   - **Windows**: This script is designed to work on Windows operating systems.

3. **Running the Script**

   - Open a command prompt or terminal and navigate to the directory where you have saved the script (`wifi_passwords.py`) and the SQLite database (`wifi_passwords.db`).

   - Execute the script by running the following command:

     ```bash
     python wifi_passwords.py
     ```

4. **Script Execution**

   - The script will use the `netsh` command to retrieve information about Wi-Fi profiles on your Windows system.

   - It will create an SQLite database (`wifi_passwords.db`) and a table (`wifi_passwords`) to store the network names and passwords.

   - For each Wi-Fi network profile found, the script will attempt to retrieve and store the associated password (if available).

5. **Accessing the Data**

   - You can access the collected data in the `wifi_passwords.db` database using SQLite database tools or by writing your own SQL queries.

6. **Notes**

   - Make sure to run the script with administrative privileges to access Wi-Fi password information.

   - This script is provided for educational purposes and should only be used on your own Windows computer or with proper authorization.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



# Alternate

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

