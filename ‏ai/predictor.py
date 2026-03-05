async def predict(rows):

    right = {}
    left = {}

    for r in rows:

        rr = r["right_result"]
        ll = r["left_result"]

        right[rr] = right.get(rr,0)+1
        left[ll] = left.get(ll,0)+1

    if not right:
        return ("زوجين",50),("لاشيء",50)

    best_r = max(right,key=right.get)
    best_l = max(left,key=left.get)

    pr = int(right[best_r]/len(rows)*100)
    pl = int(left[best_l]/len(rows)*100)

    return (best_r,pr),(best_l,pl)
