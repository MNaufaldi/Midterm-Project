#%%
#main
import xlsxwriter as xw
from Classroom import Classroom 
from Subject import Subject
from Teacher import Teacher
import csv
import random
SubjectFile = "Subject.csv"
NumberOfClasses = 1
Grade = "X"
Classroom_List = []
Subjects_List = []
Teachers_List = []
SubjectTeacher = {}
SubjectDuration = {}
TimeSubject = {}
SubjectFor3 = []
SubjectFor2 = []
Next1Hour = None
Next2Hour = None


#To create the lists and dictionaries
def CreateAll(file):
    global Subjects_List,Teachers_List,Classrom_List,SubjectDuration,SubjectTeacher,TimeSubject
    with open(file) as Subjects:
        reader = csv.reader(Subjects)
        header = next(Subjects)
        for row in reader:
            #Creating classes for each of elements that are called
            row[0] = Subject(row[0],int(row[1]))
            row[2] = Teacher(row[2],row[0],row[3])
            row[0].setTeachers(row[2])
            #Adding the classes to a list
            Subjects_List.append(row[0])
            Teachers_List.append(row[2])
            #Pairing them
            SubjectTeacher[row[0]] = row[2]
            SubjectDuration[row[0]] = int(row[1])
        #Create 5 classroom (for testing purposes) and grade x
        for Class in range(NumberOfClasses):
            CurrentClass = "{}{}".format(Grade,chr(65+Class))
            CurrentClass = Classroom(Grade,chr(65+Class))
            CurrentClass.setAvailableSubjects(SubjectDuration)
            Classroom_List.append(CurrentClass)
        #Create a dictionary with time and the available subjects at that time
        for day in range(1,6):#Day
            for hour in range(1,13):#Hour
                if hour == 5 or hour == 9:
                    TimeSubject["{}:{}".format(day,hour)] = "Break"
                elif hour == 1:
                    if day == 1:
                        TimeSubject["{}:{}".format(day,hour)] = "Ceremony"
                    else:
                        TimeSubject["{}:{}".format(day,hour)] = "Homeroom"
                else:
                    TimeSubject["{}:{}".format(day,hour)] = Subjects_List
        #Create the special subjects
        for subjects in SubjectDuration.keys():
            if SubjectDuration[subjects] == 3:
                SubjectFor3.append(subjects)
            elif SubjectDuration[subjects] == 2 or SubjectDuration[subjects] == 4:
                SubjectFor2.append(subjects)
            else:
                continue
            
       


def CreateAvailableSubjects(SubjectDuration,Time,TimeSubject,Classroom,SubjectForTheDay):
    global SubjectFor2,SubjectFor3,Next1Hour,Next2Hour
    AvailableSubjects = list(TimeSubject[Time])
    random.shuffle(AvailableSubjects)
    day = int(Time[0])
    hour = int(Time[2::])
    
    #These for loops are reversed because it has to be this way so i can remove the subject while iterating
    #Sometimes it doesnt work
    #Check duration
    for subject in reversed(AvailableSubjects):
        if SubjectDuration[subject] < 1:
            AvailableSubjects.remove(subject)
        
    for subject in reversed(AvailableSubjects):
        try:
            if Next1Hour != None or Next2Hour != None:
                if subject == SubjectForTheDay[-1]:
                    #Could be 2 hours or 3 hours sequence
                    if subject in SubjectFor3:
                        #3 hours sequence
                        AvailableSubjects = [subject]
                        #Reset the 'flag' for 3 hours sequence
                        if subject == SubjectForTheDay[-2]:
                            Next2Hour = None
                            
                    elif subject in SubjectFor2:
                        #2 hours sequence
                        if subject == SubjectForTheDay[-1]:
                            AvailableSubjects = [subject]
                            Next1Hour = None
                else:#Meaning that the subject is already in that day but it is not connected to the sequence
                    pass
                    
                
            else:#This is strictly for the first hour and subject changing
                if Next1Hour == None or Next2Hour == None:
                    if subject in SubjectFor2 and subject not in SubjectForTheDay:
                        #2nd hour check
                        if subject in list(TimeSubject["{}:{}".format(str(day),str(hour+1))]):
                            AvailableSubjects = [subject]
                            Next1Hour = [subject]
                            
                        #If the 2 hours sequence is interrupted by break time
                        elif list(TimeSubject["{}:{}".format(str(day),str(hour+1))]) == 'Break':
                            if subject in list(TimeSubject["{}:{}".format(str(day),str(hour+2))]):
                                AvailableSubjects = [subject]
                                Next1Hour = [subject]
                    
                    elif subject in SubjectFor3 and subject not in SubjectForTheDay:
                        #Next 2 hours check
                        if subject in list(TimeSubject["{}:{}".format(str(day),str(hour+1))]) and list(TimeSubject["{}:{}".format(str(day),str(hour+2))]):
                            AvailableSubjects = [subject]
                            Next2Hour = [subject]
                            
                        #If the 3 hours sequence is interrupted by break time 
                        elif list(TimeSubject["{}:{}".format(str(day),str(hour+1))]) == 'Break':
                            if subject in list(TimeSubject["{}:{}".format(str(day),str(hour+2))]) and list(TimeSubject["{}:{}".format(str(day),str(hour+3))]):
                                AvailableSubjects = [subject]
                                Next2Hour = [subject]
                        elif list(TimeSubject["{}:{}".format(str(day),str(hour+2))]) == 'Break':
                            if subject in list(TimeSubject["{}:{}".format(str(day),str(hour+1))]) and list(TimeSubject["{}:{}".format(str(day),str(hour+3))]):
                                AvailableSubjects = [subject]
                                Next2Hour = [subject]
                             
        #Some lines have these error but it is not critical
        except (IndexError, KeyError):
            pass
            
        
    
    
    return AvailableSubjects


