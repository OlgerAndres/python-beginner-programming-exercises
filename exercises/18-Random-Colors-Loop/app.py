import random

def get_color(color_number=2):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():

    example_color = 1
    students_array = []
    #your loop here
    for students_array in range(10):
        get_color = random.randint(1,4)






print(get_color())
print(get_allStudentColors())