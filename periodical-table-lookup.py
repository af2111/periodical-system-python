import json

def element_to_string(element: dict):
    out = ""
    for key in element.keys(): 
        out += f"\n{key.capitalize()}: {element[key]}"
    return out

table_file = open("periodical-table.json", "r")
table_json: dict = json.load(table_file)
order_num = input("what's the order number of your element OR search by element name").lower()
try:
    order_num = int(order_num)
    if order_num <= 0:
        print("that's too low.")
        exit()
    try:
        element_name: list = table_json["order"][order_num]
        elem_string = element_to_string(table_json[element_name])
        print(elem_string)
    except IndexError:
        print("that element doesnt exist loser")
except ValueError:
    try:
        elem_name = table_json[order_num]
        elem_string = element_to_string(elem_name)
        print(elem_string)
    except KeyError:
        print("that element doesnt exist loser")