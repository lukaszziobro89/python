# LISTS
courses = ['history', 'math', 'physics', 'compsci']
courses_2 = ['Gym', 'Philosophy']
courses_3 = ['Geography', 'Chemistry']
courses_4 = ['Politics', 'Economics']
nums = [3, 5, 1, 8]
nums_2 = [12, 1, 9, 4]
nums_3 = [100, 56, 123, 12, 77, 111]

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
# -----------------------------------------------------------------------

# 4. Removing element from list
courses_3.remove('Politics')
print("4. List with removed element: " + str(courses_3))
# -----------------------------------------------------------------------

# 5. Removing last element of list - pop() returns value that it removes
popped = courses_3.pop()
print("5. Popped list: {} - Popped element: {}".format(str(courses_3), str(popped)))
# -----------------------------------------------------------------------

# 6. Reversed list:
print("6. -- Original list: " + str(courses))
courses.reverse()
print("6. -- Reversed list: " + str(courses))
# -----------------------------------------------------------------------

# 7. Sorting method (ALTERING ORIGINAL LIST)
print("7. -- Original numbers list: " + str(nums))
nums.sort()
print("7. -- Sorted numbers list (altered): " + str(nums))
nums.sort(reverse=True)
print("7. -- Reversed numbers list sort (altered): " + str(nums))
# -----------------------------------------------------------------------

# 7a. Sorting function (WITHOUT ALTERING ORIGINAL LIST - makes new variable with sorted list)
print("7a. -- Original list : " + str(nums_3))
sorted_list = sorted(nums_3)
print("7a. -- Sorted list (not altered): " + str(sorted_list)) # here new variable with sorted list is created
reversed_sorted_list = sorted(nums_3, reverse=True)
print("7a. -- Sorted reversed list (not altered): " + str(reversed_sorted_list)) # here new variable with sorted list is created
# -----------------------------------------------------------------------

# 8. Searching using index() method
print("8. Original list is: " + str(courses))
english_index = courses.index('English')
print("8. Element 'English' is in list under index: " + str(english_index))
# -----------------------------------------------------------------------

# 9. Checking if element is in the list:
print("9. Original list is: " + str(courses))
art_check = 'Art' in courses
literature_check = 'Literature' in courses
print("9. Checks for elements in courses: 'Art' ({}) - 'Literature' ({}).".format(art_check, literature_check))