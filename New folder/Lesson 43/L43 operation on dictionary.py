dic1 = {}

#dictionary with integer keys
dict1 = {1: "apple",
         2: "ball"
         }

#dictionary with mixed keys
dict2 = {"name": "John",
         1: [2,4,3]
         }

#dictionay with string keys
dict3 = {"name": "Jack",
         "age": 26,
         "phone": 123455
         }

#getting the data
print(dict3["name"])
print(dict3.get("age"))
print()

#update value
print("updated dictionary 3:")
dict3["age"] = 27
print(dict3)
print()

#remove particular element
dict3.pop("age")
print("updated dictionary 3 after removing age:")
print(dict3)
print()

#add item
dict3["address"] = "Guyana"
print(dict3)
print()