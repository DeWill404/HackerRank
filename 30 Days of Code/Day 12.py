

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
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, fname, lname, id, score):
        super().__init__(fname, lname, id)
        self.avg = sum(score)//len(score)
    def calculate(self):
        return "O" if self.avg>=90 else "E" if self.avg>=80 else "A" if self.avg>=70 else "P" if self.avg>=55 else "D" if self.avg>=40 else "T"
