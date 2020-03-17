import os

try:
	user = os.getlogin()
except Exception:
	user = os.environ.get("SUDO_USER")

# If that fails, try to get the direct user
if user == "root" or user is None:
	env_user = getpass.getuser().strip()

	# If even that fails, error out
	if env_user == "":
		print("Could not determine user, please use the --user flag")
		sys.exit(1)
	else:
		user = env_user

CONFIG_DIR = os.path.join('var', 'lib', 'pam-device', user)

CONFIG_FILE = os.path.join(CONFIG_DIR, 'pam-device.json')
PARAMS = {'usb': [],
          'bluetooth-scan-timeout': 8,
          'bluetooth-check-timeout': 2,
          'bluetooth': []}
