grocery_list = []
grocery_dict = {}
appended_str = 'tmp'
while(len(appended_str) != 0):  # creating list
    inp_req = input()
    appended_str = str(inp_req)
    if (len(appended_str) == 0):
        break
    grocery_list.append(appended_str)

for item in grocery_list:       # creating dict with amount of each item
    if (item in grocery_dict) == True:
        grocery_dict[item] += 1
    elif (item in grocery_dict) == False:
        grocery_dict[item] = 1
print(grocery_dict)


def get_key(d, value):  # func to get key of dict element by its value
    for k, v in d.items():
        if v == value:
            return k


def del_most_freq_el(d):  # func to delete the element with the biggest amount
    tmp = 0
    for val in grocery_dict.values():
        if tmp < val:
            tmp = val
    del grocery_dict[get_key(grocery_dict, tmp)]


del_most_freq_el(grocery_dict)
print(grocery_dict)
