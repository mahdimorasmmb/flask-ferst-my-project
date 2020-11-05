from .import admin
from flask import session, render_template,request, abort,flash
from mod_users.forms import LoginForm
from mod_users.models import User

@admin.route('/')
def admin_index():
    return "Hello from admin Index"

@admin.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            abort(400)
        user = User.query.filter(User.email.ilike(f'{form.email.data}')).first()
        if not user:
            flash("Incoreent Credentials",category='error')
            return render_template('admin/login.html',form = form) 
        if  not user.check_password(form.password.data):
            flash("Incoreent Credentials",category=error)
            return render_template('admin/login.html',form = form) 
        session['email'] = user.email
        session['id'] = user.id
        print(session)    
        return "Login Successful",200 
    if session.get('email') is not None:
        return "You are already logged in "              
    return render_template('admin/login.html',form = form) 