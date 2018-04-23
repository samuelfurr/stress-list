from flask import render_template, flash, redirect, url_for, request, abort, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from stress import stress
from stress import db

from stress.forms import LoginForm, RegistrationForm
from stress.models import *

@stress.route('/')
@stress.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('cal', username=current_user.username))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            return redirect(url_for('cal', username=current_user.username))
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@stress.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@stress.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('cal', username=current_user.username))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        user.save()
        flash('Welcome!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@stress.route('/user/<username>/cal')
@login_required
def cal(username):
    user = User.objects(username=username).first_or_404()
    if not user.username == current_user.username:
        abort(404)
    tasks = Task.objects(user=user)
    breaks = Break.objects(user=user)
    return render_template('cal.html', user=user, tasks=tasks, breaks=breaks)

@stress.route('/user/<username>/feed')
@login_required
def feed(username):
    user = User.objects(username=username).first_or_404()
    if not user.username == current_user.username:
        abort(404)
    tasks = Task.objects(user=user)
    breaks = Break.objects(user=user)
    return render_template('feed.html', user=user, tasks=tasks, breaks=breaks)

