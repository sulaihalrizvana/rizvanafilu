ra1=int(input())
ra2=int(input())
ra3=int(input())
if (ra1>=ra2) and (ra1>=ra3):
   largest=ra1
elif (ra2>=ra1) and (ra2>=ra3):
   largest =ra2
else:
   largest =ra3

print("The largest number between",ra1,",",ra2,"and",ra3,"is",largest)
