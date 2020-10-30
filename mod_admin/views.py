from .import admin
from flask import session

@admin.route('/')
def admin_index():
    return "Hello from admin Index"

@admin.route('/login')
def login():
    session['name'] = 'mahdi'
    print(session)
    return '1'    