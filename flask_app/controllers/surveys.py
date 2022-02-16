
from flask_app import app 
from flask import redirect, render_template, session, request
from flask_app.models.survey import Survey






@app.route('/')
def root_route():
    return render_template('index.html')

@app.route('/showuser', methods=['POST'])
def create_user():
    print('Got user info')
    session['name'] = request.form['name']
    session['language'] = request.form['language']
    session['location'] = request.form['location']
    session['comment'] = request.form['comment']

    if not Survey.validate_survey(request.form):
        return redirect('/')
# add validations 
    new_survey = Survey.save(request.form)

    return redirect('/show')


@app.route('/show')
def show_user():
    print("Showing the user")
    print(session['name'])
    return render_template('show.html')