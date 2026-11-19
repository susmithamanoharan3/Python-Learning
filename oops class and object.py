## 1
# class Demo():
#     pass
# obj1=Demo()
# obj2=Demo()
# print(type(obj1))

### 2
# class Demo():
#     a=10
#     b=20
# obj1=Demo()
# print(Demo.a)
# print(obj1.a)
# print(obj1.b)

## 3
# class School:
#     sname="Vidhyanikethan"
#     sprinci="seethamma"
#     sloc="Tumkur"
# st1=School()
# st2=School()
# print(School.sname)
# print(School.sprinci)
# print(st1.sname,st1.sprinci,st1.sloc)
# print(st2.sname,st2.sprinci,st2.sloc)

### 4
# class School:
#     sname="Vidhyanikethan"
#     sprinci="seethamma"
#     loc="Tumkur"

# st1=School()
# st1.name="Deepak"
# st1.bgrp='B+ve'
# st1.phno=9090909090

# st2=School()
# st2.name="Jassie"
# st2.bgrp='A+ve'
# st2.phno=9191919191
# print(School.sname)
# print(School.sprinci)
# print(st1.sname,st1.sprinci,st1.sloc)
# print(st2.sname,st2.sprinci,st2.sloc)
# print(st1.name,st2.name)
#print(School.name)  ### type object 'School' has no attribute 'name'. Did you mean: 'sname'?

## 5
# class School:
#     sname="Vidhyanikethan"
#     sprinci="seethamma"
#     sloc="Tumkur"
# st1=School()
# st1.name="Deepak"
# st1.bgrp='B+ve'
# st1.phno=9090909090
# st2=School()
# st2.name="Jassie"
# st2.bgrp='A+ve'
# st2.phno=9191919191
# print(School.sname,School.sprinci)
# print(st1.sname,st1.sprinci,st1.sloc)
# print(st2.sname,st2.sprinci,st2.sloc)
# print(st1.name,st2.name)
# School.sprinci="Ramayya"
# print(School.sprinci)
# print(st1.sname,st1.sprinci,st1.sloc)
# print(st2.sname,st2.sprinci,st2.sloc)
# st1.sname="Qspiders"
# print(School.sname)
# print(st1.sname,st1.sprinci,st1.sloc)
# print(st2.sname,st2.sprinci,st2.sloc)

## 6
# class Bank:
#     Bank_name="SBI"
#     Bank_ifsc="SBIN0033"
#     Bank_loc="Jayanagar"
#     Bank_website="ww.sbi.com"

# cst1=Bank()
# cst1.name="Ranga"
# cst1.bgrp="B+ve"
# cst1.adress="Mathikere"

# cst2=Bank()
# cst2.name="Manga"
# cst2.bgrp="A+ve"
# cst2.adress="Mahalakshimi layout"

# print(Bank.Bank_name,Bank.Bank_loc,Bank.Bank_ifsc,Bank.Bank_website)
# print(cst1.name,cst1.bgrp,cst1.adress)
# cst1.adress="mahakavi kuvempu"
# print(cst1.adress)


# ### 7
# class Bank:
#     Bank_name="SBI"
#     Bank_ifsc="SBIN0033"
#     Bank_loc="Jayanagar"
#     Bank_website="ww.sbi.com"

# cst1=Bank()
# cst2=Bank()
# def sam(obj,name,bgrp,adrs,bal):
#     obj.name=name
#     obj.bgrp=bgrp
#     obj.adrs=adrs
#     obj.bal=bal
# sam(cst1,"Langa","O+ve","peelamedu",90000)
# print(cst1.name,cst1.bgrp,cst1.adrs,cst1.bal)

# ##  8

# class Bank:
#     Bank_name = "SBI"
#     Bank_ifsc = "SBIN0033"
#     Bank_loc = "Jayanagar"
#     Bank_website = "www.sbi.com"
#     def sam(self, name, bgrp, adrs, bal):
#         self.name = name
#         self.bgrp = bgrp
#         self.adrs = adrs
#         self.bal = bal
# cst1 = Bank()
# cst2 = Bank()
# cst1.sam("jaya", "O-ve", "ukkadam", 6000)
# cst2.sam("priya", "AB+ve", "Erode", 40000)
# print(cst1.name, cst1.bgrp, cst1.adrs, cst1.bal)
# print(cst2.name, cst2.bgrp, cst2.adrs, cst2.bal)

# ##

# #constructor __init__

# #constructor __init__

class Bank:
    Bank_name="SBI"
    Bank_ifsc="SBIN0033"
    Bank_loc="Jayanagar"
    Bank_website="www.sbi.com"

    def __init__(self,name,bgrp,adrs,bal):
        self.name=name
        self.bgrp=bgrp
        self.adrs=adrs
        self.bal=bal

cst1=Bank("Aaa","B+ve","Tirrupur",15000)
cst2=Bank("oooo","B-ve","Salem",200000)
print(cst1.name,cst1.bgrp,cst1.adrs,cst1.bal)
print(cst2.name,cst2.bgrp,cst2.adrs,cst2.bal)



###
#constructor __init__

# class Company:
#   Company_name="CMT"
#   Company_ifsc="SBIN0033"
#   Company_loc="Jayanagar"
  

# def __init__(self,name,bgrp,adrs,bal):
#     self.name=name
#     self.bgrp=bgrp
#     self.adrs=adrs
#     self.bal=bal

# cst1=Company("Aaa","B+ve","Tirrupur",15000)
# cst2=Company("oooo","B-ve","Salem",200000)
# print(cst1.name,cst1.bgrp,cst1.adrs,cst1.bal)
# print(cst2.name,cst2.bgrp,cst2.adrs,cst2.bal)