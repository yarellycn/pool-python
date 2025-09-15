from functools import reduce

student = {
    "name": "Kida",
    "academic_year": 1,
    "units": [
        {"name": "Web Development", "credits": 4, "grade":"A"},
        {"name": "Network and System Administration", "credits": 3, "grade":"C"},
        {"name": "Java", "credits": 2, "grade":"E"},
    ]
}

grade_weigh_mapping = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "E": 0,
}

# total_credits=0
# for unit in student["units"]:
#     total_credits += unit["credits"]
# student["total_credits"] = total_credits

credits = list(map(lambda x: x["credits"], student["units"]))
student["total_credits"] = reduce(lambda x, y: x+y, credits)
grades = list(map(lambda x: x["grade"], student["units"]))
gradeweigh = list(map(lambda x: grade_weigh_mapping[x], grades))
print(gradeweigh)
multip_grd_crd = list(map(lambda x: x[0]*x[1], [*zip(gradeweigh, credits)]))
print(multip_grd_crd)
student["GPA"] = (reduce(lambda x, y: x+y, multip_grd_crd))/student["total_credits"]

# grades=["A", "B", "C", "E"]
# grades=list(map(lambda x: {"grade": grade_weigh_mapping[x]}, grades))
# print(grades)

students = [
    {
    "name": "Ariel",
    "academic_year": 1,
    "units": [
        {"name": "Web Development", "credits": 4, "grade":"B"},
        {"name": "Network and System Administration", "credits": 3, "grade":"D"},
        {"name": "Java", "credits": 2, "grade":"C"},
        ]
    },
    {
    "name": "Vaiana",
    "academic_year": 1,
    "units": [
        {"name": "Web Development", "credits": 4, "grade":"A"},
        {"name": "Network and System Administration", "credits": 3, "grade":"B"},
        {"name": "Java", "credits": 2, "grade":"E"},
        ]
    },
    {
    "name": "Lilo",
    "academic_year": 1,
    "units": [
        {"name": "Web Development", "credits": 4, "grade":"C"},
        {"name": "Network and System Administration", "credits": 3, "grade":"D"},
        {"name": "Java", "credits": 2, "grade":"B"},
        ]
    },
]

#METHOD 1

for x in students:
    credits = list(map(lambda x: x["credits"], student["units"]))
    student["total_credits"] = reduce(lambda x, y: x+y, credits)
    grades = list(map(lambda x: x["grade"], student["units"]))
    gradeweigh = list(map(lambda x: grade_weigh_mapping[x], grades))
    multip_grd_crd = list(map(lambda x: x[0]*x[1], [*zip(gradeweigh, credits)]))
    student["GPA"] = (reduce(lambda x, y: x+y, multip_grd_crd))/student["total_credits"]

#METHOD 2

# def fill_student(student: dict):
#     credits = list(map(lambda x: x["credits"], student["units"]))
#     student["total_credits"] = reduce(lambda x, y: x+y, credits)
#     grades = list(map(lambda x: x["grade"], student["units"]))
#     gradeweigh = list(map(lambda x: grade_weigh_mapping[x], grades))
#     multip_grd_crd = list(map(lambda x: x[0]*x[1], [*zip(gradeweigh, credits)]))
#     student["GPA"] = (reduce(lambda x, y: x+y, multip_grd_crd))/student["total_credits"]
#     return student

# students = list(map(fill_student, students))


