class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print "%s:%s" % (self.name, self.score)
    def get_grade(self):
        if self.score >= 90:
            return "A"
    
bart = Student("xiaoming",98)
bart.print_score()
c = bart.get_grade()
print c




