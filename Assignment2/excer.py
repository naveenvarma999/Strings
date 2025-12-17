import numpy as np


def calculate_grade(exam, coursework, overall):
    """
    Decide grade based on rounded marks.
    """
    exam_r = round(exam)
    coursework_r = round(coursework)
    overall_r = round(overall)

    if overall_r >= 70 and exam_r >= 65 and coursework_r >= 65:
        return "Distinction"
    elif overall_r >= 60:
        return "Merit"
    elif 45 <= overall_r <= 59:
        return "Pass"
    else:
        return "Fail"


def main():
    filename = input("Enter the marks file name: ")

    try:
        with open(filename, "r") as f:
            # Read first line
            first_line = f.readline().strip().split()
            n_students = int(first_line[0])
            cw_weight = float(first_line[1]) / 100.0
            exam_weight = 1.0 - cw_weight

            # Temporary array to store calculations
            arr1 = np.zeros((n_students, 4))

            # Read student data
            for i, line in enumerate(f):
                reg, exam, cw = line.split()
                reg = float(reg)
                exam = float(exam)
                cw = float(cw)

                overall = exam * exam_weight + cw * cw_weight
                arr1[i] = [reg, exam, cw, overall]

    except FileNotFoundError:
        print("Error: File not found. Program terminated.")
        return

    # Structured array for final output
    student_type = np.dtype([
        ("reg", np.int32),
        ("exam", np.int32),
        ("cw", np.int32),
        ("overall", np.int32),
        ("grade", "U12")
    ])

    students = np.zeros(n_students, dtype=student_type)

    for i in range(n_students):
        reg = int(round(arr1[i, 0]))
        exam = int(round(arr1[i, 1]))
        cw = int(round(arr1[i, 2]))
        overall = int(round(arr1[i, 3]))
        grade = calculate_grade(arr1[i, 1], arr1[i, 2], arr1[i, 3])

        students[i] = (reg, exam, cw, overall, grade)

    # Sort by overall (descending)
    students_sorted = np.sort(students, order="overall")[::-1]

    # Write to output.txt
    with open("output.txt", "w") as f:
        f.write(f"{'Reg':<8}{'Exam':<8}{'CW':<8}{'Overall':<10}{'Grade'}\n")
        f.write("-" * 45 + "\n")

        for s in students_sorted:
            f.write(f"{s['reg']:<8}{s['exam']:<8}{s['cw']:<8}{s['overall']:<10}{s['grade']}\n")

    # Summary
    print("\nSummary of results:")
    print("Distinctions:", np.sum(students["grade"] == "Distinction"))
    print("Merits:", np.sum(students["grade"] == "Merit"))
    print("Passes:", np.sum(students["grade"] == "Pass"))
    print("Fails:", np.sum(students["grade"] == "Fail"))

    failed_students = students[students["grade"] == "Fail"]["reg"]

    if len(failed_students) > 0:
        print("Failed students (registration numbers):", list(failed_students))
    else:
        print("No failed students.")


if __name__ == "__main__":
    main()
