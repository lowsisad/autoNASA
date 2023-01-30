#API
ENDPOINT = "https://api.nasa.gov/"
METHOD = "planetary/apod"
API_KEY = "api_key=l3WFEcWttxd73RGefoTlXBhMmo7XVMXa8NgXusrY"

#status_codes
successfully = 200
fail = 400
fail_auth = 403

#dates
normal = "2023-01-01"
tooOld = "1970-01-01"
future = "2077-01-01"
weird = "2022-02-30"

#message
future_msg = "Date must be between Jun 16, 1995 and Jan 30, 2023."