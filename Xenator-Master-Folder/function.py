with open('v_input.txt', 'r') as file:
    word = file.read().replace('\n', '')
fun = 'print'
# returns first occurrence of Substring
result = word.find(fun)

# How to use find()
if (result != -1):
    print word[word.index(fun) + len(fun):]
else:
    print ("Sorry say again")
