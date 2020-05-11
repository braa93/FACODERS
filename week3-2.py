S1=[18,17,19.5,8,25]
S2=[20,20,19,9,28]
S3=[14.5,16,13,7,23]
AH=sum(S1)
SA=sum(S2)
FA=sum(S3)
students={'Ahmad':AH, 'Sami':SA, 'Faris':FA}
B=input("Enter students name")
if B == 'Ahmad':
    print('Ahmad' ,students.get('Ahmad'))
elif B == 'Sami':
    print('Sami' ,students.get('Sami'))
elif B == 'Faris':
   print('Faris' ,students.get('Faris'))
else:
    print('Student is not recorded', 0)
