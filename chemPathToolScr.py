from chemPathTool import *

if __name__ == '__main__': 

    # Make a set of test nodes/edges
    edgeVals = []
    nodes = ['sp1','sp2','sp3','sp4','sp5']
    edges = []
    for i in range(1,len(nodes)):
        edges.append((nodes[i-1],nodes[i]))
    edges.append((nodes[len(nodes)-1],nodes[0]))
    edges.append((nodes[0],nodes[3]))
    edges.append((nodes[0],nodes[2]))
    for i in range(len(edges)):
        (s1,s2) = edges[i]
        if s1 == 'sp1' or s2 == 'sp1':
            val = 0.5
            if i == 0:
                val = 2.5
            else:
                val = 1.0
            edgeVals.append((s1,s2,0.5*val,-0.15*val))

    root = Tkinter.Tk()
    Pmw.initialise(root, fontScheme = 'pmw3')
    root.title('ChemPathTool from script')
    widget = ChemPathTool(root, nodes, edgeVals, '')
    root.mainloop()
    
