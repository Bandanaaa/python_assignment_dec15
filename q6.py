def func():
    return ("Hello", 45, 23.3)


temp=func()

x,y,z=temp

print('The function returned the following:\n'+x, y, z, sep='\n')