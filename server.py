from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'password'

@app.route('/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return "Total count: {}".format(session.get('visits'))

@app.route('/destroy_session')
def destroySession():
    session.pop('visits', None)
    print('session deleted...')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)