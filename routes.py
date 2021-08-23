from app import app, db
from flask import render_template, url_for, redirect, flash, get_flashed_messages
from datetime import datetime

import models
import forms

@app.route('/')
@app.route('/index')
def index():    
    tasks = models.Task.query.all()
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods = ["GET", "POST"])
def add():
    form = forms.AddTaskForm() # create a form object
    if form.validate_on_submit(): # if form is submitted
        t = models.Task(title=form.title.data, date=datetime.utcnow()) 
        db.session.add(t)
        db.session.commit()
        flash('Task added to the database')
        return redirect(url_for('index')) # go to index page
        # return render_template('about.html', form=form, title=form.title.data)
    return render_template('add.html', form=form)

@app.route('/edit/<int:task_id>', methods = ["GET", "POST"])
def edit(task_id):
    task = models.Task.query.get(task_id) # get task by its id
    form = forms.AddTaskForm()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash("task has been updated")
            return redirect(url_for('index'))
        form.title.data = task.title
        return render_template('edit.html', form = form, task_id=task_id)
    else:
        flash("task not found!")
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods = ["GET", "POST"])
def delete(task_id):
    task = models.Task.query.get(task_id) # get task by its id
    form = forms.DeleteTaskForm()

    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("task has been deleted")
            return redirect(url_for('index'))
        return render_template('delete.html', form = form, task_id=task_id, title = task.title)
    else:
        flash("Task not found!")
    return redirect(url_for('index'))
