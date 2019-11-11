#Classroom class
# schedule structure is Subject:Hour:(Detail) detail is for when the said hour is divided

class Classroom:
    Assigned_Time = []
    AvailableSubjects = {}
    Schedule = {}
    
    def __init__(self,grade,sufix):#Sufix is like A B C D after the grade number
        self.grade = grade
        self.sufix = sufix
        self.ClassroomName = "{}{}".format(self.grade,self.sufix)
    
    def setAssignedTime(self,subject,time):
        self.Assigned_Time.append("{}:{}".format(time,subject))
    def setHomeroomTeacher(self,teacher):
        self.HomeroomTeacher = teacher
    def setAvailableSubjects(self,subjectduration):
        self.AvailableSubjects = subjectduration
    def setSchedule(self,time,subject):
        self.Schedule[time] = subject
        
    def getHomeroomTeacher(self):
        return self.HomeroomTeacher
    def getAssignedTime(self):
        return self.Assigned_Time
    def getAvailableSubjects(self):
        return self.AvailableSubjects
    def getClassroomName(self):
        return self.ClassroomName
    def getSchedule(self):
        return self.Schedule
    def getScheduleSubject(self):
        return self.Schedule.values
        

