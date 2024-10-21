num_fails = 2
spanish_grade = 7
maths_grade = 3

promote = False

if num_fails <= 2:
    if spanish_grade < 5 and maths_grade < 5:
        promote = False
    else:
        promote = True
else:
    promote = False
    
if promote:
    print("Pasa de curso")
    
else:print("No pasa de curso")