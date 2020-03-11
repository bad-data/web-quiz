from random import seed
from random import randrange
from tinydb import TinyDB, Query
import json
from typing import List

class Question:
    def __init__(self, answers = [], correct_answer = [], label = '', picture_path = ''):
        self.answers = answers  # list of strings
        self.label = label # string
        self.picture_path = picture_path # string
        self.correct_answer = correct_answer # string
    
    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)
    
    def printQuestion(self):
        print(self.answers)
        print(self.label)
        print(self.picture_path)
        print(self.correct_answer)
        print('\n')

class Quiz:
    def __init__(self, answer_key = [], grade = 0, questions = [], size = 3, user_answers = []):
        self.questions = questions #list of Question objects
        self.answer_key = answer_key    # list of strings
        self.user_answers = user_answers    # list of strings
        self.size = size    # interger size
        self.grade = grade  # integer grade
    
    def addUserAnswer(self, answer):
        user_answer = str(answer)
        self.user_answers.append(user_answer)
        
    def printQuestions(self):
        for x in self.questions:
            x.printQuestion()
        
    def printAnswerKey(self):
        for x in self.answer_key:
            print(x)
    
    def gradeQuiz(self):
        i = 0
        while i < self.size:
            if self.answer_key[i] == self.user_answers[i]:
                self.grade = self.grade + 1

    def serializeQuiz(self):
        data = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        return data

    @classmethod
    def deserializeQuiz(cls, json_data: dict):
        json_dict = json.loads(json_data)
        Questions = list(map(Question.from_json, json_dict['questions']))
        AnswerKey = list(json_dict['answer_key'])
        UserAnswers = list(json_dict['user_answers'])
        Grade= json_dict['grade']
        Size= json_dict['size']
        # create Quiz object with parsed json data and return it
        deserialized = Quiz(answer_key=AnswerKey, grade=Grade, questions=Questions, size=Size, user_answers=UserAnswers)
        return deserialized

def serializeQuestion(Question):
    a = Question
    json_data = json.dumps(a.__dict__)
    d = json.loads(json_data)
    return d

def serializeQuiz(x):
    data = json.dumps(x.__dict__, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return data

def makeQuiz():
    # make all variables needed to fill for constructor
    quizAnswer_key = []
    quizGrade = 0
    quizSize = 3
    quizQuestions = []  # this will be a list full of Question objects
    quizUser_Answers = []
    # pick x random non-repeating numbers in range 0-question pool size
    taken = []
    while len(taken) < quizSize:
        qID = randrange(28)  # qID will hold int 0-4 , int 5 needs to be same as size of question pool in database
        while qID in taken:
            qID = randrange(5)
        taken.append(qID)
    print(taken)
    # taken now contains 3 seperate question IDs, query databse and fill each Question in list questions with necessary info
    # puesocode here
    index = 0

    db = TinyDB('database.json')
    questions = db.table('questions')
    answer_sets = db.table('answer_sets')

    while index < quizSize:
        current_q_id = taken[index]
        #q = Question() # fresh new question object to append to self.questions after filled out with db data
        QueryBy = Query()
        table_row = questions.search(QueryBy.id == current_q_id)
        #print(table_row)
        label_data = table_row[0]['label']
        #q.label = label_data
        correct_answer_data = table_row[0]['correct_answer']
        quizAnswer_key.append(correct_answer_data)
        #q.correct_answer = correct_answer_data
        picture_file_path = table_row[0]['picture_filename']
        #q.picture_path = picture_file_path
        QueryBy2 = Query()
        table_row2 = answer_sets.search(QueryBy2.id == current_q_id)
        #   determine amount of answers, i = 0 while i < length of table_row-1, then create string 'a' + str(index+1), i = i + 1
        i = 0
        questionAnswers = []
        while i < (len(table_row2[0]) - 1):
            answer_index = 'a'+str(i+1)
            answer = table_row2[0][answer_index]
            questionAnswers.append(answer)
            i = i + 1
        aQuestion = Question(answers=questionAnswers,correct_answer=correct_answer_data,label=label_data,picture_path=picture_file_path)
        quizQuestions.append(aQuestion)
        index = index+1
        # now everything should be filled create a Quiz Object and return it
    Quiz4Return = Quiz(answer_key=quizAnswer_key,grade=quizGrade,questions=quizQuestions,size=quizSize,user_answers=quizUser_Answers)
    return Quiz4Return

#def deserializeQuiz(x):

#if __name__ == "__main__":
    #b = Question()
    #b.label = 'How are you doing?'
    #b.picture_path = 'None'
    #b.correct_answer = 'fine'
    #b.answers = ['good','bad','fine']
    #serializedQuestion = serializeQuestion(b)
    #print(serializedQuestion)
    #a = makeQuiz()
    #a.printQuestions()
    #serializedQuiz = serializeQuiz(a)
    #print(serializedQuiz)
    #quiz = a.deserializeQuiz(serializedQuiz)
    #quiz.printQuestions()
    #quiz.printAnswerKey()
    #print(quiz)
    #b = deserializeQuiz(serializedQuiz)
    #print(b['questions'][2]['answers'])
    