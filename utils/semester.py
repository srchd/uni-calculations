class Semester:
    def __init__(self, subjects, semID):
        self.subjects = subjects
        self.semID = semID

        if self.semID < 0:
            raise ValueError("A szemeszter ID-ja nem lehet negatív!")
        
        return
    
    def __str__(self):
        strResult = '\n' + str(self.semID + 1) + '. szemeszter:'
        for sub in self.subjects:
            strResult += str(sub)
        return strResult + '\n'
