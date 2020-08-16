class student(object):
    __city="patna"
    def __init__(self,name,email,roll,father_name):
        self.name=name
        self._roll=roll
        self.email=email
        self.__father_name=father_name
    def __str__(self):
        return "{},{},{}".format(self.name,self.roll,self.email)
    def __gat_father_name(self):
        return self.__father_name
    def get_fname(self):
        return self.__gat_father_name(),self.__city


class school_employee(student):
    def __init__(self,name,email,emp_id):
        super().__init__(name, email,roll=None,father_name=None)
        self.emp_id=emp_id
    def __str__(self):
        return "name: {},email: {},emp_id: {}".format(self.name, self.email,self.emp_id)





stu1=student("jainendra","jain@gmail.com","17","sid")
print(stu1.__dict__)
print(stu1.get_fname())
stu1.get_fname()

emp1=school_employee("bhanu","bhanu@gmail.com","2020123")
print (emp1.__dict__)
print(emp1._roll)

