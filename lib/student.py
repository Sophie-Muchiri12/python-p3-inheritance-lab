#!/usr/bin/env python

from user import User

class Student(User):

    knowledge = []

    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.knowledge = Student.knowledge
    
    def learn(self,otherknowledge):

        if isinstance(otherknowledge,str):
            self.knowledge.append(otherknowledge)

        else:
            print("error")
    
        






student1 = Student('sophie','muchiri')
student1.learn(['read'])