Quick Setup (not for sample_celery_example folder)
-----------

1. Clone this repository.
2. Make sure you have redis installed in you system
3. Create a virtualenv and install the requirements.
4. Open a terminal window and start a local Redis server.
5. Open a second terminal window. Set two environment variables `MAIL_USERNAME` and `MAIL_PASSWORD` to a valid Gmail account credentials (these will be used to send test emails). Then start a Celery worker: `venv/bin/celery worker -A app.celery --loglevel=info`.
6. Start the Flask application on your original terminal window: `venv/bin/python app.py`.
7. Go to `http://localhost:5000/` and see the magic 🧙‍♂️  ✨
