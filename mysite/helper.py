from random import seed
from random import randrange
from tinydb import TinyDB, Query

class Question:
    def __init__(self):
        self.answers = []
        self.label = ''
        self.picture_path = ''
        self.correct_answer = ''

class Quiz:
    def __init__(self):
        self.questions = []
        self.answer_key = []
        self.user_answers = []
        self.size = 3

    def makeQuiz(self):
        # pick x random non-repeating numbers in range 0-question pool size
        taken = []
        while len(taken) < self.size:
            qID = randrange(5)  # qID will hold int 0-4 , int 5 needs to be same as size of question pool in database
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

        while index < self.size:
            current_q_id = taken[index]
            q = Question() # fresh new question object to append to self.questions after filled out with db data
            QueryBy = Query()
            table_row = questions.search(QueryBy.id == current_q_id)
            #print(table_row)
            label_data = table_row[0]['label']
            q.label = label_data
            correct_answer_data = table_row[0]['correct_answer']
            q.correct_answer = correct_answer_data
            picture_file_path = table_row[0]['picture_filename']
            q.picture_path = picture_file_path
            QueryBy2 = Query()
            table_row2 = answer_sets.search(QueryBy2.id == current_q_id)
        #   determine amount of answers, i = 0 while i < length of table_row-1, then create string 'a' + str(index+1), i = i + 1
            i = 0
            while i < (len(table_row2[0]) - 1):
                answer_index = 'a'+str(i+1)
                answer = table_row2[0][answer_index]
                q.answers.append(answer)
                i = i + 1
            self.questions.append(q)
            index = index+1
        # fill answer key by looping through filled quetions and appending questions[x].correct_answer
        for x in self.questions:
            ca = x.correct_answer
            self.answer_key.append(ca)
    
    def addUserAnswer(self, answer):
        user_answer = str(answer)
        self.user_answers.append(user_answer)
        
    def printQuestions(self):
        for x in self.questions:
            print(x.label)
            print(x.answers)
            print(x.correct_answer)
            print(x.picture_path)
            print('\n')
        
    def printAnswerKey(self):
        for x in self.answer_key:
            print(x)

if __name__ == "__main__":
    a = Quiz()
    a.makeQuiz()
    a.printQuestions()
    a.printAnswerKey()