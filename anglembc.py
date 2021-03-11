
import math

a =  int(input())
b =  int(input())
M = math.sqrt(a**2 + b**2)
theta = math.acos(b/M)
print(str(round(math.degrees(theta))) + '°' )