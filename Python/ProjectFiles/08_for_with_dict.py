classroom = {
    'teacher': 'kim',
    'student1': 'hong',
    'student2': 'choi'
}

for member in classroom:
    print(member) # key가 나옴!!

for member in classroom:
    print(classroom[member]) # value 나옴!!
# ---> 이렇게 뽑지 않음
# ------------- 위는 권장 안함!!! --------------

# dict.values --> list 형태였음.
print('더 명확함----------')
# 더명확함!! keys
print('keys!!')
for member in classroom.keys():
    print(member) # key 나옴!!
# 더명확함!! values
print('values!!')
for member in classroom.values():
    print(member) # value 나옴!!
    print(type(member))

print('----------key, value-------------')
for key, value in classroom.items():
    print(key)
    print(value)
    print(type(key))
    print(type(value))

