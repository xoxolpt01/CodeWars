def better_than_average(class_points, your_points):
    # Your code here
    sum = 0
    for i in class_points:
        sum += i

    average = sum / len(class_points)

    if average < your_points:
        return True
    else:
        return False

print(better_than_average([24, 56, 15, 58, 6, 89, 39, 33, 12, 43, 20, 12, 70, 61, 50, 78, 93, 31, 43, 23, 23, 97, 0, 38, 68, 38, 27, 38, 80, 67,
                           35, 63, 70, 97, 49, 51, 41, 28, 26, 6, 58, 29, 27, 61, 64, 78, 57, 90, 35, 56], 37))