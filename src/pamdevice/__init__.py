#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of pam-device
#
# Copyright (c) 2019 Lorenzo Carbonell Cerezo <atareao@atareao.es>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import getpass

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
