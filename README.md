# LunchBuddy

This service is used for lunch_buddy.

Tech stack: Django, Docker, Postgresql

## Local development installation
1. At first pull the repository.


2. Create a virtual environment then activate it.

```bash
python -m venv "venv"
cd venv
cd Scripts
activate
```


3. Install the required packages.

```bash
pip install -r backend/requirements/dev.txt
```


4. Install pre-commit to configure git commit hook.

```bash
pre-commit install
```


5. Run the project:

```bash
docker-compose up --build
```

Now click on this [URL](http://0.0.0.0:8023/admin/)  to check it works.


## Contributing

1. Create a new branch from the main branch then send the pull request.
