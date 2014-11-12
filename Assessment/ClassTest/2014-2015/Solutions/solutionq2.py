"""
Solution to question 2 of class test

Marking for this question will be lenient with marks given for methodology and 'almost working' answers.
"""

fle = open('output.txt', 'w')  # Open file

### 5 marks for correctly opening the file.

for k in range(500):  # Marks given even if range is of by 1
    fle.write('%s\n' % (4 * k + 1))  # Some students might forget the next line character (lost some but not all marks)

fle.close()
### 25 marks for the above (if they forget to close the file that's ok)


## Student might also create the list separately:

data = [4 * k + 1 for k in range(500)]  # They might use a loop instead of a list comprehension (if they do that or indeed this, that's completely fine)
for n in data:
    fle.write('%s\n' % n)

fle.close()
