import random

all_lessons = ('语文', '数学', '英语', '美术', '思品', '手工', '体育', '科学', '书法',)

var_lessons = []
for row in range(1,6):
    row_data = []
    for col in range(1,3):
        if col == 1:
            row_data.append(row)
        else:
            row_data.append(random.choice(all_lessons))
        #print(row_data)
    var_lessons.append(row_data)

print(var_lessons)
