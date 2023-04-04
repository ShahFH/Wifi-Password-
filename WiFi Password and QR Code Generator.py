import subprocess
import pyqrcode

# Fetching WiFi SSID
wifi_ssid = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[4].split(':')[1].strip()

# Fetching WiFi password
wifi_password = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', wifi_ssid, 'key=clear']).decode('utf-8').split('\n')[26].split(':')[1].strip()

# Generating QR code
qr_code = pyqrcode.create(f'WIFI:T:WPA;S:{wifi_ssid};P:{wifi_password};;')

# Saving QR code as PNG
qr_code.png('wifi_qr_code.png', scale=10)

# Saving password to a text file
with open('wifi_password.txt', 'w') as f:
    f.write(wifi_password)

# Printing password to console
print(f'Your WiFi password is: {wifi_password}')