def CreateSchedule(Classroom,SubjectDuration):
    global TimeSubject
    hour = 1
    #A list to keep track of subject that has been placed for the day 
    SubjectForTheDay = []
    
    #Start iterating through the predefined time
    for time in list(TimeSubject.keys()):
        #1st hour and break times
        SpecialHour = [1,5,9]
        
        if hour in SpecialHour:
            Classroom.setSchedule(time,TimeSubject[time])
            hour += 1
            
        #Assigning the subject to the schedule in classroom class
        else:
            AvailableSubjects = CreateAvailableSubjects(SubjectDuration,time,TimeSubject,Classroom,SubjectForTheDay)
            Subject = AvailableSubjects[0]
            Classroom.setSchedule(time,Subject)
            SubjectForTheDay.append(AvailableSubjects[0])
            SubjectDuration[AvailableSubjects[0]] -= 1
           
            
            hour += 1 
            
        #Reset when the day is over    
        if hour == 13:
            SubjectForTheDay = []
            hour = 1
            
#Calling the functions to create the schedule
CreateAll(SubjectFile)    
CreateSchedule(Classroom_List[0],SubjectDuration.copy())

#Predefined header for the excel file
Schedule = [['Time','Subject','Teacher']]

#For file writing to excel file
for time in Classroom_List[0].getSchedule().keys():
    
    #defining time format for easier writing
    dayList = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    day = dayList[int(time[0])-1]
    hour = int(time[2::])
    
    #Creating the data list to write into excel
    try:
        Schedule.append(["{}:{}".format(day,hour),
                         Classroom_List[0].getSchedule()[time].getSubject(),
                         Classroom_List[0].getSchedule()[time].getTeachers().getName()])
    #Subjects that doesnt have teachers (homeroom,ceremony,break etc) will go here
    except AttributeError:
        Schedule.append(["{}:{}".format(day,hour),
                         Classroom_List[0].getSchedule()[time],
                         "-"])
    
#Create the workbook and the sheet in excel    
wbSchedule = xw.Workbook('Class Schedule.xlsx')
wsSchedule = wbSchedule.add_worksheet('Schedule')

#Predefining the row and col number for easier format
row_number = 0
col_number = 0

#Creating the data with time,subject,teacher format
#It wont work if it already have a file with that name
for time, subject, teacher in Schedule:
    wsSchedule.write(row_number,col_number,time)
    wsSchedule.write(row_number,col_number + 1,subject)
    wsSchedule.write(row_number,col_number + 2,teacher)
    #As subject changes the row will increase
    row_number += 1
    
wbSchedule.close()






#%%