# Installation instructions

Use python 3.11 or later and Node 19.0.0 or later.

```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
cd backend/
python manage.py migrate
cd ../frontend/
npm i --force
```


# Usage

For the backend, run the following command:

```bash
cd backend/
python manage.py runserver
```

For the frontend, run the following command:

```bash
cd frontend/
bun run dev
```
