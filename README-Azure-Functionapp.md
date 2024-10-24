1. Create venv in project - do not use poetry
2. `pip install -r requirements.txt`
3. testing: `func start`
4. deployment: `func azure functionapp publish abis-portal-api --build remote`

Local testing:

1. `pyenv virtualenv 3.11.8 abis_portal` 
2. `pyenv activate abis_portal`