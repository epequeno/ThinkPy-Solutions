x = int(raw_input('x?\n'))
y = int(raw_input('y?\n'))
z = int(raw_input('z?\n'))

def is_between(x, y, z):
    return x <= y and y <= z

a = is_between(x, y, z)
if a:
    print 'y is between x and z!'
else:
    print 'y is not between x and z!'

