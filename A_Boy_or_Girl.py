user_name =input()

duplicate= set()
for i in user_name:
    duplicate.add(i)

if len(duplicate) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")