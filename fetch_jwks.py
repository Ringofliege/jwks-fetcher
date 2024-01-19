import requests
import time
import os

KEYCLOAK_URL = os.environ.get('KEYCLOAK_URL')
REALM = os.environ.get('REALM')
JWKS_PATH = os.environ.get('JWKS_PATH', '/jwks/jwks.json')
UPDATE_INTERVAL = int(os.environ.get('UPDATE_INTERVAL', 3600))

def fetch_jwks():
    jwks_url = f"{KEYCLOAK_URL}/auth/realms/{REALM}/protocol/openid-connect/certs"
    response = requests.get(jwks_url)
    response.raise_for_status()
    return response.json()

def main():
    while True:
        try:
            jwks = fetch_jwks()
            with open(JWKS_PATH, 'w') as f:
                f.write(str(jwks))
            print(f"JWKS updated at {JWKS_PATH}")
        except Exception as e:
            print(f"Error fetching JWKS: {e}")

        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
