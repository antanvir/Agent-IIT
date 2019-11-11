import TeachersSchedule
import RoutineForStudents_dTree
import ExamSchedule
import BloodGroup
import UserQueryProcessor



global today
global tomorrow


def getStudentsRoutine(tree, query):
	return RoutineForStudents_dTree.takeQuery(tree, query)


def getExamSchedule(dataset, query):
	return ExamSchedule.takeQuery(dataset, query)

def getTeachersSchedule(dataset, query):
	return TeachersSchedule.takeQuery(dataset, query)


def findBloodGroup(dataset, group):
	return BloodGroup.takeQuery(dataset, group)


def initiateStudentsRoutine():
	return RoutineForStudents_dTree.main()


def initiateExamSchedule():
	return ExamSchedule.main()

def initiateTeachersSchedule():
	return TeachersSchedule.main()


def initiateBloodGroup():
	return BloodGroup.main()


def startQueryProcessor():
	UserQueryProcessor.initialize()


def messageParser(userInput):
	return UserQueryProcessor.process(userInput)


if __name__ == "__main__":
    main()
