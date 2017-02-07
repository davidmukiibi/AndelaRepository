class CitizenIdentification(object):
    def __init__(self, name, age, gender, level):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level


class citizen(CitizenIdentification):
    def levelFinder(self):
        if 7 <= self.age < 15:

            self.level = 'PRIMARY SCHOOL LEVEL'
            return self.level

        elif 15 <= self.age < 20:

            self.level = 'SECONDARY SCHOOL LEVEL'
            return self.level

        elif 20 < self.age < 25:

            self.level = 'UNIVERSITY LEVEL'
            return self.level

        else:
            self.level = 'GRADUATE'
            return self.level

    def freeBenefits(self):

        if self.gender == 'FEMALE':
            return 'This individual should be paid a monthly stipend'
        else:
            return 'This individual should be enrolled for skills development'

    def citizenshipValidity(self):
        if self.name is not None and self.age > 20:
            return True
        else:
            return False	