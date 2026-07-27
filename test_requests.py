import requests

try:
    response = requests.get("https://www.google.com", timeout=10)
    print("Google Status:", response.status_code)

    response = requests.get("https://api.mfapi.in/mf/125497", timeout=10)
    print("MFAPI Status:", response.status_code)

except Exception as e:
    print("Error:", e)