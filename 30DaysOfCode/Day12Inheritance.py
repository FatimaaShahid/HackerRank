class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,fname,lname,i,scores):
        super().__init__(fname,lname,i)
        self.scores=scores
    def calculate(self):
        score = sum(scores)/len(scores)
        if score >= 90 and score <=100 :
            return "O"
        elif score < 90 and score >=80 :
            return "E"
        elif score < 80 and score >=70 :
            return "A"
        elif score < 70 and score >=55 :
            return "P"
        elif score < 55 and score >=40 :
            return "D"
        elif score < 40:
            return "T"


    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())