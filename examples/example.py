from time import sleep

from flask import Flask
from flask_restpoints import RestPoints

app = Flask(__name__)
rest = RestPoints(app)


@rest.status_job
def active_directory():
    sleep(0.5)


@rest.status_job()
def paypal():
    sleep(5)


@rest.status_job(name="PostgreSQL", timeout=5)
def postgresql():
    sleep(0.5)


@rest.status_job(timeout=5)
def db2():
    sleep(0.5)


app.run(host="0.0.0.0", debug=True)
