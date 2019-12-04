
#from flask import url_for
from app import db




class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))

class Appointment(db.Model):
    appo_id = db.Column(db.Integer, primary_key=True)
    appo_title = db.Column(db.String(128), index = True)
    appo_date = db.Column(db.DateTime)
    appo_duration = db.Column(db.String(128))
    appo_location = db.Column(db.String(256))
    appo_customer_name = db.Column(db.String(128))
    appo_notes = db.Column(db.String(300))
