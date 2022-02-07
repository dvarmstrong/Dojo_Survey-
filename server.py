from flask import Flask, redirect, render_template, session, request



app = Flask(__name__)
app.secret_key = 'ssh its a secret'

@app.route('/')
def root_route():
    return render_template('index.html')

@app.route('/showuser', methods=['POST'])
def create_user():
    print('Got user info')
    session['name'] = request.form['name']
    session['language'] = request.form['language']
    session['location'] = request.form['location']
    session['message'] = request.form['message']

    return redirect('/show')


@app.route('/show')
def show_user():
    print("Showing the user")
    print(session['name'])
    return render_template('show.html')



















if __name__=="__main__":
    app.run(debug=True)