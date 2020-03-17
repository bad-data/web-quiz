# This file is to hold db operations and data structures that will hold quiz info

from tinydb import TinyDB, Query

db = TinyDB('database.json')

qtable = db.table('questions')
atable = db.table('answer_sets')
# correct add questions table format
# qtable.insert({'id': 5, 'label': "Which dinosaur’s name means “three horned face” but only had two horns?", 'correct_answer': "Triceratops", 'answer_set_id': 5, 'picture_filename': "None"})
# correct add answer_sets table format
# atable.insert({'id': 5, 'a1': "Brachiosaurus", 'a2': "Tyrannosaurus-Rex", 'a3': "Spinosaurus", 'a4': "Triceratops"})

qtable.remove(doc_ids=[1,2,3,4])
atable.remove(doc_ids=[1,2,3,4])

#atable.all()
#for row in atable:
    #print(row)

qtable.all()
for row in qtable:
    print(row)

#Label = Query()
#hi = table.search(Label.id == 0)
#data = hi[0]['a3']
#print(data)