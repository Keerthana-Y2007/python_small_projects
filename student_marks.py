name=input("Enter student's name: ")
total=0
for i in range(1,7):
 marks=float(input(f"Enter marks for subject {i}: "))
 total+=marks/6
if total>=90:
    grade='A'
elif total>=80:
    grade='B'
elif total>=70: 
    grade='C'               
elif total>=60:
    grade='D'
else:
    grade='F'
print(f"{name} got  {total:.2f}% and grade {grade} in the exam.")   