# Write a program that calculates and displays the grade
# given numerical score (e.g., A, B, C, D or F)
# based on the following grading scale"
# input - score- 89
# output - B
# A: 90 - 100
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: 0 - 59

score = int(input("Enter the score\n"))
if score >=90 and score <=100:
    print("A")
elif score > 79 and score < 90:
    print("B")
elif score > 69 and score < 80:
    print("C")
elif score > 59 and score < 70:
    print("D")
elif score >= 0  and score <= 59:
    print("F")
else:
    print("Invalid score")