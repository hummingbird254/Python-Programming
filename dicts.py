myDict = {"Name": "Anne", "Age": 24}
myDict0 = dict(name="Tom", age=50, gender="Male")

print(myDict0)
value = myDict["Age"]
print(value)

del myDict0["age"]
print(myDict0)

if "Age" in myDict:
    print(myDict["Name"])

myDict["Gender"] = "Female"
print(myDict)

for keys in myDict.keys():
    print(keys)

for values in myDict.values():
    print(values)

for keys, values in myDict0.items():
    print(keys, values)

myDict.update(dict(Name="Martha"))
print(myDict)
