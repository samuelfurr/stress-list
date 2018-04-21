from flask import render_template, flash, redirect, url_for, request, abort, jsonify
from stress import stress
from stress import db

@stress.route('/')
@stress.route('/index')
def index():
    return render_template('index.html', title='Home')
