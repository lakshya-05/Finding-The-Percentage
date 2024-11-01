# Finding The Percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    # print(student_marks)

    b = student_marks[query_name]

    marks = (b[0]+b[1]+b[2])/3
    print("%0.2f" %marks)
