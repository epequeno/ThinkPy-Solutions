# Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# delimiter = '.'
# For each of the following expressions, write the value of the expression 
# and the type (of the value of the expression).
# 1. width/2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5
# 5. delimiter * 5
# Use the Python interpreter to check your answers.

# In the first case 17 is an int, by dividing an odd int into half python will
# truncate the decimal and return 8 when the accurate value of half of 17 is 
# 8.5 which is a float.

# In the second case the value is the accurate value 8.5 since we divided our 
# int by a float. If any one part of a calculation is a float the output will
# also be float.

# In the third case the value is an float since at least one part of the
# calculation is a float, the value of height.

# The fourth case is about order of operations, PEMDAS places multiplication
# at a higher priority than addition so that operation takes primacy. 2 * 5
# is calculated (10) then added to one (11). 

# Python will do want it is told. If you want 5 of '.' then what comes out 
# is '.....'

