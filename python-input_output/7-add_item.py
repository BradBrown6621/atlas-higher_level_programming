#!/usr/bin/python3
"""
This module loads/saves Python objects in JSON files
"""

import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except Exception:
    json_list = []

for i in range(1, len(sys.argv)):
    json_list.append(sys.argv[i])

save_to_json_file(json_list, filename)
