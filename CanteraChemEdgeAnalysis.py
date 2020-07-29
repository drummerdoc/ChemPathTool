from string import *
from ChemEdge import *
from mechinfo import *

class Group:
    def copy(self):
        return Group(self.mEltCnts)
    def __init__(self,eltCnts_in):
        self.mEltCnts = {}
        for elt in eltCnts_in.keys():
            self.mEltCnts[elt] = eltCnts_in[elt]
    def __sub__(self,rhs):
        val = self.copy()
        for elt in rhs.mEltCnts.keys():
            if (val.mEltCnts.has_key(elt)):
                res = val.mEltCnts[elt] - rhs.mEltCnts[elt]
                if (res != 0):
                    val.mEltCnts[elt] = res
                else:
                    del val.mEltCnts[elt]
            else:
                val.mEltCnts[elt] = - rhs.mEltCnts[elt]
        return val
    def __mul__(self,rhs):
        val = self.copy()
        for elt in val.mEltCnts.keys():
            val.mEltCnts[elt] = rhs * val.mEltCnts[elt]
        return val        
    def __rmul__(self,lhs):
        val = self.copy()
        for elt in val.mEltCnts.keys():
            val.mEltCnts[elt] = lhs * val.mEltCnts[elt]
        return val
    def __str__(self):
        val = 'Group < '
        for elt in self.mEltCnts.keys():
            val = val + elt + ':' + str(self.mEltCnts[elt]) + ' '
        val = val + '>'
        return val
    def __getitem__(self,elt):
        if self.contains(elt):
            return self.mEltCnts[elt]
        return 0
    def sameSign(self):
        keys = self.mEltCnts.keys()
        if (len(keys) > 0):
            if (self.mEltCnts[keys[0]] < 0):
                for elt in keys:
                    if (self.mEltCnts[elt] > 0):
                        return 0
            else:
                for elt in keys:
                    if (self.mEltCnts[elt] < 0):
                        return 0            
        return 1
    def contains(self,elt):
        return self.mEltCnts.has_key(elt)
    def awt(self):
        awt = 0
        for elt in self.mEltCnts.keys():
            awtElt = elementAtomicWt()[indexElt(elt)]
            awt = awt + abs(self.mEltCnts[elt])*awtElt
        return awt
    def size(self):
        return len(self.mEltCnts)

def getEdges(trElt):
    edges = []
    groups = {}
    for sp in speciesNames():
        eltCnts = {}
        for elt in elementNames():
            m = numberOfElementXinSpeciesY(elt,sp)
            if (m>0):
                eltCnts[elt] = m
        groups[sp] = Group(eltCnts)

    for r in range(numReactions()):
        Redges = []
        coeffs = specCoeffsInReaction(r)
        net = {}
        for (sp,co) in coeffs:
            if (net.has_key(sp)):
                net[sp] = net[sp] + co
                if (net[sp]==0):
                    del net[sp]
            else:
                net[sp] = co

        reac = []
        prod = []
        for sp in net.keys():
            if (net[sp] < 0):
                if (numberOfElementXinSpeciesY(trElt,sp)>0):
                    reac.append([sp,-net[sp]])
            else:
                if (numberOfElementXinSpeciesY(trElt,sp)>0):
                    prod.append([sp,net[sp]])

        LR = len(reac)
        LP = len(prod)
        # no tr-containing species in reac
        if (LR == 0 | LP == 0):
            continue
        # exactly one tr-containing species either side
        if ((LR <= 1) | (LP <= 1)):
            for spr in reac:
                [spcr,cor] = spr
                for spp in prod:
                    [spcp,cop] = spp
                    w = min(cor*groups[spcr][trElt],cop*groups[spcp][trElt])
                    Redges.append(Edge(spcr,spcp,[[r,w]]))
        else:
            # two tr-containing species each side
            if (LR == 2 & LP == 2):
                [rs0,rc0] = reac[0]
                [rs1,rc1] = reac[1]
                [ps0,pc0] = prod[0]
                [ps1,pc1] = prod[1]

                b0 = pc0*groups[ps0] - rc0*groups[rs0]
                b1 = pc1*groups[ps1] - rc0*groups[rs0]
                pick = 0

                if (b0.sameSign() & b1.sameSign()):
                    if (b1.size() < b0.size()):
                        pick = 1
                        
                    if (b1.size() == b0.size()):
                        if (b0.awt() > b1.awt()):
                            pick = 1
                else:
                    if (b1.sameSign()):
                        pick = 1

                nR0 = rc0*groups[rs0][trElt]
                nR1 = rc1*groups[rs1][trElt]
                nP0 = pc0*groups[ps0][trElt]
                nP1 = pc1*groups[ps1][trElt]

                if (pick == 0):
                    Redges.append(Edge(rs0,ps0,[[r,min(nR0,nP0)]]))
                    if (nP0<nR0):
                        Redges.append(Edge(rs0,ps1,[[r,nR0-nP0]]))
                    if (nR0<nP0):
                        Redges.append(Edge(rs1,ps0,[[r,nP0-nR0]]))
                    Redges.append(Edge(rs1,ps1,[[r,min(nR1,nP1)]]))
                else:
                    Redges.append(Edge(rs0,ps1,[[r,min(nR0,nP1)]]))
                    if (nP1<nR0):
                        Redges.append(Edge(rs0,ps0,[[r,nR0-nP1]]))
                    if (nR0<nP1):
                        Redges.append(Edge(rs1,ps1,[[r,nP1-nR0]]))
                    Redges.append(Edge(rs1,ps0,[[r,min(nR1,nP0)]]))

            else:
                print 'Cannot decompose rxn: ',r,': ',reactionString(r)

#        line = '(%3d) %-25s: ' % (r+1,reactionString(r))
#        for edge in Redges:
#            [rxn,c] = edge.rateWeightList[0]
#            line = line + '%5s==>%-5s (%d)  ' % (edge.sp1,edge.sp2,c)
#        print line

        for edge in Redges:
            edges.append(edge)

# Uniqueify edges
    edgesNew = []
    while (len(edges)!=0):
        edgesNew.append(edges[0])
        del edges[0]
        N = len(edges)
        i = 0
        while (i < N):
            e = edgesNew[len(edgesNew)-1]
            e1 = edges[i]
            sgn = e.equivSign(e1)
            if (sgn!=0):
                e.combine(e1,sgn)
                del edges[i]
                N = len(edges)
            else:
                i = i+1
    return edgesNew

if __name__ == '__main__':

    print 'Need to make a test for these'
