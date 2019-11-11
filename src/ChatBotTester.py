import Controller
import datetime
import Utility


global today
global tomorrow
global tree, teachersSchedule, examSchedule, bloodGroupData


def getTodaysWeekDay():
    global today, tomorrow
    today = int(datetime.datetime.today().strftime('%w'))
    tomorrow = today + 1
    Utility.dayName['today'] = today
    Utility.dayName['tomorrow'] = tomorrow
    # print(Utility.dayName)


def initializeData():
    global tree, teachersSchedule, examSchedule, bloodGroupData
    tree = Controller.initiateStudentsRoutine()
    teachersSchedule = Controller.initiateTeachersSchedule()
    examSchedule = Controller.initiateExamSchedule()
    bloodGroupData = Controller.initiateBloodGroup()
    # print("\n", tree)   
    # print("\n", teachersSchedule)
    # print("\n", examSchedule)   
    # print("\n", bloodGropData)


def initializeQueryProcessor():
    Controller.startQueryProcessor()


def generateQuery(extractKeywords):
    global tree, teachersSchedule, examSchedule, bloodGroupData
    global today, tomorrow
    semesterFound = False
    dayFound = False
    CourseFound = False
    TeacherNameFound = False
    bloodGroupFound = False
    timeRequires = False
    nameRequires = False
    isGreeting = False
    bloodDetected = False

    SemesterNo = None
    dayID = None
    TeacherID = None
    bloodGroup = None
    CourseName = None
    greeting = None
    requiresExamRoutine = False
    requiresClassRoutine = False

    iitFound = False


    result = None

    for term in extractKeywords:
        if term in Utility.greetings:
            isGreeting = True
            greeting = term
            # print(term)

        if term in Utility.dayName:
            dayFound = True
            dayID = Utility.dayName[term]
            # print(dayID)

        if term in Utility.semester:
            semesterFound = True
            SemesterNo = Utility.semester[term]
            # print(SemesterNo)

        if term in Utility.teacher_Id:
            TeacherNameFound = True
            TeacherID = Utility.teacher_Id[term]
            # print(TeacherID)

        if term in Utility.course:
            CourseFound = True
            value = Utility.course[term]
            value = value.split("|")
            CourseName = value[1].strip()

            semesterFound = True
            SemesterNo = value[0].strip()
            # print(SemesterNo, "-", CourseName)

        if term in Utility.bloodGrouping:
            bloodGroupFound = True
            bloodGroup = Utility.bloodGrouping[term]
            # print(bloodGroup)

        if "xm" in extractKeywords or "exam" in extractKeywords or "examinatiom" in extractKeywords:
            requiresExamRoutine = True

        if "class" in extractKeywords or "routine" in extractKeywords :
            requiresClassRoutine = True

        if "iit" in extractKeywords:
            iitFound = True

        if 'blood' in extractKeywords:
            bloodDetected = True


    query = ""
    if dayFound:
            if semesterFound and CourseFound:
                query = query+str(SemesterNo)+","+str(dayID)+","+CourseName
                result = Controller.getStudentsRoutine(tree, query)
            elif semesterFound:
                query = query+str(SemesterNo)+","+str(dayID)
                result = Controller.getStudentsRoutine(tree, query)
            else:
                line = input(" >> Are you a student or teacher?\n")
                extractKeywords = Controller.messageParser(line)
                if "teacher" in extractKeywords or "faculty" in extractKeywords:
                    line = input(" >> Your name please?\n")
                    extractKeywords = Controller.messageParser(line)
                    for term in extractKeywords:
                        if term in Utility.teacher_Id:
                            TeacherNameFound = True
                            TeacherID = Utility.teacher_Id[term]
                            # print(TeacherID)
                            break
                    query = query+str(TeacherID)+","+str(dayID)
                    result = Controller.getTeachersSchedule(teachersSchedule, query)

                elif "student" in extractKeywords:
                    line = input(" >> Semester No please?\n")
                    extractKeywords = Controller.messageParser(line)
                    for term in extractKeywords:
                        if term in Utility.semester:
                            semesterFound = True
                            SemesterNo = Utility.semester[term]
                            # print(SemesterNo)
                            break
                    query = query+str(SemesterNo)+","+str(dayID)
                    result = Controller.getStudentsRoutine(tree, query)


    elif requiresExamRoutine:
            if CourseFound:
                query = query+str(SemesterNo)+","+ "-1" +","+ CourseName
                result = Controller.getExamSchedule(examSchedule, query)
                
            elif semesterFound:
                query = query+str(SemesterNo)
                result = Controller.getExamSchedule(examSchedule, query)

            else:
                line = input(" >> Semester No please?\n")
                extractKeywords = Controller.messageParser(line)
                for term in extractKeywords:
                    if term in Utility.semester:
                        semesterFound = True
                        SemesterNo = Utility.semester[term]
                        # print(SemesterNo)
                        break
                query = query+str(SemesterNo)
                result = Controller.getExamSchedule(examSchedule, query)



    elif semesterFound:
        if not CourseFound:
            query = query+str(SemesterNo)
            result = Controller.getStudentsRoutine(tree, query)


    elif bloodDetected or bloodGroupFound:
        if bloodGroupFound:
            query = query+bloodGroup
            # print(query)
            result = Controller.findBloodGroup(bloodGroupData, query)
        else:
            line = input(" >> Which group of Blood?\n")
            extractKeywords = Controller.messageParser(line)
            for term in extractKeywords:
                bloodGroupFound = True
                bloodGroup = Utility.bloodGrouping[term]
                break
            query = query+bloodGroup
            # print(query)
            result = Controller.findBloodGroup(bloodGroupData, query)


    elif requiresClassRoutine:
            # "6,"",ai"
            # "dbms class routine"
            # "when ai class will take place?"
                line = input(" >> Are you a teacher or student?\n")
                extractKeywords = Controller.messageParser(line)
                if "teacher" in extractKeywords or "faculty" in extractKeywords:
                    line = input(" >> Please specify your name.\n")
                    extractKeywords = Controller.messageParser(line)
                    for term in extractKeywords:
                        if term in Utility.teacher_Id:
                            TeacherNameFound = True
                            TeacherID = Utility.teacher_Id[term]
                            # print(TeacherID)
                            break
                    query = query+str(TeacherID)
                    result = Controller.getTeachersSchedule(teachersSchedule, query)
                elif "student" in extractKeywords:
                    line = input(" >> Semester No please?\n")
                    extractKeywords = Controller.messageParser(line)
                    for term in extractKeywords:
                        if term in Utility.semester:
                            semesterFound = True
                            SemesterNo = Utility.semester[term]
                            # print(SemesterNo)
                            break
                    query = query+str(SemesterNo)
                    result = Controller.getStudentsRoutine(tree, query)

    # elif requiresExamRoutine:
    #     line = input(" >> Semester No please?\n")
    #     extractKeywords = Controller.messageParser(line)
    #     for term in extractKeywords:
    #         if term in Utility.semester:
    #             semesterFound = True
    #             SemesterNo = Utility.semester[term]
    #             # print(SemesterNo)
    #             break
    #     query = query+str(SemesterNo)
    #     result = Controller.getExamSchedule(examSchedule, query)


    elif isGreeting:
            result = Utility.greetings[greeting]

    else:
            if iitFound:
                result = '''IIT is the best institute of Bangladesh.
                                                - Dr. Mohommad Shoyaib'''
            elif TeacherNameFound:
                result = Utility.teachers[TeacherID] + " is a faculty of the best institute."
            else:
                result = "Sorry. I couldn't get your question."

    return result





def startChat():
    while True:
        line = input("\n >> Write Your Messages Here >>\n")
        if line != "q" or line != "Q" or line != 'quit' or line != 'exit':
            extractKeywords = Controller.messageParser(line)
            # print(extractKeywords)
            result = generateQuery(extractKeywords)
            if not result:
                result = "No result found."
            print( result)
            extractKeywords.clear()
        else:
            break



def main():
    global today, tomorrow
    getTodaysWeekDay()  
    # print(today, " ", tomorrow)
    initializeData()
    initializeQueryProcessor()

    startChat()



if __name__ == "__main__":
    main()
