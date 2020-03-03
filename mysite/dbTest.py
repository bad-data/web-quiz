# This file is to hold db operations and data structures that will hold quiz info

from tinydb import TinyDB, Query

db = TinyDB('database.json')

table = db.table('answer_sets')

table.all()
for row in table:
    print(row)

Label = Query()
hi = table.search(Label.id == 0)
data = hi[0]['a3']
print(data)