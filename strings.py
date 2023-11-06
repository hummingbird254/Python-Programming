var = 9
print("I got %d  cousins." % var)
print(f"I got {var} cousins. ")  # best option
print("i got {0} cousins.".format(var))

message = "Hello World"
mList = []
for x in message:
    mList.append(x)
print(mList)

mList0 = list(message.strip())

print(mList0)

message1 = "".join(mList0)
print(message1)

if "Hel" in message:
    print("Yes")

print(message.replace("World", "Universe"))

print(message.startswith("Hello"))
print(message.endswith("Universe"))

print(message.find("W"))  # returns index
