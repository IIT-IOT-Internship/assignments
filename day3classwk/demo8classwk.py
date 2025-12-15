# dict
#   - data is stored in key value pairs
#   - not indexed
#   - ordered
#   - mutable
#   d = {'k1':v1, 'k2':v2, ....}
#   d = {} or dict()    --> empty dict

student = {'name':'abc', 'rollno':12, 'std':8, 'marks':89.5}

print(f"type(student) = {type(student)} ")
print(f"len(studnet) = {len(student)}")
print(f"student = {student}")

print(f"name = {student['name']}" )
print(f"rollno = {student['rollno']}" )
print(f"std = {student['std']}" )
print(f"marks = {student['marks']}" )
