# LISTS
courses = ['history', 'math', 'physics', 'compsci']
courses_2 = ['Gym', 'Philosophy']
courses_3 = ['Geography', 'Chemistry']
courses_4 = ['Politics', 'Economics']
nums = [3, 5, 1, 8]

# General methods
print("List of courses: {}. Number of courses: {}".format(courses, len(courses)))
print("First course is {} and last course is {}.".format(courses[0], courses[-1]))
# -----------------------------------------------------------------------

# 1. Appending into list (simple add to the end)
courses.append('Art')
print("1. After append: " + str(courses))
# ['history', 'math', 'physics', 'compsci', 'Art']
# -----------------------------------------------------------------------

# 2. Insert into list (put index where you want to insert)
courses.insert(1, "English")
print("2. After insert: " + str(courses))
# ['history', 'English', 'math', 'physics', 'compsci', 'Art']
# -----------------------------------------------------------------------

# 2a. Insert list into other list
courses.insert(0, courses_2)
print("2a. List within other list: " + str(courses))
# [['Gym', 'Philosophy'], 'history', 'English', 'math', 'physics', 'compsci', 'Art']
# -----------------------------------------------------------------------

# 3. Extend one list with another (final effect is one list)
courses_3.extend(courses_4)
print("3. Extending list with elements of other: " + str(courses_3))

# 4. Removing element from list
courses_3.remove('Politics')
print("4. List with removed element: " + str(courses_3))

# 5. Removing last element of list - pop() returns value that it removes
popped = courses_3.pop()
print("5. Popped list: {} - Popped element: {}".format(str(courses_3), str(popped)))

# 6. Reversed list:
print(" -- Original list: " + str(courses))
courses.reverse()
print(" -- Reversed list: " + str(courses))





