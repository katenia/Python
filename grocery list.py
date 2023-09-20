
todo = []
print ('I am going to help you make a to do list.')

while True:
    print ('Enter task ' + str(len(todo) + 1) +  ' on your list. (If you are done entering task type "z" and press enter):')
    item = input ()
    if item == 'z':
        break
    todo = todo + [item]


print ('The todo list is:')
for item in todo:
    print(' ' + item)
