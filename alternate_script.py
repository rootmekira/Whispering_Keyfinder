import sqlite3
import subprocess

# Create a connection to the database
conn = sqlite3.connect('wifi_passwords.db')

# Create a table to store Wi-Fi passwords
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS wifi_passwords
                  (network_name TEXT, password TEXT)''')

# Retrieve Wi-Fi passwords using netsh command on Windows
netsh_command = "netsh wlan show profile | findstr /C:\"All User Profile\""
netsh_output = subprocess.run(netsh_command, capture_output=True, shell=True).stdout.decode()

profiles = [line.strip() for line in netsh_output.split("\n") if "All User Profile" in line]

for profile in profiles:
    try:
        profile_name = profile.split(":")[1].strip()
        password_output = subprocess.run(f"netsh wlan show profile name=\"{profile_name}\" key=clear | findstr /C:\"Key Content\"",
                                         capture_output=True, shell=True).stdout.decode()
        password = [line.split(":")[1].strip() for line in password_output.split("\n") if "Key Content" in line][0]
        cursor.execute("INSERT INTO wifi_passwords VALUES (?, ?)", (profile_name, password))
    except IndexError:
        continue

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
