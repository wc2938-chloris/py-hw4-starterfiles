
def getBondDuration(y, face, couponRate, m, ppy = 1):
   periodic_y = y / ppy
   n = m * ppy
   coupon = face * couponRate / ppy
   
   bondPrice = 0
   weighted_sum = 0
   
   for t in range(1, n + 1):
        pv = coupon / (1 + periodic_y) ** t
        bondPrice += pv
        weighted_sum += pv * t
   
   pv_face = face / (1 + periodic_y) ** n
   bondPrice += pv_face
   weighted_sum += pv_face * n
   
   bondDuration = (weighted_sum / bondPrice) / ppy
   
   return bondDuration
   
print(getBondDuration(0.03, 2000000, 0.04, 10, 1))

