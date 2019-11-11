
#Subject class
#this class will be assigned to the subject names variable like Math = Subject("Math")
class Subject:
    #Teachers that are assigned to this subject
    Teachers = None
    #Time like Mon:1st hour
    Assigned_Time = []
    #Takes subject name and the subject duration
    def __init__(self,subject,duration="not assigned"):
        self.subject = subject
        self.duration = duration
        
    #Getter functions
    def getSubject(self):#Call subject name
        return self.subject
    def getDuration(self):#Call subject duration
        return self.duration
    def getTeachers(self):#Call teacher that is assigned to the subject
        return self.Teachers
    def getTime(self):#Call assigned time (stack prevention)
        return self.Assigned_Time
    
    #Setter functions
    def setTeachers(self,name):#Assign teacher
        self.Teachers = name
    def setTime(self,time):#Add stack prevention
        self.Assigned_Time.append(time)
        
    #Subject description
    def toString(self):
        if type(self.duration) == int:
            return "{} is assigned for {} hours per week".format(self.getSubject(),self.getTime())
        else:
            return "{} duration is currently not assigned".format(self.getSubject())
    
