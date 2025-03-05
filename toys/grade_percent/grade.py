import numpy as np




def fdata(size,tests,x,y,std_mean,std_std):
    
    
    def r2g(rank):
        if rank <= size * 0.15:
            return 4.0
        elif rank <= size * 0.3:
            return 3.7 + (size*0.3-rank) / (0.15*size) * 0.3
        elif rank <= size * 0.45:
            return 3.3 + (size*0.45-rank) / (0.15*size) * 0.4
        elif rank <= size*0.6:
            return 3 + (size*0.6-rank) / (0.15*size) * 0.3
        elif rank <= size*0.8:
            return 2.5 + (size*0.8-rank) / (0.2*size) * 0.5
        elif rank <= size*0.9:
            return 2 + (size*0.9-rank) / (0.1*size) * 0.5
        else:
            return 1.5 + (size-rank) / (0.1*size) * 0.5
    
    
    mean = np.random.normal(loc=x, scale=y, size=size)
    
    std = np.zeros(size)
    for s in range(size):
        while True:
            std[s] = np.random.normal(loc=std_mean,scale=std_std)
            
            if std[s] > 0:
                break
    
    
    score = np.zeros((tests,size))
    grade = np.zeros((tests,size))

    for t in range(tests):
        
        for s in range(size):
            score[t][s] = np.random.normal(loc=mean[s],scale=std[s])
    
        index_array = enumerate(score[t])
        sorted_array = sorted(index_array,key=lambda x:x[1],reverse=True)
    
        rank = np.zeros(size)
        for s in range(size):
            rank[sorted_array[s][0]] = s + 1
        
        for s in range(size):
            grade[t][s] = r2g(rank[s])
        
            

    dict = {
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
        
        
    for s in range(size):
        sum = 0
        for t in range(tests):
            sum = sum + grade[t][s]
        sum = sum / tests
        #print(sum)
        
        for g in range(30,40):
            q = g / 10
            if sum >= q:
                dict[str(q)+"+"] = dict[str(q)+"+"] + 1
        
    return dict



#print(fdata(100,10,65,15,9,1))
#print(fdata(100,20,65,15,9,1))
 
 

