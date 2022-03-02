grocery_list = []
appended_str = 'tmp'
while(len(appended_str) != 0):
    inp_req = input()
    appended_str = str(inp_req)
    if (len(appended_str) == 0):
        break
    grocery_list.append(appended_str)
print(grocery_list)
