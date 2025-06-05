class Student:
    # constructor
    # initialise instance variable

    def __init__(self, name):
        print('Inside the constructor...')
        self.name = name
        print('The variable name is initialised...')

    # instance Method
    def show(self):
        print('The next line was created by an instance Method')
        print('\nHello, my name is', self.name+ '.')

# create object using constructor 
s1 = Student('Florence')
s1.show()
