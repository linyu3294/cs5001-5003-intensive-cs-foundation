'''   
	 Yu Lin
   CS5001 - Spring 2019
   Handling read/write files
   Feb 19, 2019 
'''

# Open the file for reading and populate
# grades list with original data
try:
    infile = open('grades.txt', 'r')
    lines = infile.read()
    grades = lines.splitlines()
    infile.close()

except OSError:
    print('Error opening grades.txt for reading')
    return

# Modify grades by adding .5 to each one
rounded_grades = []
for grade in grades:
   mod_grade = float(grade) + .5
   rounded_grades.append(mod_grade)

# Open the same file for writing
# and publish updated grades
try:
   outfile = open('grades.txt', 'w')
   for grade in rounded_grades:
       outfile.write(str(grade) + '\n')
   outfile.close()

except OSError:
   print('Error opening grades.txt for writing')
   return

