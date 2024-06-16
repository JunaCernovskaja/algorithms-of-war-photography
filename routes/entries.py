from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from flask_app import db
from flask_app.models import Entry
from flask_app.forms import EntryForm

entries = Blueprint('entries', __name__)

@entries.route('/new_entry', methods=['GET', 'POST'])
@login_required
def new_entry():
    form = EntryForm()
    if form.validate_on_submit():
        new_entry = Entry(income=True, sum=form.sum.data, user_id=current_user.id)
        db.session.add(new_entry)
        db.session.commit()
        flash('Entry was created successfully', 'success')
        return redirect(url_for('entries.entries'))
    return render_template('new_entry.html', form=form)

@entries.route('/entries')
@login_required
def entries():
    my_entries = Entry.query.filter_by(user_id=current_user.id).all()
    return render_template('entries.html', all_entries=my_entries)

@entries.route('/balance')
@login_required
def balance():
    all_entries = Entry.query.filter_by(user_id=current_user.id)
    balance = 0
    for entry in all_entries:
        if entry.income:
            balance += entry.sum
        else:
            balance -= entry.sum
    return render_template('balance.html', balance=balance)