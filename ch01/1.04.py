# Start the Python interpreter and use it as a calculator. Python's syntax for
# math operations is almost the same as standard mathematical notation. For 
# example, the symbols +, - and / denote addition, subtraction and division, as 
# you would expect. The symbol for multiplication is *. If you run a 10 kilometer
# race in 43 minutes 30 seconds, what is your average time per mile? What is 
# your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).

distKm = 10.0
distMi = (distKm * (1.0 / 1.61))
seconds = ((43.0 * 60.0) + 30.0)
hours = (43.5 / 60.0)

def timePerMile(distMi, seconds):
   print seconds / distMi, 'seconds per mile'

def avgSpeed(distMi, hours):
   print distMi / hours, 'miles per hour'

timePerMile(distMi, seconds)
avgSpeed(distMi, hours)
