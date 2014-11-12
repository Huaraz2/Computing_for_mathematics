"""
Solution to question 1 of class test

Marking for this exercise will be strict as the students were told multiple times during lectures that all they would need to do for question 1 of the class test is to copy a file from the solutions.
"""

coursedictionary = {1: "Analysis I",
                    2: "Geometry",
                    3: "Algebra I",
                    4: "Computing for Mathematics"}

studentlist = [["Adam", [1, 2, 3]],
                ["Zoe", [4, 2, 1]],
                ["Ben", [3]],
                ["Thomas", [4]]]

#################################
# 10 marks for changing the inputs
#################################

class Course():
    """
    A class for each course with attributes:
    - A list of enrolled students
    - Number of enrolled students
    This class also contains a method that 'enrolls' a new student
    """
    def __init__(self, student_list=[]):
        self.student_list = student_list
        self.number_enrolled = len(student_list)

    def enroll_new_student(self, student):
        self.student_list.append(student)
        self.number_enrolled += 1


class Student():
    """
    A class for each student with attributes:
    - Their name
    - The list of courses enrolled on
    - A boolean true/false variable indicating whether or not the student is enrolled on at least 1 course
    """
    def __init__(self, name, courselist, coursedictionary=coursedictionary):
        self.name = name
        self.courselist = []
        for e in courselist:
            self.courselist.append(coursedictionary[e])
        self.enrolled = False
        if len(self.courselist) > 0:
            self.enrolled = True


class School_Year():
    """
    A class that generates the solution to the example
    """
    def __init__(self, studentlist=studentlist, coursedictionary=coursedictionary):
        #We initialise an empty dictionary that will keep count of numbers on each course.
        self.course_numbers = {}
        #We go through every key in the course_dictionary and set the corresponding value (in our new dictionary) to be 0.
        for e in coursedictionary:
            self.course_numbers[coursedictionary[e]] = 0

        #We initialise an empty list of students. NOTE:  this list will contain our instances of the student class defined above.
        self.student_record = []
        for e in studentlist:
            #We create a temporary new_student who is appended to the list of students. NOTE that due to the OOP nature of our code we don't need to worry too much about what information is created with the student. This was all done previously!
            new_student = Student(e[0], e[1])
            self.student_record.append(new_student)

            #We increment the number of students enrolled for each course on which our student is enrolled.
            for i in new_student.courselist:
                self.course_numbers[i] += 1

    def output(self):
        #A method to print to screen all the required info. First we print (IF THE VALUE OF ENROLLED IS TRUE!) the name of the student and some other info.
        for e in self.student_record:
            if e.enrolled:
                print e.name,  "is enrolled on: "
                for i in e.courselist:
                    print "\t", i
        print ""
        print "---------------"
        print ""
        #We print the course numbers
        for e in self.course_numbers:
            print e, " has ", self.course_numbers[e], "students enrolled"


#We now create the instance and run the output method.
a = School_Year()
a.output()

###########################################
# 20 marks for pasting the correct solution
###########################################
