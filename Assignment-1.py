#Assignment-1

#I.	String Methods
#upper
text = "hello"
print("upper:", text.upper())

# replace
text = "hello world"
print("replace:", text.replace("world", "Python"))

# split
text = "apple,banana,grape"
print("split:", text.split(","))

#II.	List Methods
# append
fruits = ["apple", "banana"]
fruits.append("orange")
print("append:", fruits)

# remove
numbers = [1, 2, 3, 4]
numbers.remove(3)
print("remove:", numbers)

# sort
nums = [5, 2, 9, 1]
nums.sort()
print("sort:", nums)



#III.	Tuple Methods
# append
fruits = ["apple", "banana"]
fruits.append("orange")
print("append:", fruits)

# remove
numbers = [1, 2, 3, 4]
numbers.remove(3)
print("remove:", numbers)

# sort
nums = [5, 2, 9, 1]
nums.sort()
print("sort:", nums)


#IV.	Set Methods
# add
s = {1, 2, 3}
s.add(4)
print("add:", s)

# remove
s = {1, 2, 3}
s.remove(2)
print("remove:", s)

# union
a = {1, 2}
b = {2, 3}
print("union:", a.union(b))


#V.	Dictionary Methods
# get
d = {"name": "Shleshma", "age": 25}
print("get:", d.get("name"))

# keys
d = {"x": 10, "y": 20}
print("keys:", d.keys())


# update
d = {"a": 1}
d.update({"b": 2})
print("update:", d)
