from flask import Flask, render_template, request, redirect, session
import requests

app = Flask(__name__)

app.secret_key = "quizmaster"


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form.get('username')

        session['user'] = username

        return redirect('/quiz')

    return render_template('login.html')


# Quiz Page
@app.route('/quiz')
def quiz():

    if 'user' not in session:
        return redirect('/login')

    url = "https://opentdb.com/api.php?amount=5&type=multiple"

    response = requests.get(url)

    data = response.json()

    questions = data['results']

    return render_template(
        'quiz.html',
        questions=questions
    )

@app.route('/result', methods=['POST'])
def result():

    return render_template('result.html')

# Logout
@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)