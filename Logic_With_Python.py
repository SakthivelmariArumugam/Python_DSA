#Check Even Number In list

num_list=[1,2,3,4,5]
def check_even(num_list):
    for number in num_list:
        if number%2==0:
            return True
        else:
            pass

print(check_even(num_list))

#tuple UnPacking In The list

tup_list=[("Goog",200),("Msft",300),("App",500)]

for item in tup_list:
    print(item)

for com,pri in tup_list:
    print(com)
    print(pri)
    
#Employee Of The Month
Employee_List=[("Arun",100),("Karthi",59),("Vinoth",105)]

def Employee_Month(Employee_List):
    current_max=0 
    Employee=""
    for employ,time in (Employee_List):
        if time>current_max:
            current_max=time
            Employee=employ
    return (Employee,time)

print(Employee_Month(Employee_List))
