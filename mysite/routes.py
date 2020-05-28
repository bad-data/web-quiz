from flask_app import app
from flask import redirect, url_for, render_template, request, session
from forms import quizForm, submitForm, questionForm, onePageQuizForm
from helper import Quiz, Question, serializeQuiz, makeQuiz
import os

@app.route('/', methods=['POST','GET'])
def index():
    form = submitForm()
    if form.is_submitted():
        return redirect(url_for('createquiz'))
    return render_template('index.html', title='Index Page', form=form)


@app.route('/test', methods=['GET','POST'])
def test():
    return render_template('testkeys1.html')

@app.route('/createquiz')
def createquiz():
    triviaQuiz = makeQuiz()
    passableQuiz = serializeQuiz(triviaQuiz)
    session['quiz'] = passableQuiz
    session['questionNumber'] = 0
    #return redirect(url_for('takequiz'))
    return redirect(url_for('exam', questionNumber=session['questionNumber']))

@app.route('/takequiz', methods=['POST','GET'])
#@app.route('/test2/<quiz>', methods=['POST','GET'])
#@app.route('/test2/<quiz>/<qNumber>', methods=['POST','GET'])
def takequiz():
    QuizObject = Quiz.deserializeQuiz(session['quiz'])
    if request.method == 'POST':
        # if form submitted, 
        QuizObject.user_answers.append(request.form["q1"])
        QuizObject.user_answers.append(request.form["q2"])
        QuizObject.user_answers.append(request.form["q3"])
        QuizObject.user_answers.append(request.form["q4"])
        QuizObject.user_answers.append(request.form["q5"])
        QuizObject.user_answers.append(request.form["q6"])
        QuizObject.user_answers.append(request.form["q7"])
        QuizObject.user_answers.append(request.form["q8"])
        QuizObject.user_answers.append(request.form["q9"])
        QuizObject.user_answers.append(request.form["q10"])
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
        question4 = []
        question5 = []
        question6 = []
        question7 = []
        question8 = []
        question9 = []
        question10 = []
        picPathLists = [] # this will be a list of dictionaires, holding exists and path values
        itr = 0
        while itr < QuizObject.size:
            if QuizObject.questions[itr].picture_path != "None":
                elemPicturePath = "../static/pictures/" + QuizObject.questions[itr].picture_path
                if os.path.exists(elemPicturePath[3:]):
                    print("it exists")
                    #print(elemPicturePath[3:])
                    listItem = {"exists":"yes","path":str(elemPicturePath)}
                    picPathLists.append(listItem)
                else:
                    print("not here")
            else:
                listItem = {"exists":"no","path":"None"}
                picPathLists.append(listItem)
            itr += 1
        print(picPathLists)
        for elem in QuizObject.questions[0].answers:
            newChoice = elem
            question1.append(newChoice)
        for elem in QuizObject.questions[1].answers:
            newChoice = elem
            question2.append(newChoice)
        for elem in QuizObject.questions[2].answers:
            newChoice = elem
            question3.append(newChoice)
        for elem in QuizObject.questions[3].answers:
            newChoice = elem
            question4.append(newChoice)
        for elem in QuizObject.questions[4].answers:
            newChoice = elem
            question5.append(newChoice)
        for elem in QuizObject.questions[5].answers:
            newChoice = elem
            question6.append(newChoice)
        for elem in QuizObject.questions[6].answers:
            newChoice = elem
            question7.append(newChoice)
        for elem in QuizObject.questions[7].answers:
            newChoice = elem
            question8.append(newChoice)
        for elem in QuizObject.questions[8].answers:
            newChoice = elem
            question9.append(newChoice)
        for elem in QuizObject.questions[9].answers:
            newChoice = elem
            question10.append(newChoice)
        #cleanCopy = serializeQuiz(QuizObject)
        #print(path)
        return render_template('quiz.html', question1=question1, question2=question2,question3=question3,question4=question4,question5=question5,question6=question6,question7=question7,question8=question8,question9=question9,question10=question10, accessibleQuiz=QuizObject,picPaths = picPathLists)
        #return redirect(url_for('index'))


@app.route('/exam', methods=['POST','GET'])
@app.route('/exam/<int:questionNumber>', methods=['POST','GET'])
def exam(questionNumber):
    QuizObject = Quiz.deserializeQuiz(session['quiz'])
    qNumber = int(questionNumber)
    print(QuizObject.user_answers)
    if request.method == "POST":
        # save requested data into last data
        QuizObject.user_answers.append(request.form["questionData"])
        passableQuiz = serializeQuiz(QuizObject)
        session['quiz'] = passableQuiz
        qNumber = qNumber + 1
        if qNumber < 10:
            #in here when qNumber is 0-9, which is questions 1-10 in QuizObject
            # render template with passing values with new values from quizObject
            #quizQuestion = QuizObject.questions[qNumber].label
            #answerList = QuizObject.questions[qNumber].answers
            #print(answerList)
            return redirect(url_for('exam', questionNumber=qNumber))
        else:
            # quiz is done and needs to graded
            for elem in QuizObject.user_answers:
                print(elem)
            index = 0
            while index < QuizObject.size:
                if QuizObject.answer_key[index] == QuizObject.user_answers[index]:
                    QuizObject.grade = QuizObject.grade + 1
                index = index + 1
            grade= QuizObject.grade
            #STOP THERE NEEDS TO A REDIRECT_URL for PRG pattern
            return render_template('graded.html', grade=grade)
    else:
        quizQuestion = QuizObject.questions[qNumber].label
        answerList = QuizObject.questions[qNumber].answers
        print(answerList)
        return render_template('questionPage.html', questionNumber=qNumber, question=quizQuestion, answers=answerList)