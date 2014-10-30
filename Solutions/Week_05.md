---
layout      : post
categories  : solutions
title       : Week 5 - Solutions - Object Orientated Programming
comments    : true
---


## Q1

{% highlight python %}
"""
Solution to question 1 of week 5 lab sheet.

"""

class Student():
    """
    A class that does nothing
    """
    pass  # The pass command does not do anything but a command is needed to avoid a syntax error

vince = Student()
print vince

joey = Student()
print joey
{% endhighlight %}

## Q2

{% highlight python %}
"""
Solution to question 2 of week 5 lab sheet.

There is nothing much going on in this question. Simply there so that student understand that they kind have already been using objects.
"""

a = 25
a = str(a)
{% endhighlight %}

## Q3

{% highlight python %}
"""
Solution to question 3 of week 5 lab sheet.

"""


class Student():
    """
    A class for a student.

    Attributes:
        courses: the courses on which the student is enrolled
        age: the age of the student
        sex: the gender of the student
    """
    courses = ["Biology", "Mathematics", "English"]
    age = 12
    sex = 'Male'

# Create a student and print the student's attributes to screen
vince = Student()
print vince.courses
print vince.age
print vince.sex

# Include a new course
vince.courses.append("French")
print vince.courses

# Change age
vince.age = 28
print vince.age

# Change gender
vince.sex = "M"
print vince.sex
{% endhighlight %}

## Q4

{% highlight python %}
"""
Solution to question 4 of week 5 lab sheet.
"""

import csv  # Am importing this library as can also be used to import data


class Quadratic():
    """
    A class for a quadratic

    Attributes:
        a: The coefficient of x^2
        b: The coefficient of x
        c: The coefficient of x^0
    """
    a = 0
    b = 0
    c = 0


f = open('W05_D01.csv', 'r')
csvdata = csv.reader(f)  # This is a slightly messier file to read manually so using the csv library
data = [row for row in csvdata]  # Read all data in to a list
f.close()  # Close file
data = [[float(e) for e in row] for row in data[1:]]  # Convert relevant data to float

listofquadratics = []  # Initialise empty list
for row in data:
    listofquadratics.append(Quadratic())  # Append a quadratic to the list
    listofquadratics[-1].a = row[0]  # Change attribute names to match data
    listofquadratics[-1].b = row[1]
    listofquadratics[-1].c = row[2]

for q in listofquadratics:
    print "%sx^2+%sx+%s" % (q.a, q.b, q.c)  # Print out quadratic
{% endhighlight %}

## Q5

{% highlight python %}
"""
Solution to question 5 of week 5 lab sheet.
"""


class Student():
    """
    A class for a student.

    Attributes:
        courses: the courses on which the student is enrolled
        age: the age of the student
        sex: the gender of the student

    Methods:
        haveabirthday: increments age
    """
    courses = ["Biology", "Mathematics", "English"]
    age = 12
    sex = 'Male'

    def haveabirthday(self):
        """
        Increments age by 1

        Arguments: NA

        Outputs: NA
        """
        self.age += 1

vince = Student()  # Assign a student to the variable vince
print vince.age
vince.haveabirthday()  # Make vince have a birthday
print vince.age


class Student():
    """
    A class for a student.

    Attributes:
        courses: the courses on which the student is enrolled
        age: the age of the student
        sex: the gender of the student

    Methods:
        haveabirthday: increments age
    """
    courses = ["Biology", "Mathematics", "English"]
    age = 12
    sex = 'Male'

    def haveabirthday(self, numberofbirthdays=1):
        """
        Increments age by 1 (default) or a given amount

        Arguments: numberofbirthdays

        Outputs: NA
        """
        self.age += numberofbirthdays

vince = Student()
print vince.age
vince.haveabirthday()
print vince.age
vince.haveabirthday(28)
print vince.age
{% endhighlight %}

## Q6

{% highlight python %}
"""
Solution to question 6 of week 5 lab sheet.

Although this is not a tickable exercise, it is a very important one. It introduces certain 'important' methods in python.
"""

