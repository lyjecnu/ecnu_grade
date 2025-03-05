class input:
    def __init__(self,**kwargs):
        self.students = 100
        self.tests = 10
        self.test_mean = 65
        self.test_std = 15    
        self.stu_std_mean = 6
        self.stu_std_std = 1
        self.property = 0.6   #stu_std_mean / test_mean
        
        for key, value in kwargs.items():
            setattr(self, key, value)
          


params = input(tests=(10,20,1))