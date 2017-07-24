student = {'name': 'John', 'age': '25', 'courses': ['Math', 'CompSci']}
# Basic methods
# -----------------------------------------------------------------------
print("Whole dictionary: {}".format(student))  # print whole dictionary
print("Dictionary keys: {}".format(student.keys()))  # print keys
print("Number of keys: {}".format(len(student))) #
print("Items of dictionary: {}".format(student.items()))

for key, value in student.items():
    print("Key is ({}) and value is ({}).".format(key, value))
# -----------------------------------------------------------------------

# 1. Printing key(s):
print(student['name'])  # simple print (throws error if key does not exist)
print(student.get('name'))  # print using get() method (does not throw error)
print(student.get('phone', 'Not found in keys.'))  # default value when key does not exist

# -----------------------------------------------------------------------

# 2. Adding key into existing dictionary:
student['phone'] = '5564-65-221'  # adding key and value
print(student)
print(student.get('phone', 'Not found in keys.'))

# -----------------------------------------------------------------------

# 3. Updating value:
student['name'] = 'Jane'  # update value for provided key
print(student)  # 'John' changed into 'Jane'
student.update({'name': 'George', 'age': 26, 'phone': '445-785-124'})
print(student)  # update more than one key

# -----------------------------------------------------------------------

# 4. Delete key and value:
del student['age']  # delete key 'age' and its' value
print(student)  # dictionary without 'age' key
phone_deleted = student.pop('phone')  # delete using pop method
print(student)  #
print(phone_deleted)  #
