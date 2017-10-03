def findIt(h, missingZ, stateFactor):
        #print("{}-{}-{}".format(h, missingZ, stateFactor))
        max = (2**h) - 1
        maxhalf = int(max/2)

        if missingZ == maxhalf + stateFactor:
            return max + stateFactor
        elif missingZ == maxhalf*2 + stateFactor:
            return max + stateFactor

        if missingZ < maxhalf+stateFactor:
            stateFactor += 0
        else:
            stateFactor += maxhalf

        return findIt(h-1, missingZ, stateFactor)

def answer(h, q):
    p = [None] * len(q)
    
    for missingZ in q:
        #print("{} - {}".format(missingZ,q.index(missingZ)))
        cornerCase = (2**h) - 1
        if cornerCase == missingZ:
            p[q.index(cornerCase)] = -1
        else:
            p[q.index(missingZ)] = findIt(h, missingZ, 0)

    return p

if(__name__ == '__main__'):
    #print(answer(3, [1, 4, 7]))
    #print(answer(3,[3]))
    print(answer(5,[19,14,28]))