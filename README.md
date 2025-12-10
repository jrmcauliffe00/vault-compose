# Hashicorp Vault in docker compose easy to launch

Hashicorp announced core projects would move from the open-source license MPL 2.0 ot a more restrictive Business Source Licence v1.1

This project utilizes the last open-source available image to run a local instance of Hashicorp Vault

## Quick Start

To quickly start a local Vault instance using Docker Compose:

1. **Clone this repository** (if not already):
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Copy and edit environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env if you wish to change VAULT_ROOT_TOKEN etc.
   ```

3. **Start Vault using Docker Compose:**
   ```bash
   docker compose -f docker-compose.vault.yaml up -d
   ```

4. **Access the Vault UI:**
   - Visit [http://localhost:8200/](http://localhost:8200/) in your browser.
   - Login with the root token specified in your `.env` file.

5. **Stop Vault:**
   ```bash
   docker compose -f docker-compose.vault.yaml down
   ```

**Note:**  
- The configuration uses the last MPL-licensed Vault image (`hashicorp/vault:1.14.0`).  
- Secrets and configuration are stored in dedicated bind mounts; you can clean up local data by removing the `vault_data` folder.

Refer to [Project/config.hcl](Project/config.hcl) for Vault server config and [Project/docker-compose.vault.yaml](Project/docker-compose.vault.yaml) for container setup.
