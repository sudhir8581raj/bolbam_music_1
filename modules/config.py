import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID","22337090"))
API_HASH = getenv("API_HASH","3f8e855a5d11abbaec517fc5d3535dc8")
BOT_TOKEN = getenv("BOT_TOKEN","6702023295:AAHYwWlJqTvAb5OP1KKc5lcfjDrOwW7l_qc)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION","BQFU1kIAszX4eNmlZkp5krrIQl-lTv7vhj2mF1w3MUFKjPInm243LXP_nJJmh0fJTz8q2Earpc6zng8Z36LZAeFeEJEusBm0B7tndblYkauVLHOCZrFk7opSfWOaR4Q89tt-M4hkSKEJDZNz6k5NXTNCApyxfwVzXRiKF0zoCjkp-vJoXddew8GYwjo17VoFc7bAU3a0DAVbDBMNpFuXxySfhZv0VWNFYEUUCEJchzREDpmYyHgmDQ_ERjxrqWxzmIGzzK2_k5icJWwGqfxhkmbeNEFV8gtDDLYBucOnVIt_FySgqRGwVX5R40bfAGZxyIPsIE2YjMsNWGb7z4Tc7aaWQ1QpdQAAAAF91qcwAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5990221577").split()))
aiohttpsession = aiohttp.ClientSession()
