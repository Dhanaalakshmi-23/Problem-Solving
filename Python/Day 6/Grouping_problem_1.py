#1. Group students based on marks range and find topper in each group.
# sample input :
# {
#  "Arun": 85,
#  "Bala": 72,
#  "Charan": 91,
#  "Divya": 67,
#  "Esha": 78,
#  "Farhan": 95
# }

# output :
# {
#  '80-100': ['Arun', 'Charan', 'Farhan'],
#  '60-79': ['Bala', 'Divya', 'Esha']
# }

# topper in 80-100 : Farhan
# topper in 60-79 : Esha

def groupStudents(studentMarks):
    groups = {
        "80-100": [],
        "60-79": []
    }
    
    toppers = {}
    
    for name in studentMarks:
        marks = studentMarks[name]
        
        if marks >= 80:
            groups["80-100"].append(name)
        elif marks >= 60:
            groups["60-79"].append(name)
    
    max1 = -1
    topper1 = ""
    
    for name in groups["80-100"]:
        if studentMarks[name] > max1:
            max1 = studentMarks[name]
            topper1 = name
    
    toppers["80-100"] = topper1
    
    max2 = -1
    topper2 = ""
    
    for name in groups["60-79"]:
        if studentMarks[name] > max2:
            max2 = studentMarks[name]
            topper2 = name
    
    toppers["60-79"] = topper2
    
    print(groups)
    
    for key in toppers:
        print("topper in", key, ":", toppers[key])


students = {
    "Arun": 85,
    "Bala": 72,
    "Charan": 91,
    "Divya": 67,
    "Esha": 78,
    "Farhan": 95
}

groupStudents(students)