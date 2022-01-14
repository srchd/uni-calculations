import json
from utils.subject import Subject
from utils.semester import Semester
from utils.student import Student

def main():

    content = dict()
    with open('config/uni.json', 'r') as openFile:
        content = json.load(openFile)

    semesters = []
    for idx, sem in enumerate(content["semesters"]):
        subjects = []
        for sub in content["semesters"][sem]:
            subName = sub['name']
            subCreds = sub['credits']
            subGrade = sub['grade']

            subject = Subject(subName, subCreds, subGrade)
            subjects.append(subject)

        semester = Semester(subjects, idx)
        semesters.append(semester)

    student = Student(semesters)
    print(student)
    print('\n' * 4)

    okki, sems, allCreds, compCreds, subs = student.okki()

    outStr = f"A == {sems} == félév alatt:\n"
    outStr += f"\n\t == {subs} == tárgyat próbáltál meg elvégezni,\n"
    outStr += f"\t == {allCreds} == kreditet vettél fel összesen,\n"
    outStr += f"\t amiből == {compCreds} == kreditet sikerült is elvégezni.\n\n"
    outStr += f"Így az összesített korrigált kreditindexed: == {okki} ==\n"
    outStr += f"Valamint az esetlegesen megajánlott záróvizsga jegyed: == {round(okki)} =="

    print(outStr + '\n\n\n')
    input("Press ENTER to export calculations to result.txt...")

    print("Exporting to result.txt...")
    with open("result.txt", "w") as writeFile:
        writeFile.write(outStr)
    print("Exported to result.txt!")
