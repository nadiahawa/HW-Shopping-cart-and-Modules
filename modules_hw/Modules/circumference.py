def circumference_circle():
    radius = float(input('please enter the radius as a numerical value and as a decimal: '))
    pi = 3.14
    #2*(3.14*r**2)
    return 2*pi*radius**2

print(f'The circumference of your circle is about = {circumference_circle()} ')