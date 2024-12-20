my_dict = {"Andrys" : 1963, "Irina" : 1973, "Anton" : 2010}
print(my_dict)
print(my_dict.get("Andrys"))
print(my_dict.get("Anna"))
my_dict.update({"Sasha":1980, "Wasja": 2000})
print(my_dict)
del my_dict["Wasja"]
print(my_dict)
my_set = {1,2,"Oring",4,5,2,4,1}
print(my_set)
print(my_set.add("Patsh"))
print(my_set.add(7))
print(my_set)
print(my_set.remove(2))
print(my_set)