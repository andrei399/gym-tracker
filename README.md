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

You can use the `start.sh` script to run both the backend and the frontend at the same time(requires tmux)
Alternatively, you can run the backend and frontend separately.

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
