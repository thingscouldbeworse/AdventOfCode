import math

inputnum = 265149
# 1^2 3^2 5^2 7^2
# (n+(n-1))^2 outer block size
# (2n-1)^2
# finding which outer edge contains our input, probably a better way to do this...

n = 0
x = 0
while x < inputnum:
    p = 2 * n
    p = p - 1
    x = math.pow(p,2)
    n = n + 1
n = n - 1
print("n",n)
radius = n - 1
print("x",x)
print("r",radius)
print("p",p)
# find our center pieces, because these are simply r steps away from center
# then distance to center is one component, radius is second
lowest_distance = x
for i in range(0,4):
    first_center = x - math.floor(p/2) - 1
    if i == 0:
        distance = math.fabs(first_center - inputnum)
    else:
        center = x - (first_center + ((p-1)*i))
        distance = math.fabs(center - inputnum)
    if distance < lowest_distance:
        lowest_distance = distance
lowest_distance = lowest_distance - 1
print("distance to nearest center",lowest_distance)
total_distance = lowest_distance + radius
print("manhattan distance",total_distance)
