class School:
    def __init__(self): 
        self._students = []
        self._successful_adds = []
    def add_student(self, name, grade):
        if not [oldname for _, oldname in self._students if oldname == name]:
            self._students = sorted(self._students + [(grade, name)])
            self._successful_adds.append(True)
        else:
            self._successful_adds.append(False)
    def roster(self):
        return [name for _, name in self._students]
    def grade(self, grade_number):
        return [name for grade, name in self._students if grade == grade_number]
    def added(self):
        return self._successful_adds