from flask import render_template,  redirect, url_for
from app.appointment import bp
from app import db
from app.appointment.forms import AppointmentForm
from app.models import Appointment

@bp.route('/appointment', methods=['GET', 'POST'])
def appointment():
    form = AppointmentForm()

    if form.validate_on_submit():
        new_appo = Appointment()
        new_appo.appo_title =  form.appo_title.data
        new_appo.appo_date = form.appo_date.data
        new_appo.appo_duration = form.appo_duration.data
        new_appo.appo_location = form.appo_location.data
        new_appo.appo_customer_name = form.appo_customer_name.data
        new_appo.appo_notes = form.appo_notes.data

        db.session.add(new_appo)
        db.session.commit()

        return redirect(url_for('appointment.appointment'))

    appo_list = db.session.query(Appointment).all()

    return render_template("appointment/appointment.html", appo_list=appo_list,form=form)

@bp.route('/appointment/remove/<int:appo_id>', methods=['GET', 'POST'])
def remove_appo(appo_id):
    Appointment.query.filter(Appointment.appo_id == appo_id).delete()
    db.session.commit()

    return redirect(url_for('appointment.appointment'))

@bp.route('/appointment/edit/<int:appo_id>', methods=['GET', 'POST'])
def edit_appointment(appo_id):
    form = AppointmentForm()

    if form.validate_on_submit():
        current_appo = Appointment.query.filter_by(appo_id=appo_id).first_or_404()
        current_appo.appo_title = form.appo_title.data
        current_appo.appo_date = form.appo_date.data
        current_appo.appo_duration = form.appo_duration.data
        current_appo.appo_location = form.appo_location.data
        current_appo.appo_customer_name = form.appo_customer_name.data
        current_appo.appo_notes = form.appo_notes.data

        db.session.add(current_appo)
        db.session.commit()

        return redirect(url_for('appointment.appointment'))

    current_appo = Appointment.query.filter_by(appo_id=appo_id).first_or_404()

    form.appo_title.data = current_appo.appo_title
    form.appo_date.data = current_appo.appo_date
    form.appo_duration.data = current_appo.appo_duration
    form.appo_location.data = current_appo.appo_location
    form.appo_customer_name.data = current_appo.appo_customer_name
    form.appo_notes.data = current_appo.appo_notes

    return render_template("appointment/appointment_edit.html", form=form, appo_id=appo_id)
