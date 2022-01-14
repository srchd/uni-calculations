class Subject:
    def __init__(self, name, credits, grade):
        self.name = name
        self.credits = credits
        self.grade = grade
        self.failed = grade == 1

        if self.grade < 1 or self.grade > 5:
            raise ValueError("Az osztályzat nem megfelelő! (1-5)")

        return

    def __str__(self):
        return '\n' + self.name + ':\n\tKredit: ' + str(self.credits) + '\n\tJegy: ' + str(self.grade) + '\n\tBukó?(I/N): ' + ('I' if self.failed else 'N') + '\n'
