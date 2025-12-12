import numpy as np

def main():
    filename = input("Enter marks file name: ") # asking the user for the input file

    try:  # try to open the file if we find it will open if not give an error message like cannot open file
        file = open(filename, "r")
    except:
        print("Error: cannot open file")
        return

    first = file.readline().split() # reads the first line 
    n = int(first[0])
    courseWeight = float(first[1]) / 100
    examWeight = 1 - courseWeight

    # creating a 2D array to store reg, exam, coursework and overall
    marks = np.zeros((n, 4))
    
    # read each student's data
    for i in range(n):
        reg, exam, courseWork = file.readline().split()
        exam = float(exam)
        courseWork = float(courseWork)

        # calculating overall mark
        overall = exam * examWeight + courseWork * courseWeight

        # store everything in the array
        marks[i] = [float(reg), exam, courseWork, overall]

    file.close()


    dtype = np.dtype([
        ('reg', 'i4'),
        ('exam', 'i4'),
        ('courseWork', 'i4'),
        ('overall', 'i4'),
        ('grade', 'U12')
    ])

    results = np.zeros(n, dtype=dtype)


    dist = merit = pas = fail = 0
    failed_regs = []


    for i in range(n):
        reg, exam, cw, overall = np.round(marks[i]).astype(int)

        if overall >= 70 and exam >= 65 and cw >= 65:
            grade = "Distinction"
            dist += 1
        elif overall >= 60:
            grade = "Merit"
            merit += 1
        elif overall >= 45:
            grade = "Pass"
            pas += 1
        else:
            grade = "Fail"
            fail += 1
            failed_regs.append(reg)

        results[i] = (reg, exam, cw, overall, grade)


    results.sort(order='overall')
    results = results[::-1]


    outputFile = open("output2.txt", "w")
    print(results, file=outputFile)
    outputFile.close()

    print("Distinctions:", dist)
    print("Merits:", merit)
    print("Passes:", pas)
    print("Fails:", fail)

    # it prints the failed registration numbers
    if failed_regs:  
        print("Failed registration numbers:")
        for r in failed_regs:
            print(r)


main()
