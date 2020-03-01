from flask_app import app
from flask import redirect, url_for, render_template
from forms import quizForm, submitForm

@app.route('/', methods=['POST','GET'])
def index():
    form = submitForm()
    if form.is_submitted():
        print('true')
        return redirect(url_for('test'))
    return render_template('index.html', title='Index Page', form=form)

@app.route('/test', methods=['POST','GET'])
def test():
    form = quizForm()
    numberCorrect=0
    if form.validate_on_submit():
        print(form.question1.data)
        if form.question1.data == "aerodactyl":
            numberCorrect += 1
            print(numberCorrect)
        print(form.question2.data)
        if form.question2.data == "f":
            numberCorrect += 1
            print(numberCorrect)
        print(form.question3.data)
        if form.question3.data == "trex":
            numberCorrect += 1
            print(numberCorrect)
        print(form.question4.data)
        if form.question4.data == "10million":
            numberCorrect += 1
            print(numberCorrect)
        print(form.question5.data)
        if form.question5.data == "velociraptor":
            numberCorrect += 1
            print(numberCorrect)
        print(numberCorrect)
        return render_template('report.html', title="Progress Page", numCorrect=numberCorrect)
    return render_template('test.html', title='Testing Page', form=form)

@app.route('/testing')
def testing():
    return render_template('base.html')