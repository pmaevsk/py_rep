grocery_list = []
appended_str = 'tmp'
while(appended_str != ''):
    # inp_req = input()
    appended_str = input()
    if (appended_str):
        grocery_list.append(appended_str)
    else:
        break
    grocery_list.append(appended_str)
print(grocery_list)