class Student():
    """
    A class for a student.

    Attributes:
        courses: the courses on which the student is enrolled
        age: the age of the student
        sex: the gender of the student

    Methods:
        haveabirthday: increments age
    """
    def __init__(self, courses, age, sex):  # The init method is a standard method that allows us to pass arguments to a class when we create an instance. There is no real need to give it the standard level of comments.
        self.courses = courses
        self.age = age
        self.sex = sex
    def haveabirthday(self, numberofbirthdays):
        """
        Increments age by 1 (default) or a given amount

        Arguments: numberofbirthdays

        Outputs: NA
        """
        self.age += numberofbirthdays


vince = Student(["Biology","Math"], 28, "Male")  # Creating an instance by passing arguments. This uses the init method
print vince.courses
print vince.age
print vince.sex
{% endhighlight %}

## Q07

{% highlight python %}
"""
Solution to question 7 of week 5 lab sheet.

"""

import csv  # Am importing this library as can also be used to import data


class Quadratic():
    """
    A class for a quadratic

    Attributes:
        a: The coefficient of x^2
        b: The coefficient of x
        c: The coefficient of x^0

    Methods:
        hasrealroots: returns boolean depending on whether or not real roots exist
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def hasrealroots(self):
        """
        Return true if function has real roots (false otherwise)

        Arguments: NA
        Outputs: True or False
        """
        if self.b ** 2 > 4 * self.a * self.c:
            return True
        return False

f = open('W05_D01.csv', 'r')
csvdata = csv.reader(f)  # This is a slightly messier file to read manually so using the csv library
data = [row for row in csvdata]  # Read all data in to a list
f.close()  # Close file
data = [[float(e) for e in row] for row in data[1:]]  # Convert relevant data to float

listofquadratics = []  # Initialise empty list
for row in data:
    listofquadratics.append(Quadratic(row[0], row[1], row[2]))  # Append a quadratic to the list

nbrofqwithrealroots = len([e for e in listofquadratics if e.hasrealroots()])  # Count the elements that have real roots
print "%s of %s equations have real roots" % (nbrofqwithrealroots, len(listofquadratics))
{% endhighlight %}

## Q08

{% highlight python %}
"""
Solution to question 8 of week 5 lab sheet.

