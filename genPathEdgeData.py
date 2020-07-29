from mechinfo import *
from CanteraChemEdgeAnalysis import *

if __name__ == "__main__":

    from Cantera import OneAtm
    readMechanism('gri30.inp')
    Nspec = numSpecies()

    # Set state
    X = [1.0 / Nspec] * Nspec
    setState(2000.0, OneAtm, X)

    # Compute reaction rates
    qf = fwdRatesOfProgress()
    qr = revRatesOfProgress()
    qnet = qf - qr

    # Decompose reactions into edges
    trElt = 'C'
    edges = getEdges(trElt)

    # Dump out nodes and edges
    print join(speciesNames())    
    for e in edges:
        valf = 0.0
        valr = 0.0
        for [r,c] in e.rateWeightList:
            valf += c*qf[r]
            valr += c*qr[r]
        print e.sp1,e.sp2,valf,-valr
