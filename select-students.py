def select_student(students, threshold):
    accepted = list(filter(lambda x: x[1] >= threshold, students))
    accepted.sort(key=lambda x: x[1], reverse=True) #descending

    refused = list(filter(lambda x: x[1] < threshold, students))
    refused.sort(key=lambda x: x[1]) #ascending

    d = {"Accepted": accepted, "Refused": refused}
    return d


my_class = [
    ["Kermit Wade", 27],
    ["Hattie Schleusner", 67],
    ["Ben Ball", 5],
    ["William Lee", 2],
]

res = select_student(my_class, 20)
print(res)
# {'Accepted': [['Hattie Schleusner', 67], ['Kermit Wade', 27]],
#  'Refused': [['William Lee', 2], ['Ben Ball', 5]]}

res = select_student(my_class, 50)
print(res)
# {'Accepted': [['Hattie Schleusner', 67]],
#  'Refused': [['William Lee', 2], ['Ben Ball', 5], ['Kermit Wade', 27]]}
