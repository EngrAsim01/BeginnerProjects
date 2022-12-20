

a = int(input('Numerator of first fraction: '))
b = int(input('Denumerator of first fraction: '))
print(f'Your first fraction is: {a}/{b}')

c = int(input('Numerator of second fraction: '))
d = int(input('Denumerator of second fraction: '))
print(f'Your second fraction is: {c}/{d}')

e = a*d
f = b*c

if e>f:
    print(f'First fraction is greater than second.')
elif f>e:
    print(f'Second fraction is greater than first.')

print(f'First fraction is: {a/b} and Second fraction is: {c/d}')