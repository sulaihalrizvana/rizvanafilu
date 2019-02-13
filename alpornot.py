print("Enter '0' for exit.");
ra=input("Enter any character: ");
if ra=='0':
    exit();
else:
    if((ra>='a' and ra<='z') or (ra>='A' and ra<='Z')):
    	print(ra, "is an alphabet.");
    else:
    	print(ra, "is not an alphabet.");
