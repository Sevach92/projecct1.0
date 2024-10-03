grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo','Steve', 'Khendrik', 'Aaron'}
Aaron_grades = sum(grades[0])/len(grades[0])
Bilbo_graades = sum(grades[1])/len(grades[1])
Johnny_grades = sum(grades[2])/len(grades[2])
Khendrik_grades = sum(grades[3])/len(grades[3])
Steve_grades = sum(grades[4])/len(grades[4])
grades = Aaron_grades, Bilbo_graades, Johnny_grades, Khendrik_grades, Steve_grades
students = list(students)
students = sorted(students)
average_grades = {}
for i in range(len(grades)):
    average_grades[students[i]] = grades[i]
print(average_grades)
