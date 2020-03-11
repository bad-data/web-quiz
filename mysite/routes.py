from flask_app import app
from flask import redirect, url_for, render_template, request, session
from forms import quizForm, submitForm, questionForm, onePageQuizForm
from helper import Quiz, Question, serializeQuiz, makeQuiz

@app.route('/', methods=['POST','GET'])
def index():
    form = submitForm()
    if form.is_submitted():
        return redirect(url_for('createquiz'))
    return render_template('index.html', title='Index Page', form=form)

@app.route('/createquiz')
def createquiz():
    triviaQuiz = makeQuiz()
    passableQuiz = serializeQuiz(triviaQuiz)
    session['quiz'] = passableQuiz
    return redirect(url_for('test2'))

@app.route('/test/<quiz>', defaults={'qNumber': 0}, methods=['POST','GET'])
@app.route('/test/<quiz>/<qNumber>', methods=['POST','GET'])
def test(quiz,qNumber):
    form = questionForm()
    qNumberInt= int(qNumber)
    accessibleQuiz = deserializeQuiz(quiz)
    choicesList = []
    #fill choices list of tuples with same values as answer name ("T-Rex","T-Rex")
    for elem in accessibleQuiz['questions'][qNumberInt]['answers']:
        newChoice = (str(elem),str(elem))
        choicesList.append(newChoice)
    print(choicesList)
    if form.validate_on_submit(): # Next Question Button Hit
        print('Question submitted')
        if qNumberInt > 9:
            # process data and stuff for quiz
            return redirect(url_for('index'))
        else:
            # update accesibleQuiz Obj user_answers, move question number up one
            accessibleQuiz['user_answers'].append(form.question.choices.data)
            qNumberInt = qNumberInt + 1
            form.question.choices = choicesList
            quiz = serializeQuiz(accessibleQuiz)
            return redirect(url_for('test.html', quiz=quiz, qNumber=qNumberInt))
    else:
        form.question.choices = choicesList
        return render_template('test.html', form=form, test=accessibleQuiz, qNumber=qNumberInt)

@app.route('/testing')
def testing():
    return render_template('base.html')

@app.route('/oldtest/<qnumber>', methods=['POST','GET'])
def oldtest(qnumber):
    #triviaQuiz = Quiz()
    #triviaQuiz.makeQuiz()
    numberCorrect = 0
    form = quizForm()
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

@app.route('/test2', methods=['POST','GET'])
#@app.route('/test2/<quiz>', methods=['POST','GET'])
#@app.route('/test2/<quiz>/<qNumber>', methods=['POST','GET'])
def test2():
    QuizObject = Quiz.deserializeQuiz(session['quiz'])
    if request.method == 'POST':
        # if form submitted, 
        QuizObject.user_answers.append(request.form["q1"])
        QuizObject.user_answers.append(request.form["q2"])
        QuizObject.user_answers.append(request.form["q3"])
        for elem in QuizObject.user_answers:
            print(elem)
        index = 0
        while index < QuizObject.size:
            if QuizObject.answer_key[index] == QuizObject.user_answers[index]:
                QuizObject.grade = QuizObject.grade + 1
            index = index + 1
        grade= QuizObject.grade
        return render_template('graded.html', grade=grade)
    else:
        questionList = []
        for item in QuizObject.questions:
            questionList.append(item)
        # Now QuizObject is current updated instance of Quiz user is taking
        question1 = []
        question2 = []
        question3 = []
        for elem in QuizObject.questions[0].answers:
            newChoice = elem
            question1.append(newChoice)
        for elem in QuizObject.questions[1].answers:
            newChoice = elem
            question2.append(newChoice)
        for elem in QuizObject.questions[2].answers:
            newChoice = elem
            question3.append(newChoice)
        #cleanCopy = serializeQuiz(QuizObject)
        #print(path)
        return render_template('quiz.html', question1=question1, question2=question2,question3=question3, accessibleQuiz=QuizObject)
        #return redirect(url_for('index'))
