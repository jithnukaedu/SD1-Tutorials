#Convert a mark to a grade: 
def convertMark(mark): 
    if mark >= 70: 
        grade = 'First' 
    elif mark >= 60: 
        grade = '2:1' 
    elif mark >= 50: 
        grade = '2:2' 
    elif mark >= 40: 
        grade = 'Third' 
    else: 
        grade = 'Fail'   
    return grade 

grade1 = convertMark(75) 
print(grade1) 
grade2 = convertMark(42) 
print(grade2) 
print(convertMark(55))  #call & print in one statement
