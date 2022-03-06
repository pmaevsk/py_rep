grocery_list = []
grocery_dict = {}
appended_str = 'tmp'
while(len(appended_str) != 0):  # creating list
    # inp_req = input()
    appended_str = input()
    if (len(appended_str) == 0):
        break
    grocery_list.append(appended_str)

for item in grocery_list:       # creating dict with amount of each item
    if item in grocery_dict:
        grocery_dict[item] += 1
    else:
        grocery_dict[item] = 1
print(grocery_dict)


def get_key(d, value):  # func to get key of dict element by its value
    for k, v in d.items():
        if v == value:
            return k


def del_most_freq_el(d):  # func to delete the element with the biggest amount
    del d[get_key(d, max(d.values()))]


del_most_freq_el(grocery_dict)
print(grocery_dict)
