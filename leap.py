year = 2015
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("yes".format(year))
       else:
           print("not".format(year))
   else:
       print("yes".format(year))
else:
   print("not".format(year))
