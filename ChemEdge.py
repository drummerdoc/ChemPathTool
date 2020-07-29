
class Edge:
    def __init__(self,sp1,sp2,rateWeightList):
        self.sp1 = sp1
        self.sp2 = sp2
        self.rateWeightList = rateWeightList
    def equivSign(self,rhs):
        if ((self.sp1 == rhs.sp1) & (self.sp2 == rhs.sp2)):
            return 1
        else:
            if ((self.sp1 == rhs.sp2) & (self.sp2 == rhs.sp1)):
                return -1
        return 0
    def combine(self,rhs,sgn):
        if (sgn!=0):
            for [r,c] in rhs.rateWeightList:
                c = c*sgn
                self.rateWeightList.append([r,c])
    def touchesSp(self,rhs):
        if ((self.sp1 == rhs) | (self.sp2 == rhs)):
            return 1
        return 0
    def reverse(self):
        rateWeightList = []
        for [r,c] in self.rateWeightList:
            rateWeightList.append([r,-c])
        self.rateWeightList = rateWeightList
        spt = self.sp1
        self.sp1 = self.sp2
        self.sp2 = spt
        return self
    def __str__(self):
        return self.sp1 + ' <==> ' + self.sp2


if __name__ == '__main__':

    print 'Need to make a test for these'
