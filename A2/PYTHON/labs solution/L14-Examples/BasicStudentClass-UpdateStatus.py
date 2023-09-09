class Student:
    Count = 0 #Number of instances
    def __init__(self,NAME,ID,T1,T2,st=1):
        self.name = NAME
        self.id = ID
        self.status = st #full-time=1, part-time=2
        self.t1 = T1
        self.t2 = T2
        Student.Count += 1
    def __del__(self):
        Student.Count -= 1
        print ("Deleting Student instance!")
    def __repr__(self):
        if self.status==1: stat="full-time"
        else: stat="part-time"
        format_str="{:20s}{:7d} {:10s}"
        d=format_str.format(self.name,self.id,stat)
        return(d)
    def update_status(self,new_status):
        self.status  =  new_status
