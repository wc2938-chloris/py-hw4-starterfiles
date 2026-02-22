

def getBondPrice(y, face, couponRate, m, ppy=1):
    periodic_y = y / ppy
    n = m * ppy
    coupon = face * couponRate / ppy
    
    bondPrice = 0
    for t in range(1, n + 1):
        bondPrice += coupon / (1 + periodic_y) ** t
    bondPrice += face / (1 + periodic_y) ** n
    
    return bondPrice
