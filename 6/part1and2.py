import math 
data = """Time:        46     80     78     66
Distance:   214   1177   1402   1024"""

def ways(T: int, D: int) -> int:
    t1 = (T+math.sqrt(T**2-4*D))/2
    t2 = (T-math.sqrt(T**2-4*D))/2

    return math.ceil(t1)-math.ceil(t2)

# part 1
# cba to parse the file
a = ways(46, 214)
b = ways(80, 1177)
c = ways(78, 1402)
d = ways(66, 1024)

print(a*b*c*d)

# part 2 lol
print(ways(46807866, 214117714021024))