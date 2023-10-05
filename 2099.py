# 2099. Space Invader
# https://acm.timus.ru/problem.aspx?space=1&num=2099

# solved

import math

# There always will be line between two points
# So only problem will require two checks:
# 1. Check - does angle between lines AB and CD equal to 90 degrees
# 2. Check - does CD intersect AB after point B:
# 2.1 Find point of intersection between AB and CD
# 2.2 Find if this point lies outside of AB (or on B) and is closer to B than to A

result = 'Valid'

# 1. Check - does angle between lines AB and CD equal to 90 degrees
a_coords = input().split(' ')
b_coords = input().split(' ')
c_coords = input().split(' ')
d_coords = input().split(' ')

for i in range(len(a_coords)):
    a_coords[i] = int(a_coords[i])
    b_coords[i] = int(b_coords[i])
    c_coords[i] = int(c_coords[i])
    d_coords[i] = int(d_coords[i])

ab_vector = []
cd_vector = []

for i in range(len(a_coords)):
    ab_vector.append(b_coords[i] - a_coords[i])
    cd_vector.append(d_coords[i] - c_coords[i])

# ABx * CDx + ABy * CDy + ABz * CDz
scalar_product_ab_cd = ab_vector[0] * cd_vector[0] + ab_vector[1] * cd_vector[1] + ab_vector[2] * cd_vector[2]
# AB length = sqrt(ABx*ABx + ABy*ABy + ABz*ABz)
ab_length = math.sqrt(ab_vector[0]**2 + ab_vector[1]**2 + ab_vector[2]**2)
# CD length = sqrt(CDx*CDx + CDy*CDy + CDz*CDz)
cd_length = math.sqrt(cd_vector[0]**2 + cd_vector[1]**2 + cd_vector[2]**2)
# check - is there 90 degrees between AB and CD lines
# cos of 90 degrees is 0
cos_ab_cb = scalar_product_ab_cd/(ab_length * cd_length)
if cos_ab_cb != 0:
    result = 'Invalid'

# 2. Check - does CD intersect AB after point B

# 2.1 Find point of intersection between AB and CD
# Linear equations for vectors:
# abx = Ax + ABx * ABt
# aby = Ay + ABy * ABt
# abz = Az + ABz * ABt
# cdx = Cx + CDx * CDt
# cdy = Cy + CDy * CDt
# cdz = Cz + CDz * CDt

# N - intersection point of AB and CD
# If N exists then:
# nx = Ax + ABx * ABt = Cx + CDx * CDt
# ny = Ay + ABy * ABt = Cy + CDy * CDt
# nz = Az + ABz * ABt = Cz + CDz * CDt
# where ABt and CDt must be found first

# Ax + ABx*ABt = Cx + CDx*CDt
# Ax + ABx*ABt - Cx = CDx*CDt
# CDt = (Ax + ABx*ABt - Cx) / CDx

# Ay + ABy*ABt = Cy + CDy*CDt
# Ay + ABy*ABt = Cy + CDy*((Ax + ABx*ABt - Cx) / CDx)
# ABy*ABt = Cy - Ay + CDy*((Ax + ABx*ABt - Cx) / CDx)
# ABy*ABt = Cy - Ay + (CDy*Ax + CDy*ABx*ABt - CDy*Cx) / CDx
# ABy*ABt*CDx = Cy*CDx - Ay*CDx + CDy*Ax + CDy*ABx*ABt - CDy*Cx
# ABy*ABt*CDx - CDy*ABx*ABt = Cy*CDx - Ay*CDx + CDy*Ax - CDy*Cx
# ABt * (ABy*CDx - CDy*ABx) = Cy*CDx - Ay*CDx + CDy*Ax - CDy*Cx
# ABt = (Cy*CDx - Ay*CDx + Ax*CDy - Cx*CDy) / (ABy*CDx - CDy*ABx)

# Deal with division by zero in equation "CDt = (Ax + ABx*ABt - Cx) / CDx"

for i in range(len(cd_vector)):
    # Search for any CD vector coord (x,y,z) that is not 0 - call it i
    # for equation "CDt = (Ai + ABi*ABt - Ci) / CDi"
    if cd_vector[i] != 0:
        # Calculate ABt - we must use any coord (x,y,z) other than i - call it j
        # for equation "Aj + ABj*ABt = Cj + CDj*CDt"
        # Also check if equation "(ABy*CDx - CDy*ABx)" is 0 - then try another j to avoid division by zero
        if i == 0:
            j = 1
            if (ab_vector[j] * cd_vector[i] - ab_vector[i] * cd_vector[j]) == 0:
                j = 2

        elif i == 1:
            j = 0
            if (ab_vector[j] * cd_vector[i] - ab_vector[i] * cd_vector[j]) == 0:
                j = 2

        elif i == 2:
            j = 1
            if (ab_vector[j] * cd_vector[i] - ab_vector[i] * cd_vector[j]) == 0:
                j = 0

        abt = (cd_vector[i] * (c_coords[j] - a_coords[j]) + cd_vector[j] * (a_coords[i] - c_coords[i])) \
              / (ab_vector[j] * cd_vector[i] - ab_vector[i] * cd_vector[j])

        cdt = (a_coords[i] - c_coords[i] + ab_vector[i] * abt) / cd_vector[i]

# Get and compare all coords
# If coords are different then there is no intersection point between AB and CD
abx = a_coords[0] + ab_vector[0]*abt
cdx = c_coords[0] + cd_vector[0]*cdt
if abx != cdx:
    result = 'Invalid'

aby = a_coords[1] + ab_vector[1]*abt
cdy = c_coords[1] + cd_vector[1]*cdt
if aby != cdy:
    result = 'Invalid'

abz = a_coords[2] + ab_vector[2]*abt
cdz = c_coords[2] + cd_vector[2]*cdt
if abz != cdz:
    result = 'Invalid'

# 2.2 Find if this point lies outside of AB (or on B) and is closer to B than to A
# N - intersection point of AB and CD, so it lies on AB vector and CD vector
# There shouldn't be backward movement, so N shouldn't lie between A and B or between C and D

an_length = math.sqrt((abx - a_coords[0])**2 + (aby - a_coords[1])**2 + (abz - a_coords[2])**2)
bn_length = math.sqrt((abx - b_coords[0])**2 + (aby - b_coords[1])**2 + (abz - b_coords[2])**2)
cn_length = math.sqrt((c_coords[0] - abx)**2 + (c_coords[1] - aby)**2 + (c_coords[2] - abz)**2)
dn_length = math.sqrt((d_coords[0] - abx)**2 + (d_coords[1] - aby)**2 + (d_coords[2] - abz)**2)

# Only right answers:
# A----BN
# A----B--N
# A----B------N
if ab_length + bn_length != an_length:
    result = 'Invalid'

# Only right answers:
#       NC----D
#     N--C----D
# N------C----D
if cn_length + cd_length != dn_length:
    result = 'Invalid'

print(result)
