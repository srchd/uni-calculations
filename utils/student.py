class Student:
    def __init__(self, semesters):
        self.semesters = semesters

    def __str__(self):
        strResult = '\n' + 'Egyetemi aktivitas: '
        for sem in self.semesters:
            strResult += str(sem)
        return strResult

    def okki(self):
        semesters = len(self.semesters)
        sum_creds = 0
        completed_creds = 0
        all_creds = 0
        all_subjects = 0
        for sem in self.semesters:
            for sub in sem.subjects:
                sum_creds += sub.credits * sub.grade
                all_subjects += 1
                if sub.grade != 1:
                    completed_creds += sub.credits

                all_creds += sub.credits

        part_one = sum_creds / (semesters * 30)
        part_two = completed_creds / all_creds

        result = part_one * part_two

        return result, semesters, all_creds, completed_creds, all_subjects
