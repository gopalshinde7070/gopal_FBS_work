#2. Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.
i=1
student=int(input("Enter the Student"))

while(i<=student):
    s1=int(input("Enter the mark  of sub1: "))
    s2=int(input("Enter the mark  of sub2: "))
    s3=int(input("Enter the mark  of sub3: "))
    s4=int(input("Enter the mark  of sub4: "))
    s5=int(input("Enter the mark  of sub5: "))
    c=s1+s2+s3+s4+s5
    mark=c/500*100
    print(mark)
    i+=1