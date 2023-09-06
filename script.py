import sqlite3
import subprocess

# Create a connection to the database
conn = sqlite3.connect('wifi_passwords.db')

# Create a table to store Wi-Fi passwords
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS wifi_passwords
                  (network_name TEXT, password TEXT)''')

# Retrieve Wi-Fi passwords using netsh command on Windows
if subprocess.run("netsh wlan show profile", capture_output=True).returncode == 0:
    output = subprocess.run("netsh wlan show profile", capture_output=True).stdout.decode()
    profiles = [line.split(":")[1][1:-1] for line in output.split("\n") if "All User Profile" in line]
    for profile in profiles:
        try:
            password_output = subprocess.run(f"netsh wlan show profile name={profile} key=clear",
                                             capture_output=True).stdout.decode()
            password = [line.split(":")[1][1:-1] for line in password_output.split("\n") if "Key Content" in line][0]
            cursor.execute("INSERT INTO wifi_passwords VALUES (?, ?)", (profile, password))
        except IndexError:
            continue

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
