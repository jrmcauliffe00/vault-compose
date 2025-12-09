import requests
from fastapi import FastAPI
import os
import uvicorn

VAULT_BASE_URL = os.getenv("VAULT_BASE_URL")
VAULT_ROOT_TOKEN = os.getenv("VAULT_ROOT_TOKEN")

app = FastAPI()

# One function to get all available engines, all roles, and all secrets
@app.get("/all")
def get_all():
    return get_all_from_vault(VAULT_BASE_URL, VAULT_ROOT_TOKEN)


def get_all_from_vault(vault_base_url: str, vault_root_token: str):
    url = f"{vault_base_url}/v1/sys/engines"
    headers = {
        "X-Vault-Token": vault_root_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        engines = response.json()
    else:
        raise Exception(f"Error fetching all from vault: {response.text}")
    url = f"{vault_base_url}/v1/auth/approle/roles"
    headers = {
        "X-Vault-Token": vault_root_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        roles = response.json()
    else:
        raise Exception(f"Error fetching all roles from vault: {response.text}")
    url = f"{vault_base_url}/v1/secret/metadata"
    headers = {
        "X-Vault-Token": vault_root_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        secrets = response.json()
    else:
        raise Exception(f"Error fetching all secrets from vault: {response.text}")

    return {
        "engines": engines,
        "roles": roles,
        "secrets": secrets
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)