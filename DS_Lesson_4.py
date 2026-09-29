#conditions and Decision making
name = input("Enter your name: ")
eng = int(input("Enter the score for English: "))
maths = int(input("Enter the score for Maths: "))
kiswa = int(input("Enter the score for Kiswahili: "))
if eng > 100 or maths > 100 or kiswa > 100:
    print("Your score is out of range.!")
    exit()

total = eng + maths + kiswa
avg = total/3

if avg >= 70:
    garde = "A"
elif avg >= 60:
    garde = "B"
elif avg >= 50:
    garde = "C"
elif avg >= 40:
    garde = "D"
else:
    garde = "E"
print(name, ", the following is your performance")
print("English: ", eng)
print("Maths: ", maths)
print("Kiswahili: ", kiswa)
print("Total Marks: ", total)
print("Garde: ", garde)
