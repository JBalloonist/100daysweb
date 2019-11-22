from program import app
from flask import render_template, flash, redirect
from program.forms import LoginForm, StoreForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/100Days')
def p100Days():
	return render_template('100days.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/store', methods=['GET', 'POST'])
def store():
    form = StoreForm()
    if form.validate_on_submit():
        flash('Store data submitted!')
        return redirect('/index')
    return render_template('store.html', title='Store', form=form)
