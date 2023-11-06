class School:
    def __init__(self, name):
        self.name = name
        self.bachelor_d = {}
        self.student_d = {}

    def __str__(self):
        s = f"école:{self.name}\n"
        for k, b in self.bachelor_d.items():
            s += str(b)
        return s

    def create_bachelor(self, bach_name):
        b = Bachelor(bach_name)
        self.bachelor_d[bach_name] = b

    def create_lecture(self, bach_name, lect_name):
        b = self.bachelor_d[bach_name]
        b.create_lecture(lect_name)

    def register_student(self, stud_name):
        self.student_d[stud_name] = Student(stud_name)

    def register_lecture(self, bach_name, lect_name, stud_name):
        s = self.student_d[stud_name]  # objet Rudy
        l = self.bachelor_d[bach_name].get_lecture(lect_name) # objet Algo
        s.register_lecture(l)
        l.register_student(s)


class Bachelor:
    def __init__(self, name):
        self.name = name
        self.lecture_d = {}

    def __str__(self):
        s = f"bachelier:{self.name}\n"
        for k, l in self.lecture_d.items():
            s += str(l)
        return s

    def create_lecture(self, lect_name):
        l = Lecture(lect_name)
        self.lecture_d[lect_name] = l

    def get_lecture(self, lect_name):
        return self.lecture_d[lect_name]


class Lecture:
    """ un cours """
    def __init__(self, name):
        self.name = name
        self.student_d = {}

    def __str__(self):
        s =  f"cours:{self.name}\n"
        for k, st in self.student_d.items():
            s += str(st)
        return s

    def register_student(self, stud_o):
        stud_name = stud_o.name
        self.student_d[stud_name] = stud_o


class Student:
    def __init__(self, name):
        self.name = name
        self.lecture_d = {}

    def __str__(self):
        return f"étudiant:{self.name}\n"

    def register_lecture(self, lect_o):
        lect_name = lect_o.name
        self.lecture_d[lect_name] = lect_o


if __name__ == '__main__':
    school_o = School("IFC")
    school_o.create_bachelor("BIG")
    school_o.create_lecture( "BIG", "Stats" )
    school_o.create_lecture( "BIG", "Algo" )
    school_o.create_lecture( "BIG", "DB" )
    school_o.register_student( "Rudy" )
    school_o.register_student( "Ali" )
    school_o.register_lecture( "BIG", "Algo", "Rudy")
    school_o.register_lecture( "BIG", "DB", "Rudy")
    school_o.register_lecture( "BIG", "Stats", "Ali")
    school_o.register_lecture( "BIG", "DB", "Ali")
    print(school_o)

