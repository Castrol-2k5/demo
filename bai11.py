it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle',
'Amazon'}
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
t=0
for i in a:
    if i in b: b.remove(i)
print(b)
