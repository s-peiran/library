class job:
    def __init__(self,deadline,price):
        self.deadline=deadline
        self.price=price

array=[]
#array.append(job(2,70))
#array.append(job(1,50))
#array.append(job(1,40))
#array.append(job(3,30))

array.append(job(1,8))
array.append(job(3,5))
array.append(job(3,6))
array.append(job(3,7))

#array.append(job(3,30))
#array.append(job(3,20))
#array.append(job(3,20))
#array.append(job(1,10))

        
def jobScheduling (array):
    timetable=[None for i in range(len(array))] #initialise the result list/array
    array.sort(key=lambda x: x.price,reverse=True)  # sort jobs by descending price
    for job in array:                # loop through the jobs in above sorted order
        for i in range(len(timetable)-1,-1,-1):     # loop through the timetable in
                                          # descending order of time to find a slot
            if i<job.deadline and timetable[i]==None: #insert to slot if not taken
                                # time the job is performed must be within deadline 
               timetable[i]=job
               break;
            
    while (timetable[-1]==None):    #remove trailing None
        timetable.pop()
        
    for i in timetable:             #print answer
        if i==None:
            print(i)
        else:    
            print(f'{i.deadline} {i.price}')

jobScheduling(array)
