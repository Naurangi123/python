# Encapsulation

# class Student:
#     def __init__(self,name,roll_number):
#         self._name=name
#         self._roll_number=roll_number
        
#     def get_name(self):
#         return self.name
    
#     def set_name(self,name):
#         self.name=name
        
#     def get_roll_number(self):
#         return self.roll_number
    
#     def set_roll_number(self,roll_number):
#         self.roll_number=roll_number
        
# student1=Student("Naurangi",100074)
# print(student1.get_name(),student1.get_roll_number())

# student1.set_name("Naurangi Lal")
# print(student1.get_name())


# Inheritance

class Person:
    def __init__(self,name):
        self._name=name
        
    def get_name(self):
        return self._name
    
    def set_name(self,name):
        self._name=name
        
    
class Student(Person):
    def __init__(self, name,roll_number):
        super().__init__(name)
        self._roll_number=roll_number
        
    def get_roll_number(self):
        return self._roll_number
    
    def set_roll_number(self, roll_number):
        self._roll_number=roll_number
        
        
student=Student("Naurangi",100074)
print(student.get_name(),student.get_roll_number())

    