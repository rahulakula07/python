# Convert Array to Object
#       [["name", "Alice"], ["age", 25]] → {name: "Alice", age: 25}
# Write a function that converts an array of key-value pairs into an object.
# without using methods 
obj=input("enter")
obj=eval(obj)
res={}
for keys,values in obj:
    res[keys]=values
print(res)
# # op
# enter:[["name", "Alice"], ["age", 25]]
# {'name': 'Alice', 'age': 25}
# with using methods
obj=input("enter:")
obj=eval(obj)
print(dict(obj))
# # op
# enter:[["name", "Alice"], ["age", 25]]
# {'name': 'Alice', 'age': 25}
##############################################################################################
# Merge Two Objects
#       {a: 1, b: 2}, {b: 3, c: 4} → {a: 1, b: 3, c: 4}
# Write a function that merges two objects, giving priority to the properties of the second object in case of conflict.

obj1=input("enter:")
obj2=input("enter:")
obj1,obj2=eval(obj1),eval(obj2)
obj1=eval(obj1)
print({**obj1,**obj2})
# op 
# enter:{"b": 3, "c": 4}
# enter:{"a": 1, "b": 2}
# {'b': 2, 'c': 4, 'a': 1}

obj1=input("enter:")
obj2=input("enter:")
obj1,obj2=eval(obj1),eval(obj2)
res=obj1.copy()
res.update(obj2)
print(res)

# op 
# enter:{"b": 3, "c": 4}
# enter:{"a": 1, "b": 2}
# {'b': 2, 'c': 4, 'a': 1}

obj1=input("enter:")
obj2=input("enter:")
obj1,obj2=eval(obj1),eval(obj2)
res=obj1.copy()
for key,value in obj2.items():
    res[key]=value
print(res)
# op 
# enter:{"b": 3, "c": 4}
# enter:{"a": 1, "b": 2}
# {'b': 2, 'c': 4, 'a': 1}
#############################################################################################################