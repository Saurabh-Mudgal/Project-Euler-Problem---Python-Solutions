def pythagorean_triplet_dickson():
    for r in range(1,1000):
        for s in range(1,r):
            if ((r**2)/2)%s == 0:
                t = (r**2/2)/s
                if r+s+r+t+r+t+s == 1000:
                    return int((r+s)*(r+t)*(r+t+s))
            s = s+1
        r = r+1

print(pythagorean_triplet_dickson())
