#
# Functions to supply reaction mechanism data for use by ChemPathTool.
# These functions require the Cantera package, which is available from
# www.cantera.org.
#
# D. G. Goodwin, 8/7/02
#

from Cantera import CanteraError    
from Cantera.gases import IdealGasMix

# Store the object representing the mechanism here
class __data:
    g = None
    nsp = 0
    
def readMechanism(infile, thermo=""):
    """Read in a mechanism file."""
    g = IdealGasMix(infile, thermo)
    __data.g = g
    __data.nsp = g.nSpecies()

def setState(T, P, X):
    """Set the gas temperature [K], pressure [Pa],
    and mole fractions."""
    __data.g.setState_TPX(T, P, X)

def elementNames():
    return __data.g.elementNames()

def indexElt(elt):
    return __data.g.elementIndex(elt)

def indexSpec(elt):
    return __data.g.speciesIndex(elt)

def elementAtomicWt():
    return __data.g.atomicWeights()

def speciesNames():
    return __data.g.speciesNames()

def numberOfElementXinSpeciesY(X,Y):
    _m = __data.g.elementIndex(X)
    _k = __data.g.speciesIndex(Y)
    return __data.g.nAtoms(_k, _m)

def numSpecies():
    return __data.g.nSpecies()

def numReactions():
    return __data.g.nReactions()

def specCoeffsInReaction(r):
    """Return a list of pairs of (species name, coefficient) for reaction
    number r. Only those species with non-zero stoichiometric coefficient
    are included."""
    c = []
    for k in range(__data.nsp):
        nu = (__data.g.productStoichCoeff(k,r) -
              __data.g.reactantStoichCoeff(k,r))
        if (nu <> 0):
            c.append((__data.g.speciesName(k),nu))
    return c

def reactionString(r):
    return __data.g.reactionString(r)

def fwdRatesOfProgress():
    return __data.g.fwdRatesOfProgress()

def revRatesOfProgress():
    return __data.g.revRatesOfProgress()
            

# test
if __name__ == "__main__":

    from Cantera import OneAtm
    readMechanism('gri30.inp')
    setState(2000.0, OneAtm, [1.0]*numSpecies())
    print __data.g

    print
    print elementNames()
    print indexElt('N')
    print elementAtomicWt()

    print
    print speciesNames()
    for s in speciesNames():
        print s,':'
        for e in elementNames():
            print numberOfElementXinSpeciesY(e, s),e,
        print

    for i in range(numReactions()):
        print
        print reactionString(i)
        print specCoeffsInReaction(i)

    qf = fwdRatesOfProgress()
    qr = revRatesOfProgress()
    qnet = qf - qr
    print qf
    print qr
    print qnet
    
    

    

    
