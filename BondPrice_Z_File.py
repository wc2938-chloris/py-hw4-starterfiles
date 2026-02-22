

def getBondPrice_Z(face, couponRate, times, yc):
    coupon = couponRate * face
    bondPrice_z = 0
    
    for t, y in zip(times, yc):
        if t < times[-1]:
            pvcf = coupon / (1+y) ** t
        else:
            pvcf = (coupon + face) / (1+y) ** t
        bondPrice_z += pvcf
            
    return(bondPrice_z)

print(getBondPrice_Z(2000000, 0.04, [1,1.5,3,4,7],[0.01,0.015,0.02,0.025,0.03]))

