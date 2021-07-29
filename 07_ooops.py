# class RailwayForm:
#     formtype = "RailwayFrom"
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.train}")
    
# ayushappication = RailwayForm()
# ayushappication.name = "Ayush Kumar"
# ayushappication.train = "Rapti sager"
# ayushappication.printData()

# #above line get converted to below given line that is way we need to pass self in class funtion definition
# RailwayForm.printData(ayushappication)

# class Employee:
#     companyName = "Qualcomm"

#     def __init__(self,name,salary,subunit) -> None:
#         self.name = name
#         self.salary = salary
#         self.subunit = subunit
#         print("Employee is created")

#     def printDetail(self):
#         print(f"employee name is {self.name}")
#         print(f"Employee salary is {self.salary}")
#         print(f"Employee subunit is {self.subunit}")

#     def printSalary(self,sign):
#         print(f"Salary of {self.name} of company {self.companyName} is {self.salary}\n{sign}")
    
#     @staticmethod
#     def greet():
#         print("hello sir, good Morning")

#     @classmethod
#     def changeComName(cls,cName):
#         cls.companyName = cName
    
# ayush = Employee("ayush",100,"lint.team")
# print(Employee.companyName)
# # ayush.name = "Ayush Kumar"
# # ayush.salary = "100K"
# #ayush.printSalary("Thanks")         #Employee.printSalary(ayush)
# #ayush.greet()                       #Employee.greet()

# ayush.printDetail()
# ayush.changeComName("Qualcomm pvt. ltd.")
# print(ayush.companyName)

# use of @property

# class Employee:
#     companyName = "Bharat Gas"
#     salary = 4500
#     salaryBonus = 400

#     @property
#     def totalSalary(self):
#         return self.salary+ self.salaryBonus

#     @totalSalary.setter
#     def totalSalary(self,val):
#         self.salaryBonus = val - self.salary

#     @classmethod
#     def changeBonus(cls,newBonus):
#         cls.salaryBonus = newBonus
    
# e = Employee()
# print(e.totalSalary)
# # Employee.changeBonus(500)
# # print(e.totalSalary)

# e.totalSalary =4800
# print(e.salary)
# print(e.salaryBonus)

#operator overloading

# class Number:
#     def __init__(self,num):
#         self.num = num

#     def __add__(self,num2):
#         return self.num + num2.num
    
#     def __mul__(self,num2):
#         return self.num * num2.num

#     def __str__(self):
#         return f"decimal number : {self.num}"
    
#     def __len__(self):
#         return 1
    
# n1 = Number(3)
# n2 = Number(4)
# sum = n1+n2
# mul = n1*n2
# print(sum)
# print(mul)

# print(n1)
# print(len(n1))


'''
 problem 1 : create a class C2Dvec and create another class C3Dvec using 2Dvec
'''
# class C2Dvec:
#     def __init__(self,i,j) :
#         self.icap = i
#         self.jcap = j
#     def __str__(self) -> str:
#         return f"{self.icap}i + {self.jcap}j"

# class C3Dvec(C2Dvec):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.kcap = k
#     def __str__(self) -> str:
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

# v2d = C2Dvec(3,4)
# v3d = C3Dvec(3,5,7)
# print(v2d)
# print(v3d)

'''
problem 2 - add and multiple two complex number
'''
# class Complex:
#     def __init__(self,r,i):
#         self.real = r
#         self.imaginary = i
#     def __add__(self,c2):
#         return Complex(self.real+c2.real , self.imaginary + c2.imaginary)
#     def __mul__(self,c2):
#         mulReal = self.real*c2.real - self.imaginary*c2.imaginary
#         mulImg = self.real*c2.imaginary + self.imaginary*c2.real
#         return Complex(mulReal,mulImg)
#     def __str__(self) -> str:
#         if self.imaginary < 0:
#             return f"{self.real} - {-self.imaginary}i"
#         else: return f"{self.real} + {self.imaginary}i"

# c1 = Complex(2,3)
# c2 = Complex(3,4)

# c3 = c1+c2
# print(c3)
# c4 = c1*c2
# print(c4)

'''
problem 3 - create a vector class and add, multiply vectors
'''

class Vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"a{index} -> {i} , "
            index += 1
        return str1[:-2]
    def __add__(self,vec2):
        l = []
        for i in range(len(self.vec)):
            l.append(self.vec[i] + vec2.vec[i])
        return Vector(l)
    def __mul__(self,vec2):
        sum = 0 
        for i in range(len(self.vec)):
            sum += (self.vec[i]*vec2.vec[i])
        return sum

v1 = Vector([3,4,6,7])
v2 = Vector([8,9,7,6])

print(v1+v2)
print(v1*v2)
