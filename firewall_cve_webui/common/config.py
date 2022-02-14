import os
from dotenv import load_dotenv,find_dotenv
from pathlib import Path

try:
    env_file = find_dotenv()
    load_dotenv(env_file)
except:
    raise ("Could not open ..env file; please make sure it exsists!")

netmon_url = os.environ['NETMON_URL']
netmon_token = os.environ['NETMON_TKN']
cve_url = os.environ['CVE_URL']
