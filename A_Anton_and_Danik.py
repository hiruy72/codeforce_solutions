from collections import Counter
n= int(input())
s = input()

count = Counter(s)

if count['A'] > count['D']:
    print('Anton')
elif count['A'] < count['D']:
    print('Danik')
else:
    print('Friendship')