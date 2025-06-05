class Person:
    def __init__(self, name, gender, profession):
        # data members (instance variables)
        self.name = name
        self.gender = gender
        self.profession = profession

    # Behaviour (instance methods)
    def show(self):
        print('Name:', self.name, '\nGender: ', self.gender, '\nProfession: ', self.profession, '\n')

    # Behaviour (instance methods)
    def work(self):
        print(self.name, 'is working as a', self.profession)

# create object of a class (object is outside of class)
jessa = Person ('Jessa', 'Female', 'Software Engineer')

# call methods SHOW and WORK
jessa.show()
jessa.work()
