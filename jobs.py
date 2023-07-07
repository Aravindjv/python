class job:

    def __init__(self,taskid,deadline,profit):
        self.taskid=taskid
        self.deadline=deadline
        self.profit=profit
def schedulejobs(jobs,T):
        profit=0
        slot=[-1]*T
        jobs.sort(key=lambda x:x.profit,reverse=true)
        for job  in jobs:
            for j in reversed(range(job.deadline)):
                if j<T and  slot[j]==-1:
                    slot[j]=job.taskid
                    profit+=job.profit
        print("the scheduled jobs are:",list(filter(lambda x:x!=-1,slot)))
        print("the total profit earned is",profit)
if __name__=='__main__':
    jobs=[]
    n=int(input("enter number of jobs"))
    for i in range(n):
           taskid=int(input("enter taskid for job{}:".format(i+1)))
           deadline=int(input("enter the deadline for job{}:".format(i+1)))
           profit=int(input("enter the profit for job{}:".format(i+1)))
           jobs.append(job(taskid,deadline,profit))
    T=int(input("enter the deadline limit"))
    schedulejobs(jobs,T)