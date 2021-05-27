### To find the the names with letter "a" in the dictionary data type ###
names = {
    "male":["Sundar","Bala"],
    "female":["Viji", "Lakshmi"]
    }
for key in names.keys():  ### this will iterate the keys
    for values in names[key]:  ### this will iterate the value of each key
        if "i" in values:       ### checks condition if the value has "i" in it
            print(values)