"""
Course_Dictionary = {1: "Math",
                     2: "English",
                     3: "French",
                     4: "Physics",
                     5: "PE",
                     6: "Biology",
                     7: "History",
                     8: "Geography"}  # Dictionary given

Student_List = [["Adam", [1, 2, 5]],
                ["Zoe", [4, 3, 2]],
                ["Ben", [7]],
                ["Thomas", []],
                ["Meryl", [2, 3]],
                ["James", [6, 7, 2]],
                ["Leanne", []],
                ["Angelico", [1]],
                ["Izabela", [1, 2, 3, 4, 5]],
                ["Lisa", [1, 8]],
                ["Penny", [1, 2, 3]]]  # List given


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
    def __init__(self, name, course_list, course_dictionary=Course_Dictionary):
        self.name = name
        self.course_list = []
        for e in course_list:
            self.course_list.append(course_dictionary[e])
        self.enrolled = False
        if len(self.course_list) > 0:
            self.enrolled = True


class School_Year():
    """
    A class that generates the solution to the example
    """
    def __init__(self, student_list=Student_List, course_dictionary=Course_Dictionary):
        #We initialise an empty dictionary that will keep count of numbers on each course.
        self.course_numbers = {}
        #We go through every key in the course_dictionary and set the corresponding value (in our new dictionary) to be 0.
        for e in course_dictionary:
            self.course_numbers[course_dictionary[e]] = 0

        #We initialise an empty list of students. NOTE:  this list will contain our instances of the student class defined above.
        self.student_record = []
        for e in Student_List:
            #We create a temporary new_student who is appended to the list of students. NOTE that due to the OOP nature of our code we don't need to worry too much about what information is created with the student. This was all done previously!
            new_student = Student(e[0], e[1])
            self.student_record.append(new_student)

            #We increment the number of students enrolled for each course on which our student is enrolled.
            for i in new_student.course_list:
                self.course_numbers[i] += 1

    def output(self):
        #A method to print to screen all the required info. First we print (IF THE VALUE OF ENROLLED IS TRUE!) the name of the student and some other info.
        for e in self.student_record:
            if e.enrolled:
                print e.name,  "is enrolled on: "
                for i in e.course_list:
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

#Note that this code could be (perhaps) improved by also making a course class...
{% endhighlight %}


## Q09

{% highlight python %}
"""
Solution to question 9 of week 5 lab sheet.
"""

import random
import math  # This is not necessarily needed but will be useful for some comparisons later on.


class Drop():
    """
    A class for a rain drop falling in a random location on a square

    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        incircle: a boolean indicating whether or not the point is in the inscribed circled
    """
    def __init__(self, r=1):
        self.x = (.5 - random.random()) * 2 * r
        self.y = (.5 - random.random()) * 2 * r
        self.incircle = (self.y) ** 2 + (self.x) ** 2 <= (r) ** 2  # This returns the boolean corresponding to whether or not the point is in the circle


def approxpi(N=1000):
    """
    Function to return an approximation for pi using montecarlo simulation

    Arguments: N (default=1000) which is the number of points

    Outputs: An approximation of pi
    """
    numberofpointsincircle = 0
    for i in range(N):  # A loop to drop sufficient points
        drop = Drop()  # Generate a new drop
        if drop.incircle:  # Check if drop is in circle
            numberofpointsincircle += 1
    return 4 * numberofpointsincircle / float(N)


#########################################
# This is possibly pushing students a bit. Compares approximations to actual
# value of pi using the 'math' library.
bestapproxdif = abs(approxpi(1) - math.pi)  # Initiate a best approximation
bestN = 1  # Corresponding N
for N in range(2, 10001):  # Check approximation for 10000 values of N
    approxdif = abs(approxpi(N) - math.pi)  # check how good new approximation is
    if approxdif < bestapproxdif:  # if approximation is better update best values
        bestapproxdix = approxdif
        bestN = N
print "Best N is: %s" % bestN
# This indicates that increasing the number of points improves the
# approximation (which is logical)
#########################################

print "For N=200, pi approximated as %s" % approxpi(200)
print "For N=1000, pi approximated as %s" % approxpi()
print "For N=10000, pi approximated as %s" % approxpi(10000)
print "For N=100000, pi approximated as %s" % approxpi(100000)
print "For N=1000000, pi approximated as %s" % approxpi(1000000)
print "For N=10000000, pi approximated as %s" % approxpi(10000000)  # This seems to be the correct order of magnitude for 3 decimal places...
{% endhighlight %}

## Q10

{% highlight python %}
"""
Solution to question 10 of week 5 lab sheet.

"""


class Student():
    """
    A class for a student.

    Attributes:
        courses: the courses on which the student is enrolled
        age: the age of the student
        sex: the gender of the student

    Methods:
        haveabirthday: increments age
    """
    def __init__(self, courses, age, sex):  # The init method is a standard method that allows us to pass arguments to a class when we create an instance. There is no real need to give it the standard level of comments.
        self.courses = courses
        self.age = age
        self.sex = sex
    def haveabirthday(self, numberofbirthdays=1):
        """
        Increments age by 1 (default) or a given amount

        Arguments: numberofbirthdays

        Outputs: NA
        """
        self.age += numberofbirthdays


class MathStudent(Student):
    """
    An inherited class from Student that has a new attribute: favorite class

    Attributes:
        courses: the courses on which the student is enrolled
        age: the age of the student
        sex: the gender of the student
        favouriteclass: Mathematics

    Methods:
        haveabirthday: increments age
    """
    favouriteclass = "Mathematics"

becky = MathStudent(['Mathematics', 'Biology'], 29, 'Female')
print becky.courses
print becky.age
print becky.favouriteclass
becky.haveabirthday()
print becky.age

class BadStudent(MathStudent):
    """
    An inherited class from MathStudent that has a new attribute: favorite class

    Attributes:
        courses: the courses on which the student is enrolled
        age: the age of the student
        sex: the gender of the student
        favouriteclass: Mathematics

    Methods:
        haveabirthday: increments age
        flunkclass: takes a string and removes it from the courses
    """
    def flunkclass(self, course):
        """
        A method that removes a course from the courses

        Arguments: A string

        Outputs: NA
        """
        del self.courses[self.courses.index(course)]  # This uses the del command which is new but students are welcome to do whatever they want

jason = BadStudent(['Mathematics', 'Computer Science'], 12, 'Male')
print jason.courses
jason.flunkclass(jason.favouriteclass)  # Note that this class inherits from MathStudent
print jason.courses
{% endhighlight %}
