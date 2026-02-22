

def getBondPrice_E(face, couponRate, yc):
    coupon = face * couponRate
    BondPrice = 0
    
    for t, y, in enumerate(yc, start = 1):
        if t < len(yc):
            pvcf = coupon / (1+y) ** t
        else:
            pvcf = (coupon + face)/(1+y)**t
        BondPrice += pvcf

    return(BondPrice)

print(getBondPrice_E(2000000,0.04,[0.01,0.015,0.02,0.025,0.03]))
