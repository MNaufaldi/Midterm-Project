
#Teacher class
#this class will be assigned like (teachers name) = Teacher(~~~) so its easy to call

class Teacher:
    Assigned_Time = []
    
    def __init__(self,name,subject,grade):#Takes name and assigned subject and also assigned grade
        self.name = name
        self.subject = subject#This has to be a Subject class
        self.grade = grade
        self.AddToSubject(name,subject)#Auto add to teachers list
        
    #Getter functions
    def getName(self):
        return self.name
    def getSubject(self):
        return self.subject
    def getGrade(self):
        return self.grade
    def getTime(self):
        return self.Assigned_Time
    
    #Setter functions
    def setTime(self,time):
        self.Assigned_Time.append(time)
    
    #Adding to the teachers list
    def AddToSubject(self,name,subject):
        subject.setTeachers(name)
    #Teacher description    
    def toString(self):
        return "{} is teaching {} for grade {}".format(
                self.getName(),self.subject.getSubject(),self.getGrade())
    
        