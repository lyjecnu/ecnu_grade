import matplotlib.pyplot as plt
import numpy as np
from grade import fdata
import input
import copy


def check(obj):
    num_tuple = 0
    tuple_key = None
    
    for key,value in obj.__dict__.items():
        if type(value) == tuple:
            num_tuple = num_tuple + 1
            tuple_key = key
            
    if num_tuple > 1:
        return -1
    
    return tuple_key

def update(obj):
    obj.stu_std_mean = obj.test_std * obj.property

                


sum_initial = {
        '3.9+':0,
        '3.8+':0,
        '3.7+':0,
        '3.6+':0,
        '3.5+':0,
        '3.4+':0,
        '3.3+':0,
        '3.2+':0,
        '3.1+':0,
        '3.0+':0,
    }

sum = copy.deepcopy(sum_initial)
p = copy.deepcopy(input.params)    

epochs = 1000

#print(check(input.params))

key = check(p)
if key == -1:
    print("error")
else:
    tup = getattr(p,key)
    array = np.arange(*tup)
    sum = copy.deepcopy(sum_initial)
    for num in array:
        
        print(num)
        setattr(p,key,num)
        update(p)    #可选
        print(p.students,end=" ")
        print(p.tests,end=' ')
        print(p.test_mean,end=' ')
        print(p.test_std,end=' ')
        print(p.stu_std_mean,end=' ')
        print(p.stu_std_std)

        for e in range(epochs):
            dict = fdata(p.students,p.tests,p.test_mean,p.test_std,p.stu_std_mean,p.stu_std_std)
            
            for grade,people in dict.items():
                sum[grade] = sum[grade] + people
        
        for grade,people in sum.items():
            sum[grade] = people / epochs / p.students * 100
            
        g = list(sum.keys())[:3]
        percentage = list(sum.values())[:3]
        plt.plot(g,percentage,label=f'{num:0.1f}')


plt.xlabel('grade')
plt.ylabel('percentage')
plt.title('changing '+key)
plt.grid(True)
plt.legend()
plt.savefig('changing_' + key + '.png')
plt.show()


