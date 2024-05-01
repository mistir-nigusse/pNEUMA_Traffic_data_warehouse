#!/usr/bin/env python
import os
import subprocess

def install_dbt():
    """Install dbt."""
    subprocess.run(["pip", "install", "dbt"])

def main():
    # Install dbt
    install_dbt()

    # Continue with the original entrypoint command (starting Airflow)
    original_entrypoint = "/entrypoint"
    os.execv(original_entrypoint, [original_entrypoint])

if __name__ == "__main__":
    main()
