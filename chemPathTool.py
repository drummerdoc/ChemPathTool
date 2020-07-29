from Tkinter import *
import Pmw
import math
import cPickle
import sys
from tkFileDialog import *
from tkFont import *
from MyPmwRadioSelect import *
from string import *

# Note: The following license text appears both in this file,
# and during operation of the ChemPathTool by selecting the
# "Help->Show License Agreement" menu item.

licenseText = '\
NON-COMMERCIAL SOURCE  CODE  LICENSE  AGREEMENT \
\n\n \
Software: ChemPathTool \
\n \
Version:  1.0 \
\n\n \
IMPORTANT - READ CAREFULLY: \
\n \
This License Agreement ("Agreement") is a \
legal agreement between you (in your capacity as an individual and as \
an agent for your company, institution or other entity) and The \
Regents of the University of California, Department of Energy \
contract-operators of the Ernest Orlando Lawrence Berkeley National \
Laboratory ("Berkeley Lab").  Downloading, installing, using, or \
copying of the Software (as defined below) by you or by a third party \
on your behalf indicates your agreement to be bound by the terms and \
conditions of this Agreement.  If you do not agree to these terms and \
conditions, do not download, install or use the Software. \
\n\n \
1. LICENSE GRANT. Berkeley Lab grants you, and you hereby accept, a \
non-exclusive, royalty-free perpetual license to install, use, modify, \
prepare derivative works, incorporate into other computer software, \
and distribute the version noted above of the computer software \
program noted above, in binary and source code format, or any \
derivative work thereof, together with any associated media, printed \
materials, and on-line or electronic documentation (if any) provided \
by Berkeley Lab (collectively, the "Software") for non-commercial \
research and development purposes only, subject to the following terms \
and conditions: (i) any distribution of the Software shall bind the \
receiver to the terms and conditions of this Agreement; (ii) any \
distribution of the Software in modified form shall clearly state that \
the Software has been modified from the version originally obtained \
from Berkeley Lab.  This version of the Software constitutes a \
research prototype and may be changed substantially.  The license \
grant set forth above is subject to receipt by Berkeley Lab of any \
required U.S.  Department of Energy approvals. \
\n\n \
2. COPYRIGHT; RETENTION OF RIGHTS.  The above license grant is \
conditioned on the following: (i) you must reproduce all copyright \
notices and other proprietary notices on any copies of the Software \
and you must not remove such notices; (ii) in the event you compile \
the Software, you will include the copyright notice with the binary in \
such a manner as to allow it to be easily viewable; (iii) if you \
incorporate the Software into other code, you must provide notice that \
the code contains the Software and include a copy of the copyright \
notices and other proprietary notices.  All copies of the Software \
shall be subject to the terms of this Agreement.  Subject to approval \
by the U.S. Department of Energy: (a) you hereby acknowledge that the \
Software is protected by United States copyright law and international \
treaty provisions; (b) Berkeley Lab, and its licensors (if any), \
hereby reserve all rights in the Software which are not explicitly \
granted to you herein; (c) without limiting the generality of the \
foregoing, Berkeley Lab and its licensors retain all title, copyright, \
and other proprietary interests in the Software and any copies \
thereof, and you do not acquire any rights, express or implied, in the \
Software, other than those specifically set forth in this Agreement. \
\n\n \
3. NO MAINTENANCE OR SUPPORT; TREATMENT OF ENHANCEMENTS YOU CHOOSE TO \
PROVIDE TO BERKELEY LAB.  Berkeley Lab is under no obligation \
whatsoever to: (i) provide maintenance or support for the Software; or \
(ii) to notify you of bug fixes, patches, or upgrades to the features, \
functionality or performance of the Software ("Enhancements") (if \
any), whether developed by Berkeley Lab or third parties.  If, in its \
sole discretion, Berkeley Lab makes an Enhancement available to you \
and Berkeley Lab does not separately enter into a written license \
agreement with you relating to such bug fix, patch or upgrade, then it \
shall be deemed incorporated into the Software and subject to this \
Agreement.  You are under no obligation whatsoever to provide any \
Enhancements to Berkeley Lab or the public that you may develop over \
time; however, if you choose to provide your Enhancements to Berkeley \
Lab, or if you choose to otherwise publish or distribute your \
Enhancements, in source code form without contemporaneously requiring \
end users or Berkeley Lab to enter into a separate written license \
agreement for such Enhancements, then you agree to promptly provide \
such Enhancements to Berkeley Lab and you hereby grant Berkeley Lab a \
non-exclusive, royalty-free perpetual license to install, use, modify, \
prepare derivative works, incorporate into the Software or other \
computer software, distribute, and sublicense your Enhancements or \
derivative works thereof, in binary and source code form. \
\n\n \
4. U.S. GOVERNMENT RIGHTS.  The Software was developed under funding \
from the U.S. Department of Energy and the U.S. Government \
consequently retains certain rights as follows: the U.S. Government \
has been granted for itself and others acting on its behalf a paid-up, \
nonexclusive, irrevocable, worldwide license in the Software to \
reproduce, prepare derivative works, and perform publicly and display \
publicly.  Beginning five (5) years after the date permission to \
assert copyright was granted by the U.S. Dept. of Energy, and subject \
to any subsequent five (5) year renewals, the U.S.  Government is \
granted for itself and others acting on its behalf a paid-up, \
nonexclusive, irrevocable, worldwide license in the Software to \
reproduce, prepare derivative works, distribute copies to the public, \
perform publicly and display publicly, and to permit others to do so. \
\n\n \
5. WARRANTY DISCLAIMER.  THE SOFTWARE IS SUPPLIED "AS IS" WITHOUT \
WARRANTY OF ANY KIND.  BERKELEY LAB, ITS LICENSORS, THE UNITED STATES, \
THE UNITED STATES DEPARTMENT OF ENERGY, AND THEIR EMPLOYEES: (1) \
DISCLAIM ANY WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED \
TO ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR \
PURPOSE, TITLE OR NON-INFRINGEMENT, (2) DO NOT ASSUME ANY LEGAL \
LIABILITY OR RESPONSIBILITY FOR THE ACCURACY, COMPLETENESS, OR \
USEFULNESS OF THE SOFTWARE, (3) DO NOT REPRESENT THAT USE OF THE \
SOFTWARE WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS, (4) DO NOT WARRANT \
THAT THE SOFTWARE WILL FUNCTION UNINTERRUPTED, THAT IT IS ERROR-FREE \
OR THAT ANY ERRORS WILL BE CORRECTED. \
\n\n \
6. LIMITATION OF LIABILITY. IN NO EVENT WILL BERKELEY LAB OR ITS \
LICENSORS BE LIABLE FOR ANY INDIRECT, INCIDENTAL, CONSEQUENTIAL, \
SPECIAL OR PUNITIVE DAMAGES OF ANY KIND OR NATURE, INCLUDING BUT NOT \
LIMITED TO LOSS OF PROFITS OR LOSS OF DATA, FOR ANY REASON WHATSOEVER, \
WHETHER SUCH LIABILITY IS ASSERTED ON THE BASIS OF CONTRACT, TORT \
(INCLUDING NEGLIGENCE OR STRICT LIABILITY), OR OTHERWISE, EVEN IF \
BERKELEY LAB HAS BEEN WARNED OF THE POSSIBILITY OF SUCH LOSS OR \
DAMAGES.  IN NO EVENT SHALL BERKELEY LABS LIABILITY FOR DAMAGES \
ARISING FROM OR IN CONNECTION WITH THIS AGREEMENT EXCEED THE AMOUNT \
PAID BY YOU FOR THE SOFTWARE. \
\n\n \
7. INDEMNITY.  You shall indemnify, defend, and hold harmless Berkeley \
Lab, the U.S. Government, the Software developers, the Software \
sponsors, and their agents, officers, and employees, against any and \
all claims, suits, losses, damage, costs, fees, and expenses arising \
out of or in connection with this Agreement.  You shall pay all costs \
incurred by Berkeley Lab in enforcing this provision, including \
reasonable attorney fees. \
\n\n \
8. TERM AND TERMINATION.  The license granted to you under this \
Agreement will continue perpetually unless terminated by Berkeley Lab \
in accordance with this Agreement.  If you breach any term of this \
Agreement, and fail to cure such breach within thirty (30) days of the \
date of written notice, this Agreement shall immediately \
terminate. Upon such termination, you shall immediately cease using \
the Software, return to Berkeley Lab, or destroy, all copies of the \
Software, and provide Berkeley Lab with written certification of your \
compliance with the foregoing.  Termination shall not relieve you from \
your obligations arising prior to such termination. Notwithstanding \
any provision of this Agreement to the contrary, Sections 5 through 11 \
shall survive termination of this Agreement. \
\n\n \
9. EXPORT CONTROLS. You shall observe all applicable United States and \
foreign laws and regulations (if any) with respect to the export, \
re-export, diversion or transfer of the Software, related technical \
data and direct products thereof, including, without limitation, the \
International Traffic in Arms Regulations (ITAR) and the Export \
Administration Regulations. \
\n\n \
10. NO ENDORSEMENT.  In accordance with California Education Code \
Section 92000, you shall not use in advertising, publicity or other \
promotional activities any name, trade name, trademark, or other \
designation of the University of California, nor shall you so use \
"Ernest Orlando Lawrence Berkeley National Laboratory" or "United \
States Department of Energy" (including any contraction, abbreviation, \
or simulation of any of the foregoing) without Berkeley Lab\'s prior \
written consent. \
\n\n \
11. GENERAL.  This Agreement shall be governed by the laws of the \
State of California, excluding its rules governing conflicts of laws. \
No provision in either party\'s purchase orders, or in any other \
business forms employed by either party will supersede the terms of \
this Agreement, and no modification or amendment of this Agreement is \
binding, unless in writing signed by a duly authorized representative \
of each party.  This Agreement is binding upon and shall inure to the \
benefit of Berkeley Lab, its successors and assigns.  This Agreement \
represents the entire understanding of the parties, and supersedes all \
previous communications, written or oral, relating to the subject of \
this Agreement. If you have any questions concerning this license, \
contact Lawrence Berkeley National Laboratory, Technology Transfer \
Department, One Cyclotron Road, MS 90R1070, Berkeley, CA 94720, Attn: \
Software Licensing or via e-mail at TTD@lbl.gov. (rev 010903)'

class GraphData:
    def __init__(self):
        self.NODERADIUS = 25
        self.CANVASSIZEX = 700
        self.CANVASSIZEY = 700
        self.MAXEDGEWIDTH = 20
        self.DOUBLEARROWSPACING = .2
        self.arrowShape = (5,10,5)
        self.FONTFAMILY = 'helvetica'
        self.FONTWEIGHT = NORMAL
        self.NODEWIDTH = 1
        self.OPTIMIZEFONTSIZE = 1
        self.DEFAULTFONTSIZE = 14

gd = GraphData()

nodeMap = {}
edgeMap = {}
colorizeMap = {'Monochrome':0,'Dataset':1}
colorizeEdges = colorizeMap['Monochrome']

def r2dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

# this is a simple if stupid color map
def colorMap(num):
    global colorizeMap, colorizeEdges
    if colorizeEdges == colorizeMap['Monochrome']:
        return "#%02x%02x%02x" % (0,0,0)
    r = int(256*num)
    if r==256:
	r = 255
    b = 255-r
    g = 0
    return "#%02x%02x%02x" % (r,g,b)

class GraphNode:
    def __init__(self,canvasobj,x,y,fg,bg,name):
        self.radius = gd.NODERADIUS
        self.x = x
        self.y = y
        self.xc = x + self.radius
        self.yc = y + self.radius
        self.x2 = x + 2*self.radius
        self.y2 = y + 2*self.radius
        self.fg = fg
        self.bg = bg
        self.canvas = canvasobj
        self.edgeList = []
	self.name = name
        self.width = gd.NODEWIDTH
        global nodeMap
        nodeMap[name] = self
        self.show()
    def erase(self):
        self.canvas.delete(self.oval)
        self.canvas.delete(self.label)
    def show(self):
        self.oval = self.canvas.create_oval(self.x,self.y,self.x2,self.y2,
                                            width=self.width)
        f = Font(family=gd.FONTFAMILY, size=gd.FONTSIZE, weight=gd.FONTWEIGHT)
        self.label = self.canvas.create_text(self.xc,self.yc,text=self.name,font=f)
    def adjacentPaths(self):
        adjacentPaths = []
	for (x,y,rate) in self.edgeList:
            adjacentPaths.append(rate)
        return adjacentPaths
    def destroy(self):
        global nodeMap
        del nodeMap[self.name]
    def contains(self,id):
        if self.oval == id or self.label == id:
            return 1
        else:
            return None
    def move(self,incx,incy):
        self.x = self.x+incx
        self.y = self.y+incy
        self.x2 = self.x2+incx
        self.y2 = self.y2+incy
        self.xc = self.xc+incx
        self.yc = self.yc+incy
        self.erase()
        self.show()
        self.moveEdges(incx,incy)
    def moveEdges(self,incx,incy):
        for (offx,offy,rate) in self.edgeList:
            rate.moveEnd(self,incx,incy)

class PairTag:
    def __init__(self,sp1,sp2):
        self.sp1 = sp1
        self.sp2 = sp2
        self.string = sp1 + '<->' + sp2
    def __str__(self):
        return self.string
    def __cmp__(self,rhs):
        return (self.string == rhs.string)
        

class GraphEdge:
    def __init__(self,pd,sp1,sp2,weight,doShow,coalesce,normEdgeVal):
        self.pd = pd
        self.canvas = pd.draw
        self.node0 = sp1
        self.node1 = sp2
        self.strengthSF = gd.MAXEDGEWIDTH
        self.strength = weight
        global nodeMap
        gn1 = nodeMap[sp1]
        self.x0 = 0.5*(gn1.x + gn1.x2)
        self.y0 = 0.5*(gn1.y + gn1.y2)
        gn2 = nodeMap[sp2]
        self.x1 = 0.5*(gn2.x + gn2.x2)
        self.y1 = 0.5*(gn2.y + gn2.y2)
        self.fg = colorMap(1)
        self.bg = colorMap(1)
        gn1.edgeList.append((self.x0-gn1.x,self.y0-gn1.y,self))
        gn2.edgeList.append((self.x0-gn2.x,self.y0-gn2.y,self))
        self.coalesce = coalesce
        self.currentScaleVal = normEdgeVal
        self.lines = []
        self.show()
        global edgeMap
        self.tag = str(PairTag(sp1,sp2))
        edgeMap[self.tag] = self

    def show(self):
        if self.coalesce:
            self.showOneEdge()
        else:
            self.showTwoEdges()
        
    def drawArrow(self,x1,y1,x2,y2,w,val):
        color=colorMap(val)
        if (w>0):
            return self.canvas.create_line(x1,y1,x2,y2,width=w,
                                           arrow='last',fill=color,
                                           arrowshape=gd.arrowShape)
        else:
            return self.canvas.create_line(x2,y2,x1,y1,width=-w,
                                           arrow='last',fill=color,
                                           arrowshape=gd.arrowShape)

    def showOneEdge(self):
        self.currentScaleVal = self.pd.getNormEdgeVal()
        showEdge = 1
        sum = 0.0
        for val in self.strength:
            sum = sum + val
        if abs(sum*100/self.currentScaleVal) < self.pd.showEdgeFraction:
            showEdge = 0
            
        if showEdge:
            DX = self.x1 - self.x0
            DY = self.y1 - self.y0
            DD = math.sqrt(DX*DX + DY*DY)
            global nodeMap
            n0 = nodeMap[self.node0]
            s = n0.radius/max(1,DD)
            x0 = self.x0+s*DX
            y0 = self.y0+s*DY

            n1 = nodeMap[self.node1]
            s = n1.radius/max(1,DD)
            x1 = self.x1 - s*DX
            y1 = self.y1 - s*DY

            w0 = self.strength[0]
            if (len(self.strength)>1):
                w0 = w0 + self.strength[1]
            w0 = w0*self.strengthSF/self.currentScaleVal

            self.lines.append(self.drawArrow(x0,y0,x1,y1,w0,0))
            
    def showTwoEdges(self):
        self.currentScaleVal = self.pd.getNormEdgeVal()
        showEdge = []
        showAny = 0
        for i in range(len(self.strength)):
            showEdge.append(0)
            val = self.strength[i]
            if abs(val*100/self.currentScaleVal) >= self.pd.showEdgeFraction:
                showEdge[-1] = 1
                showAny = 1

        if showAny:
            # compute intersection with graph nodes
            DX = self.x1 - self.x0
            DY = self.y1 - self.y0
            DD = math.sqrt(DX*DX + DY*DY)
            if DD > 0:
                global nodeMap
                n0 = nodeMap[self.node0]
                s = n0.radius/DD
                x0 = self.x0 + s*DX
                y0 = self.y0 + s*DY

                n1 = nodeMap[self.node1]
                s = n1.radius/DD
                x1 = self.x1 - s*DX
                y1 = self.y1 - s*DY

                w0 = showEdge[0]*self.strength[0]*self.strengthSF/self.currentScaleVal
                if (len(self.strength)==1):
                    if abs(w0) > 0:
                        self.lines.append(self.drawArrow(x0,y0,x1,y1,w0,0))
                else:
                    w1 = showEdge[1]*self.strength[1]*self.strengthSF/self.currentScaleVal
                    ws = 0.5*(n0.radius+n1.radius)*gd.DOUBLEARROWSPACING

                    if (w0 == 0) | (w1 == 0):
                        ws = 0
                        
                    wh = 0.5*(ws + abs(w1))
                    wl = 0.5*(ws + abs(w0))
                    
                    x0l = x0 - DY/DD*wh
                    y0l = y0 + DX/DD*wh
                    x1l = x1 - DY/DD*wh
                    y1l = y1 + DX/DD*wh
                    if abs(w0) > 0:
                        self.lines.append(self.drawArrow(x0l,y0l,x1l,y1l,w0,0))
                    
                    x0h = x0 + DY/DD*wl
                    y0h = y0 - DX/DD*wl
                    x1h = x1 + DY/DD*wl
                    y1h = y1 - DX/DD*wl
                    if abs(w1) > 0:
                        self.lines.append(self.drawArrow(x0h,y0h,x1h,y1h,w1,1))
                    
    def erase(self):
        for line in self.lines:
            self.canvas.delete(line)
        for line in self.lines:
            self.lines.remove(line)

    def destroy(self):
        global edgeMap, nodeMap
        for sp in nodeMap.keys():
            el = nodeMap[sp].edgeList
            for (x,y,rate) in el:
                if (rate == self):
                    el.remove((x,y,rate))
        del edgeMap[self.tag]
    def contains(self,id):
        if self.origpt == id or self.endpt == id:
            return 1
        else:
            return None
    def moveEnd(self,specbox,incx,incy):
        name = specbox.name
        if name == self.node0:
            self.x0 = self.x0+incx
            self.y0 = self.y0+incy
        elif name == self.node1:
            self.x1 = self.x1+incx
            self.y1 = self.y1+incy
        else:
            raise AssertionError,'improper network connection'
        self.erase()
        self.show()

# this is a proxy for a name box.  The problem is that I cant pickle a 
# GraphNode directly because it contains Tkintr objects....
class ProxyGraphNode:
    def __init__(self,gn):
        self.x = gn.x
        self.y = gn.y
        self.x2 = gn.x2
        self.y2 = gn.y2
        self.fg = gn.fg
        self.bg = gn.bg
        self.name = gn.name
        # this is the tricky inverse link so I can find out what points to what
        gn.ilink = self
    def initGraphNode(self,gn):
        gn.x = self.x
        gn.y = self.y
        gn.x2 = self.x2
        gn.y2 = self.y2
        gn.xc = 0.5*(self.x+self.x2)
        gn.yc = 0.5*(self.y+self.y2)
        gn.fg = self.fg
        gn.bg = self.bg
        # set inverse link
        self.ilink = gn
        return gn
        
class ProxyGraphEdge:
    def __init__(self,rp):
        self.x0 = rp.x0
        self.y0 = rp.y0
        self.x1 = rp.x1
        self.y1 = rp.y1
        self.fg = rp.fg
        self.bg = rp.bg
        self.node0 = rp.node0
        self.node1 = rp.node1
        self.tag = rp.tag
        # this is the tricky inverse link....
        rp.ilink = self

class ChemPathTool:
    def __init__(self,parent,nodes,edgeTups,label):
        self.canvasSizeX = gd.CANVASSIZEX
        self.canvasSizeY = gd.CANVASSIZEY
        self.parent = parent
        self.selObj = None
        self.rubberbandBox = None
        self.initialize(nodes,edgeTups)
        self.showEdgeFraction = 20
        self.epsFile = ''
        self.layFile = ''
        self.multObjs = []
        self.lockedNodes = []
        self.newNodeCntr = 0
        self.coalesceMap = {'Separate Fwd/Rev':0, 'Coalesce Fwd/Rev':1}
        self.oneOrTwoCB('Separate Fwd/Rev')
        self.normalizeMap = {'Normalize to Max':1, 'Use Raw values':0}
        self.normalizeEdges = self.normalizeMap['Normalize to Max']
        self.canvasLabel = None
        self.canvasLabelText = label
        self.mansetLabelText = label
        self.datasetLabelText = label
        self.buildWidgets(parent) 
        self.toggleVar.set(1)
        self.toggleLabel()

    def initialize(self,nodes,edgeTups):
        self.allAvailNodes = []
        for node in nodes:
            self.allAvailNodes.append(node)
        if gd.OPTIMIZEFONTSIZE == 1:
            gd.FONTSIZE = self.optimizeFontSize()
        else:
            gd.FONTSIZE = gd.DEFAULTFONTSIZE
        self.allAvailEdges=[]
        self.allAvailEdgeWeights = {}
        self.tagToPair = {}
        self.maxEdgeSum = 0.0
        self.maxEdgeVal = 0.0
        for i in range(len(edgeTups)):
            s1,s2,val = edgeTups[i][0],edgeTups[i][1],edgeTups[i][2:]
            edge = (s1,s2)
            sum = 0
            for v in val:
                 sum = sum + v
                 self.maxEdgeVal = max(self.maxEdgeVal,abs(v))
            self.maxEdgeSum = max(abs(sum),self.maxEdgeSum)
            self.allAvailEdges.append(edge)
            self.allAvailEdgeWeights[edge] = val
            self.tagToPair[str(PairTag(s1,s2))] = [s1,s2]

    def optimizeFontSize(self):
        # For some reason, this seems to take a long time on Linux machines.
        # Shut of the OPTIMIZEFONTSIZE switch if this bothers you...
        size = 20
        while size > 4:
            f = Font(family=gd.FONTFAMILY, size=size, weight=gd.FONTWEIGHT)
            maxsize = 0
            for name in self.allAvailNodes:
                maxsize = max(maxsize,f.measure(name))
            if maxsize > 2*gd.NODERADIUS-2:
                size=size-1
            else:
                break
        return size

    def doNothing(self,event):
        pass

    def bindMouse(self):
	Widget.bind(self.draw, "<Button-1>", self.mouse1Down)
 	Widget.bind(self.draw, "<Button1-Motion>", self.mouse1Move)
	Widget.bind(self.draw, "<Button1-ButtonRelease>", self.mouse1Up)
	Widget.bind(self.draw, "<Button-2>", self.mouse2Down)
	Widget.bind(self.draw, "<Button-3>", self.mouse3Down)
	Widget.bind(self.draw, "<Shift-Button-1>", self.multiSelect)
	Widget.bind(self.draw, "<Shift-Button-2>", self.doNothing)
	Widget.bind(self.draw, "<Shift-Button-3>", self.doNothing)
	Widget.bind(self.draw, "<Control-a>", self.selectAll)
	Widget.bind(self.draw, "<Control-l>", self.lockNodes)
	Widget.bind(self.draw, "<Control-L>", self.unlockNodes)
	Widget.bind(self.draw, "<Control-Key-1>", self.alignInX)
	Widget.bind(self.draw, "<Control-Key-2>", self.alignInY)
	Widget.bind(self.draw, "<Control-Key-3>", self.distribInX)
	Widget.bind(self.draw, "<Control-Key-4>", self.distribInY)
	Widget.bind(self.draw, "<Left>", self.nudgeXm)
	Widget.bind(self.draw, "<Right>", self.nudgeXp)
	Widget.bind(self.draw, "<Down>", self.nudgeYp)
	Widget.bind(self.draw, "<Up>", self.nudgeYm)
	Widget.bind(self.draw, "<Shift-Left>", self.nudgeXM)
	Widget.bind(self.draw, "<Shift-Right>", self.nudgeXP)
	Widget.bind(self.draw, "<Shift-Down>", self.nudgeYP)
	Widget.bind(self.draw, "<Shift-Up>", self.nudgeYM)

    def unbindMouse(self):
	Widget.bind(self.draw, "<Button-1>", self.doNothing)
 	Widget.bind(self.draw, "<Button1-Motion>", self.doNothing)
	Widget.bind(self.draw, "<Button1-ButtonRelease>", self.doNothing)
	Widget.bind(self.draw, "<Button-2>", self.doNothing)
	Widget.bind(self.draw, "<Button-3>", self.doNothing)
	Widget.bind(self.draw, "<Shift-Button-1>", self.doNothing)
	Widget.bind(self.draw, "<Shift-Button-2>", self.doNothing)
	Widget.bind(self.draw, "<Shift-Button-3>", self.doNothing)
	Widget.bind(self.draw, "<Control-a>", self.doNothing)
	Widget.bind(self.draw, "<Control-l>", self.doNothing)
	Widget.bind(self.draw, "<Control-L>", self.doNothing)
	Widget.bind(self.draw, "<Left>", self.doNothing)
	Widget.bind(self.draw, "<Right>", self.doNothing)
	Widget.bind(self.draw, "<Down>", self.doNothing)
	Widget.bind(self.draw, "<Up>", self.doNothing)
	Widget.bind(self.draw, "<Shift-Left>", self.doNothing)
	Widget.bind(self.draw, "<Shift-Right>", self.doNothing)
	Widget.bind(self.draw, "<Shift-Down>", self.doNothing)
	Widget.bind(self.draw, "<Shift-Up>", self.doNothing)

    def buildWidgets(self,parent):

	# Create the dialog.
	self.dialog = Pmw.Dialog(parent,
	    buttons = ('OK', 'Apply', 'Cancel'),
	    defaultbutton = 'OK',
	    title = 'Set Canvas Label',
	    command = self.labelDialogCB)
	self.labelEntry = Pmw.EntryField(self.dialog.interior(),
                                         labelpos = 'w',
                                         label_text = 'Label:',
                                         validate = None,
                                         command = self.setLabelTextData)
        self.labelEntry.pack(padx = 8, pady = 8)
	self.dialog.withdraw()

	# Create and pack the MenuBar.
	self.balloon = Pmw.Balloon(parent)
	menuBar = Pmw.MenuBar(parent,
		hull_relief = 'raised',
		hull_borderwidth = 1,
		balloon = self.balloon)
	menuBar.pack(fill = 'x')

	# Add some buttons to the MenuBar.
	menuBar.addmenu('File', 'Load new geom or edge data')
	menuBar.addmenuitem('File', 'command', 'Read a new edge data set',
		command = self.readEDatCB,
		label = 'Read edge data...')
	menuBar.addmenuitem('File', 'separator')
	menuBar.addmenuitem('File', 'command', 'Clear canvas layout',
		command = self.resetLay,
		label = 'Clear Layout')
	menuBar.addmenuitem('File', 'command', 'Save the canvas layout',
		command = self.saveLayAsCB,
		label = 'Save Layout As...')
	menuBar.addmenuitem('File', 'command', 'Read a new canvas layout',
		command = self.readLayCB,
		label = 'Read Layout...')
	menuBar.addmenuitem('File', 'separator')
	menuBar.addmenuitem('File', 'command', 'Export layout to an EPS file',
		command = self.saveEPSCB,
		label = 'Export EPS...')
	menuBar.addmenuitem('File', 'separator')
	menuBar.addmenuitem('File', 'command', 'Quit the application',
		command = parent.destroy,
		label = 'Quit')
	menuBar.addmenu('Object', 'Object transformations')
	menuBar.addmenuitem('Object', 'command', 'Select All',
		command = self.selectAllNoEvent,label = 'Select All')
	menuBar.addmenuitem('Object', 'separator')
	menuBar.addmenuitem('Object', 'command', 'Align grouped nodes vertically',
		command = self.alignInX,label = 'Align In X')
	menuBar.addmenuitem('Object', 'command', 'Align grouped nodes horizontally',
		command = self.alignInY,label = 'Align In Y')
	menuBar.addmenuitem('Object', 'command', 'Distribute grouped nodes horizontally',
		command = self.distribInX,label = 'Distribute in X')
	menuBar.addmenuitem('Object', 'command', 'Distribute grouped nodes vertically',
		command = self.distribInY,label = 'Distribute in Y')
	menuBar.addmenuitem('Object', 'separator')
	menuBar.addmenuitem('Object', 'command', 'Lock grouped nodes',
		command = self.lockNodes,label = 'Lock')
	menuBar.addmenuitem('Object', 'command', 'Unlock grouped nodes',
		command = self.unlockNodes,label = 'Unlock')
	menuBar.addmenu('Labels', 'Add/adjust canvas label')
	menuBar.addmenuitem('Labels', 'command', 'Set alt canvas label',
		command = self.setCanvasLabelCB,
		label = '  Set canvas label...')

        self.sc = Pmw.ScrolledCanvas(parent,
                borderframe = 1,
                labelpos = 'n',
                label_text = 'Layout Canvas',
                usehullsize = 1,
                hull_width = self.canvasSizeX,
                hull_height = self.canvasSizeY,
                vscrollmode = 'dynamic',
                hscrollmode = 'dynamic'
        )
	self.sc.pack(padx=6,pady=6,side='top')
        self.draw = self.sc.interior()
        self.bindMouse()
        self.draw.tk_focusFollowsMouse()
        self.setCanvasLabel(self.canvasLabelText)
        
	self.nodeG = Pmw.Group(parent, tag_text='Node Display')
	self.nodeG.pack(side='left',fill='both', expand = 1, padx = 6, pady = 6)
        AllNodesButton = Tkinter.Button(self.nodeG.interior(), text = 'All',
                                        command = self.allNodes, width=15)
        AllNodesButton.grid(padx=3,pady=3,column=0,row=0,sticky='nsew')
        NoNodesButton = Tkinter.Button(self.nodeG.interior(), text = 'None',
                                       command = self.resetLay, width=15)
        NoNodesButton.grid(padx=3,pady=3,column=0,row=1,sticky='nsew')
        DetachedNodesOffButton = Tkinter.Button(self.nodeG.interior(),
                                            text = 'Remove\nDetached Nodes',
                                            command = self.removeDetachedNodes, width=15)
        DetachedNodesOffButton.grid(padx=3,pady=3,column=0,row=2,sticky='nsew')

	self.edgeG = Pmw.Group(parent, tag_text='Edge Display')
	self.edgeG.pack(side='left',fill = 'both', expand = 1, padx = 6, pady = 6)
        AllEdgesButton = Tkinter.Button(self.edgeG.interior(), text = 'All',
                                        command = self.allEdges,width=15)
        AllEdgesButton.grid(padx=3,pady=3,column=0,row=0,sticky='nsew')
        NoEdgesButton = Tkinter.Button(self.edgeG.interior(), text = 'None',
                                       command = self.noEdges,width=15)
        NoEdgesButton.grid(padx=3,pady=3,column=0,row=1,sticky='nsew')
        self.colorize_menu = Pmw.OptionMenu(self.edgeG.interior(),
                                            labelpos = 'w',
                                            label_text = 'Colorize:',
                                            command = self.colorizeCB,
                                            items = colorizeMap.keys(),
                                            initialitem = 'Monochrome',
                                            menubutton_width = 15
                                            )
	self.colorize_menu.grid(padx=6,pady=3,column=0,row=2)

	self.edgeP = Pmw.Group(parent, tag_text='Edge Parameters')
	self.edgeP.pack(side='right', fill = 'both', expand = 1, padx = 6, pady = 6)
        
        self.slider = Scale(self.edgeP.interior(),orient=HORIZONTAL,length="2i",
                            from_=0,to=100,command=self.sliderCB,resolution=0.1,
                            label='Edge Cutoff (% of strongest)',takefocus=1)
	self.slider.set(self.showEdgeFraction)
        self.slider.grid(padx=6,pady=3,column=1,row=0,sticky='nsew')

        self.oneOrTwo_menu = Pmw.OptionMenu(self.edgeP.interior(),
                                            labelpos = 'w',
                                            label_text = 'Display Mode:',
                                            command = self.oneOrTwoCB,
                                            items = self.coalesceMap.keys(),
                                            initialitem = self.coalesceMap.values()[self.coalesce],
                                            menubutton_width = 20
                                            )
	self.oneOrTwo_menu.grid(padx=6,pady=3,column=1,row=1,sticky='nsew')

        self.normalize_menu = Pmw.OptionMenu(self.edgeP.interior(),
                                             labelpos = 'w',
                                             label_text = 'Edge Thickness:',
                                             command = self.normalizeCB,
                                             items = self.normalizeMap.keys(),
                                             initialitem = self.normalizeMap.values()[self.normalizeEdges],
                                             menubutton_width = 20
                                             )
	self.normalize_menu.grid(padx=6,pady=3,column=1,row=2)

        # More menu stuff
        self.toggleVar = Tkinter.IntVar()
        self.toggleVar.set(1)
        menuBar.addmenuitem('Labels', 'checkbutton', 'Toggle me on/off',
                label = '  Use Dataset Label',
                command = self.toggleLabel,
                variable = self.toggleVar)
        self.toggleLabel()

        self.makeHelp()
        self.makeLicense()
        menuBar.addmenu('Help', 'Show Help window',side='right')
	menuBar.addmenuitem('Help', 'command', 'Show help window',
                            label = 'Show Help window', command = self.showHelp)
	menuBar.addmenuitem('Help', 'command', 'Show license',
                            label = 'Show license agreement', command = self.showLicense)

    def toggleLabel(self):
        if self.toggleVar.get() == 1:
            self.canvasLabelText = self.datasetLabelText
        else:
            self.canvasLabelText = self.mansetLabelText
        self.setCanvasLabel(self.canvasLabelText)
        
    def setLabelTextData(self):
        if self.toggleVar.get() == 1:
            self.toggleVar.set(0)
            self.toggleLabel()
        self.mansetLabelText = self.labelEntry.get()
        self.setCanvasLabel(self.mansetLabelText)

    def labelDialogCB(self, result):
        if result != 'Cancel':
            self.mansetLabelText = self.labelEntry.get()
            self.setCanvasLabel(self.mansetLabelText)
            self.toggleVar.set(0)
            self.toggleLabel()
        if result != 'Apply':
            self.dialog.deactivate(result)

    def setCanvasLabelCB(self):
        self.dialog.activate(globalMode = 1)

    def setCanvasLabel(self,text):
        if self.canvasLabel:
            self.sc.delete(self.canvasLabel)
        self.canvasLabelText = text
        f = Font(family=gd.FONTFAMILY, size=gd.FONTSIZE, weight=gd.FONTWEIGHT)
        self.canvasLabel = self.sc.create_text(0.5*self.canvasSizeX,
                                               0.02*self.canvasSizeY,
                                               text=self.canvasLabelText,font=f)

    def colorizeCB(self,colorize):
        global colorizeEdges, colorizeMap
        colorizeEdges = colorizeMap[colorize]
        global edgeMap
        for key in edgeMap.keys():
            path = edgeMap[key]
            path.erase()
            path.doShow = self.showEdge(path.strength)
            path.show()

    def normalizeCB(self,normalize):
        self.normalizeEdges = self.normalizeMap[normalize]
        global edgeMap
        for key in edgeMap.keys():
            path = edgeMap[key]
            path.erase()
            path.doShow = self.showEdge(path.strength)
            path.show()

    def oneOrTwoCB(self,oneOrTwo):
        self.coalesce = self.coalesceMap[oneOrTwo]
        global edgeMap
        for key in edgeMap.keys():
            path = edgeMap[key]
            path.erase()
            path.coalesce = self.coalesce
            path.doShow = self.showEdge(path.strength)
            path.show()

    def makeHelp(self):
        helpText = 'Bugs/comments to: MSDay@lbl.gov\n\nUsage:  (NOTE: M1=MouseButton 1)\n\nCanvas\nM1\tSelect a node (or node group) to move\n\t\t(If pointer on canvas background, select all nodes in rubber box))\nM2\tRemove a node\nM3\tDisplay window to select edges touching that node\nShift-M1\tAdd/remove node from node group\nCtrl-a\tAdd all nodes to group (same as Object->Select All)\nCtrl-l\tLock selected nodes (same as Object->Lock)\nCtrl-L\tUnlock all locked nodes and select them (same as Object->Unlock)\nCtrl-1\tAlign selected nodes in X (same as Object->Align in X)\nCtrl-2\tAlign selected nodes in Y (same as Object->Align in Y)\nCtrl-3\tDistribute selected nodes in X (same as Object->Distribute in X)\nCtrl-4\tDistribute selected nodes in Y (same as Object->Distribute in Y)\nArrow keys nudge selected nodes\nShift-Arrow nudge \'em faster\n\nNode Display\nAll\tPlaces all nodes on canvas\nNone\tRemoves all nodes from canvas (same as File->Clear Layout)\nRemove Detached Nodes\tRemoves all nodes having no displayed touching edge\n\nEdge Display\nAll\tTurn on all possible edges, subject to Edge Cutoff setting\nNone\tRemove all edges in canvas\n\nEdgeParameters\nEdge Cutoff\tStrength of weakest edge shown\nDisplay Mode\tFor double-valued edges, toggle between displaying the both, or their sum\nEdge Thickness\tToggles between using values as input, or scaling to max. \n   (NB: If Display Mode=Coalesce, then edges scaled to the max of the edge sums)'

        self.help = Pmw.Dialog(self.parent,
                               buttons = ['Cancel'],
                               defaultbutton = 'Cancel',
                               title = 'Help',
                               command = self.killHelp)
        self.helpText = Tkinter.Label(self.help.interior(),justify='left',
                                      text=helpText)
        self.helpText.pack(expand = 1, fill = 'both', padx = 4, pady = 4)
        self.help.withdraw()

    def showHelp(self):
        self.help.activate(globalMode = 'nograb')

    def killHelp(self,result):
        self.help.deactivate(result)

    def makeLicense(self):
        global licenseText
        self.license = Pmw.Dialog(self.parent,
                               buttons = ['OK'],
                               defaultbutton = 'OK',
                               title = 'License Agreement',
                               command = self.killLicense)
        self.licenseST = Pmw.ScrolledText(self.license.interior(),
                                          borderframe = 1,
                                          text_padx = 10,
                                          text_pady = 10,
                                          text_wrap = 'word')
        self.licenseST.pack(padx = 5, pady = 5, fill = 'both', expand = 1)
        self.licenseST.insert('end',licenseText)
        self.license.withdraw()

    def showLicense(self):
        self.license.activate(globalMode = 'nograb')

    def killLicense(self,result):
        self.license.deactivate(result)

    def setMultMinMax(self):
        if (len(self.multObjs)>0):
            self.multMinX = self.multObjs[0].x
            self.multMaxX = self.multObjs[0].x2
            self.multMinY = self.multObjs[0].y
            self.multMaxY = self.multObjs[0].y2
            for node in self.multObjs:
                self.multMinX = min(node.x,self.multMinX)
                self.multMaxX = max(node.x2,self.multMaxX)
                self.multMinY = min(node.y,self.multMinY)
                self.multMaxY = max(node.y2,self.multMaxY)

    def nudgeXp(self,event):
        if len(self.multObjs)>0:
            incx = min(1,max(0,self.canvasSizeX-self.multMaxX-2*self.multObjs[0].width))
            if not incx == 0:
                for obj in self.multObjs:
                    obj.move(incx,0)
                self.multMinX = self.multMinX + incx
                self.multMaxX = self.multMaxX + incx

    def nudgeXm(self,event):
        if len(self.multObjs)>0:
            incx = -min(1,max(0,self.multMinX))
            if not incx == 0:
                for obj in self.multObjs:
                    obj.move(incx,0)
                self.multMinX = self.multMinX + incx
                self.multMaxX = self.multMaxX + incx

    def nudgeYp(self,event):
        if len(self.multObjs)>0:
            incy = min(1,max(0,self.canvasSizeY-self.multMaxY-self.multObjs[0].radius))
            if not incy == 0:
                for obj in self.multObjs:
                    obj.move(0,incy)
                self.multMinY = self.multMinY + incy
                self.multMaxY = self.multMaxY + incy

    def nudgeYm(self,event):
        if len(self.multObjs)>0:
            incy = -min(1,max(0,self.multMinY))
            obj = self.multObjs[0]
            if not incy == 0:
                for obj in self.multObjs:
                    obj.move(0,incy)
                self.multMinY = self.multMinY + incy
                self.multMaxY = self.multMaxY + incy

    def nudgeXP(self,event):
        if len(self.multObjs)>0:
            incx = min(10,max(0,self.canvasSizeX-self.multMaxX-2*self.multObjs[0].width))
            if not incx == 0:
                for obj in self.multObjs:
                    obj.move(incx,0)
                self.multMinX = self.multMinX + incx
                self.multMaxX = self.multMaxX + incx

    def nudgeXM(self,event):
        if len(self.multObjs)>0:
            incx = -min(10,max(0,self.multMinX))
            if not incx == 0:
                for obj in self.multObjs:
                    obj.move(incx,0)
                self.multMinX = self.multMinX + incx
                self.multMaxX = self.multMaxX + incx

    def nudgeYP(self,event):
        if len(self.multObjs)>0:
            incy = min(10,max(0,self.canvasSizeY-self.multMaxY-self.multObjs[0].radius))
            if not incy == 0:
                for obj in self.multObjs:
                    obj.move(0,incy)
                self.multMinY = self.multMinY + incy
                self.multMaxY = self.multMaxY + incy

    def nudgeYM(self,event):
        if len(self.multObjs)>0:
            incy = -min(10,max(0,self.multMinY))
            obj = self.multObjs[0]
            if not incy == 0:
                for obj in self.multObjs:
                    obj.move(0,incy)
                self.multMinY = self.multMinY + incy
                self.multMaxY = self.multMaxY + incy

    def alignInX(self,event=None):
        Nmult = len(self.multObjs)
        if Nmult > 1:
            x = self.multObjs[0].xc
            for i in range(1,Nmult):
                obj = self.multObjs[i]
                obj.move(x-obj.xc,0)
                
    def alignInY(self,event=None):
        Nmult = len(self.multObjs)
        if Nmult > 1:
            y = self.multObjs[0].yc
            for i in range(1,Nmult):
                obj = self.multObjs[i]
                obj.move(0,y-obj.yc)

    def cmpx(self,a,b):
        if a.xc < b.xc: return -1
        if a.xc > b.xc: return +1
        return 0

    def cmpy(self,a,b):
        if a.yc < b.yc: return -1
        if a.yc > b.yc: return +1
        return 0

    def distribInY(self,event=None):
        if len(self.multObjs) > 1:
            self.multObjs.sort(self.cmpy)
            y2 = self.multObjs[-1].yc
            y1 = self.multObjs[0].yc
            dy = y2 - y1
            if abs(dy) > 1.e-6:
               dy = dy / (len(self.multObjs) - 1)
               for i in range(1,len(self.multObjs)-1):
                   newY = y1 + i*dy
                   node = self.multObjs[i]
                   node.move(0,newY - node.yc)
               self.setMultMinMax()

    def distribInX(self,event=None):
        if len(self.multObjs) > 1:
            self.multObjs.sort(self.cmpx)
            x2 = self.multObjs[-1].xc
            x1 = self.multObjs[0].xc
            dx = x2 - x1
            if abs(dx) > 1.e-6:
               dx = dx / (len(self.multObjs) - 1)
               for i in range(1,len(self.multObjs)-1):
                   newX = x1 + i*dx
                   node = self.multObjs[i]
                   node.move(newX - node.xc,0)
               self.setMultMinMax()

    def sliderCB(self,val):
        self.showEdgeFraction = float(val)
        global edgeMap
        for key in edgeMap.keys():
            path = edgeMap[key]
            path.erase()
            path.doShow = self.showEdge(path.strength)
            path.show()

    def showEdge(self,strength):
        if self.coalesce == self.coalesceMap['Coalesce Fwd/Rev']:
            showEdge = 1
            sum = 0.0
            for val in strength:
                sum = sum + val
            if abs(sum*100/self.getNormEdgeVal()) < self.showEdgeFraction:
                showEdge = 0
        else:
            showEdge = 0
            for val in strength:
                if abs(val*100/self.getNormEdgeVal()) >= self.showEdgeFraction:
                    showEdge = 1
        return showEdge

    def removeDetachedNodes(self):
        for (name,node) in nodeMap.items():
            edgeTags = self.findUsedEdgesTouching(name)
            shutoff = 1
            for tag in edgeTags:
                edge = edgeMap[tag]
                if self.showEdge(edge.strength):
                    shutoff = 0
                    continue
            if shutoff:
                self.toggleNode(name,0)

    def resetLay(self):
        self.clearCanvas()

    def clearCanvas(self):
        self.newNodeCntr = 0
        global nodeMap
        for tag in nodeMap.keys():
            nodeMap[tag].erase()
            rps = nodeMap[tag].adjacentPaths()
            state = 0
            for path in rps:
                self.toggleEdge(str(path.tag), state)
            nodeMap[tag].destroy()
    
    def unlockNodes(self,event=None):
        for node in self.lockedNodes:
            self.selectNode(node)
        self.lockedNodes = []

    def lockNodes(self,event=None):
        while len(self.multObjs) > 0:
            self.lockedNodes.append(self.multObjs[0])
            self.deselectNode(self.multObjs[0])

    def findObj(self,event):
        dx = gd.NODERADIUS * 0.01
        closestObjs = self.draw.find_overlapping(self.startx-dx,self.starty-dx,self.startx+dx,self.starty+dx)

        global nodeMap
        objSet = []
        for objID in closestObjs:
            cx = self.draw.canvasx(event.x)
            cy = self.draw.canvasy(event.y)
            for spec in nodeMap.keys():
                node = nodeMap[spec]
                if node not in self.lockedNodes:
                    if node.contains(objID):
                        if r2dist(node.xc,node.yc,cx,cy) < node.radius:
                            return node
        return None
        
    def mouse1Down(self, event):
        self.lastx = self.startx = self.draw.canvasx(event.x)
        self.lasty = self.starty = self.draw.canvasy(event.y)
        self.selObj = self.findObj(event)
        if ( (not self.selObj) | (self.selObj not in self.multObjs)):
            for node in self.multObjs:
                node.erase()
                node.width=gd.NODEWIDTH
                node.show()
            self.multObjs = []

    def mouse1Move(self, event):
        if self.selObj:
            obj = self.selObj
            if obj in self.multObjs:
                self.multiMove(event)
            else:
                rad = obj.radius
                xptr = max(rad,min(self.canvasSizeX-rad,self.draw.canvasx(event.x)))
                yptr = max(rad,min(self.canvasSizeY-rad,self.draw.canvasy(event.y)))
                self.selObj.move(xptr-self.lastx,yptr-self.lasty)
                self.lastx = xptr
                self.lasty = yptr
        else:
            self.lastx = self.draw.canvasx(event.x)
            self.lasty = self.draw.canvasy(event.y)
            
            if (self.startx != event.x)  and (self.starty != event.y) : 
                self.draw.delete(self.rubberbandBox)
                self.rubberbandBox = self.draw.create_rectangle(
                    self.startx, self.starty, self.lastx, self.lasty)

    def mouse1Up(self, event):
        if self.rubberbandBox != None:
            self.draw.delete(self.rubberbandBox)
            self.rubberbandBox = None
            self.findEnclObj(self.startx,self.starty,self.lastx,self.lasty)
	
    def findEnclObj(self,x0,y0,x1,y1):
        enclObjs = self.draw.find_enclosed(x0,y0,x1,y1)
        global nodeMap
        objSet = []
        for objID in enclObjs:
            for spec in nodeMap.keys():
                node = nodeMap[spec]
                if node not in self.lockedNodes:
                    if node.contains(objID):
                        self.selectNode(node)
        
    def mouse2Down(self, event):
        self.lastx = self.startx = self.draw.canvasx(event.x)
        self.lasty = self.starty = self.draw.canvasy(event.y)
        obj = self.findObj(event)
        if obj:
            self.toggleNode(obj.name,0)
            self.selObj = None

    def mouse3Down(self, event):
        self.lastx = self.startx = self.draw.canvasx(event.x)
        self.lasty = self.starty = self.draw.canvasy(event.y)
        self.selObj = self.findObj(event)
        if self.selObj:
            self.unbindMouse()

            self.edgeSpecies = self.selObj.name
            choices = self.findUnusedEdgesTouching(self.edgeSpecies)
            self.t1 = Toplevel(self.parent)

            label = self.edgeSpecies+' Edges'
            self.choose = MyRadioSelect(self.t1,
                                        labelpos = 'n',
                                        command = self.chooseSpecEdge,
                                        label_text = label,
                                        frame_borderwidth = 2,
                                        frame_relief = 'flat',
                                        selectmode = 'multiple',
                                        orient = 'vertical',
                                        maxcr = 1
                                    )
            self.choose.pack()
            for choice in choices:
                self.choose.add(choice)

            chosen = self.findUsedEdgesTouching(self.edgeSpecies)
            for choice in chosen:
                self.choose.add(choice,init='selected')

            self.choose.add('All')
            self.choose.add('None')
            exitButton = Tkinter.Button(self.t1,text = 'Done',
                                        command=self.killChoose)
            exitButton.pack(padx=3,pady=5)

    def selectAllNoEvent(self):
        self.selectAll(None)
        
    def selectAll(self,event):
        global nodeMap
        for node in nodeMap.values():
            if node not in self.multObjs:
                if node not in self.lockedNodes:
                    self.selectNode(node)

    def selectNode(self,node):
        self.multObjs.append(node)
        node.erase()
        node.width = gd.NODEWIDTH+2
        node.show()
        self.setMultMinMax()
        
    def deselectNode(self,node):
        self.multObjs.remove(node)
        node.erase()
        node.width = gd.NODEWIDTH
        node.show()
        self.setMultMinMax()

    def multiSelect(self,event):
        self.lastx = self.startx = self.draw.canvasx(event.x)
        self.lasty = self.starty = self.draw.canvasy(event.y)
        obj = self.findObj(event)
        global nodeMap
        if obj:
            if obj not in self.multObjs:
                self.selectNode(obj)
            else:
                self.deselectNode(obj)

    def multiMove(self, event):
        if len(self.multObjs) > 0:
            rad = self.multObjs[0].radius
            cx = min(self.canvasSizeX-rad,max(rad,self.draw.canvasx(event.x)))
            cy = min(self.canvasSizeY-rad,max(rad,self.draw.canvasy(event.y)))
            incx = cx - self.lastx
            incy = cy - self.lasty
            for obj in self.multObjs:
                obj.move(incx,incy)
            self.lastx = cx
            self.lasty = cy
            self.multMinX = self.multMinX + incx
            self.multMaxX = self.multMaxX + incx
            self.multMinY = self.multMinY + incy
            self.multMaxY = self.multMaxY + incy


    def findUnusedEdgesTouching(self,name):
        tags = []
        global edgeMap, nodeMap
        for (s1,s2) in self.allAvailEdges:
            if ( ((s1==name) & (nodeMap.has_key(s2))) |
                 ((s2==name) & (nodeMap.has_key(s1))) ):
                tag = str(PairTag(s1,s2))
                if (edgeMap.has_key(tag)==0):
                    tags.append(tag)
        return tags

    def findUsedEdgesTouching(self,name):
        tags = []
        global edgeMap, nodeMap
        for tag in edgeMap.keys():
            (s1,s2) = self.tagToPair[tag]
            if ((s1==name) | (s2==name)):
                tags.append(tag)
        return tags

    def chooseSpecEdge(self, tag, state):
        if ((tag=='All') | (tag=='None')):
            if (state):
                self.choose.invoke(tag)
            else:
                if (tag=='All'):
                    for taga in self.findUnusedEdgesTouching(self.edgeSpecies):
                        self.choose.invoke(taga)
                else:
                    for tagn in self.findUsedEdgesTouching(self.edgeSpecies):
                        self.choose.invoke(tagn)
        else:
            self.toggleEdge(tag, state)                

    def killChoose(self):
        self.t1.destroy()
        del self.t1
        self.bindMouse()

    def editEdgesKill(self,result):
        self.t1.deactivate(result)

    def allEdges(self):
        for name in nodeMap.keys():
            tags = self.findUnusedEdgesTouching(name)
            state = 1
            for tag in tags:
                self.toggleEdge(tag,state)

    def initNodeDist(self,cnt):
        f = 2*gd.NODERADIUS + 2*gd.NODEWIDTH
        nx = int(self.canvasSizeX/f)
        row = cnt/(2*nx-1)
        colM = cnt - row*(2*nx-1)
        (rowm,colm) = divmod(colM,nx)
        x = (0.5+colm+0.5*rowm)*f
        sqrt3 = math.sqrt(3.0)
        y = self.canvasSizeY - (1.0+sqrt3*row + 0.5*sqrt3*rowm)*f
        return (x,y)

    def allNodes(self):
        global nodeMap
        for node in self.allAvailNodes:
            if not node in nodeMap.keys():
                self.toggleNode(node,1)
                obj = nodeMap[node]
                rad = obj.radius
                (xloc,yloc) = self.initNodeDist(self.newNodeCntr)
                obj.move(xloc-obj.xc,yloc-obj.yc)
                self.newNodeCntr = self.newNodeCntr + 1

    def noEdges(self):
        for name in nodeMap.keys():
            tags = self.findUsedEdgesTouching(name)
            state = 0
            for tag in tags:
                self.toggleEdge(tag,state)

    def makeNewGraphNode(self,id):
        GraphNode(self.draw,0,0,colorMap(0),colorMap(0),id)

    def getNormEdgeVal(self):
        if self.normalizeEdges:
            if self.coalesce == self.coalesceMap['Coalesce Fwd/Rev']:
                return self.maxEdgeSum
            else:
                return self.maxEdgeVal
        else:
            return 1.0
        
    def makeNewGraphEdge(self,id):
        (sp1,sp2) = self.tagToPair[id]
        strength = self.allAvailEdgeWeights[(sp1,sp2)]
        doShow = self.showEdge(strength)
        GraphEdge(self,sp1,sp2,strength,doShow,self.coalesce,self.getNormEdgeVal())

    def toggleNode(self, tag, state):
        global nodeMap
        if state:
            if tag not in nodeMap.keys():
                self.makeNewGraphNode(tag)
        else:
            if nodeMap[tag] in self.lockedNodes:
                pass
            else:
                nodeMap[tag].erase()
                rps = nodeMap[tag].adjacentPaths()
                for path in rps:
                    self.toggleEdge(str(path.tag),0)
                nodeMap[tag].destroy()

    def toggleEdge(self, tag, state):
        global nodeMap, edgeMap
        (sp1,sp2) = self.tagToPair[tag]
        if state:
            if ( (edgeMap.has_key(tag) == 0) &
                 nodeMap.has_key(sp1) & nodeMap.has_key(sp2)):
                self.makeNewGraphEdge(tag)
                path = edgeMap[tag]
                path.erase()
                path.doShow = self.showEdge(path.strength)
                path.show()
            else:
                self.toggleEdge(tag,not state)
        else:
            if (edgeMap.has_key(str(tag))):
                edgeMap[str(tag)].erase()
                edgeMap[str(tag)].destroy()
                
    def saveEPSCB(self):
        self.saveEPS()

    def saveEPS(self):
        ofile = asksaveasfilename(filetypes=[("Encapsulated PostScript", "*.eps"),
                                             ("All Files", "*")])
        if ofile:
            self.epsFile = ofile
            self.doSaveEPS()

    def doSaveEPS(self):
        self.draw.postscript(file=self.epsFile,
                             pageheight=8.0*72,pagewidth=8.0*72)

    def saveLayAsCB(self):
        self.saveLayAs()

    def saveLayAs(self):
        ofile = asksaveasfilename(filetypes=[("ChemPathTool Layout File", "*.clf"),
                                             ("All Files", "*")])
        if ofile:
            self.layFile = ofile
            self.doSaveLay()

    def doSaveLay(self):
        f = open(self.layFile,'w')
        p = cPickle.Pickler(f)
        self.setObj = None
        p.dump(self.allAvailNodes)
        p.dump(self.allAvailEdges)
        pSBM = []
        global nodeMap, edgeMap
        for sp in nodeMap.keys():
            pSBM.append(ProxyGraphNode(nodeMap[sp]))
        p.dump(pSBM)
        pRPM = []
        for tag in edgeMap.keys():
            pRPM.append(ProxyGraphEdge(edgeMap[tag]))
        p.dump(pRPM)
        p.dump(self.showEdgeFraction)
        f.close()

    def readLayCB(self):
        self.readLay()

    def readLay(self):
        ifile = askopenfilename(filetypes=[("ChemPathTool Layout File", "*.clf"),
                                             ("All Files", "*")])
        if ifile:
            self.doReadLay(ifile)

    def doReadLay(self,ifile):
        self.layFile = ifile
        f = open(self.layFile,'r')
        u = cPickle.Unpickler(f)
        self.selObj = None

        # the next two lines are useless, but appear for backward compatibility
        layoutNodes = u.load()
        layoutEdges = u.load()
        pGNM = u.load()
        self.resetLay()
        
        global nodeMap, edgeMap
        for pGN in pGNM:
            name = pGN.name
            if name in self.allAvailNodes:
                self.toggleNode(name,1)
                gn = nodeMap[name]
                gn.erase()
                nodeMap[name] = pGN.initGraphNode(gn)
                gn.show()
        pGEM = u.load()
        state = 1
        for pge in pGEM:
            if (pge.node0,pge.node1) in self.allAvailEdges:
                self.toggleEdge(str(pge.tag), state)
        sliderVal = u.load()
       	self.slider.set(sliderVal)
        f.close()

    def readEDatCB(self):
        self.readEDat()

    def readEDat(self):
        ifile = askopenfilename(filetypes=[("ChemPathTool Edge Data", "*.ced"),
                                             ("All Files", "*")])
        if ifile:
            self.doReadEDat(ifile)

    def doReadEDat(self,ifile):
        self.edatFile = ifile
        f = open(self.edatFile,'r')
        l = f.readlines()
        l[0] = replace(l[0],'\n','')
        self.datasetLabelText = l[0]
        l[1] = replace(l[1],'\n','')
        nodes = split(l[1],' ')
        edgeVals = []
        for ln in range(2,len(l)):
            line = l[ln]
            p = split(line,' ')
            while '' in p:
                p.remove('')

            if p[0] not in nodes:
                print 'Bad input line',ln+1,':',p[0],'not in node list...continuing'
            elif p[1] not in nodes:
                print 'Bad input line',ln+1,':',p[1],'not in node list...continuing'
            else:
                vals = []
                vals.append(p[0])
                vals.append(p[1])
                for i in range(2,len(p)):
                    vals.append(float(p[i]))
                edgeVals.append(vals)

        self.initialize(nodes,edgeVals)
        self.toggleVar.set(1)
        self.toggleLabel()

######################################################################
 
# Create demo in root window for testing.

if __name__ == '__main__': 

    title = 'Path Diagram Tool'
    root = Tkinter.Tk()
    Pmw.initialise(root, fontScheme = 'pmw3')
    root.title(title)

    edgeVals = []
    nodes = []
    
    if len(sys.argv) == 1:
        # Make some test data. Use this as a model for something real
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

            label = ''

    else:
        
        infile = sys.argv[1]
        f = open(infile,'r')
        lines = f.readlines()
        label = lines[0].strip()
        nodes = lines[1].strip().split()
        for line in lines[2:]:
            vals = line.strip().split()
            if (len(vals) == 4):
                if ( (float(vals[2]) != 0) | (float(vals[3]) != 0) ):
                    edgeVals.append((vals[0],vals[1],float(vals[2]),float(vals[3])))
            elif (len(vals) == 3):
                if (float(vals[2]) != 0):
                    edgeVals.append((vals[0],vals[1],float(vals[2]),0.0))
            else:
                print 'bad input line - expecting 2 strings, and either one or two floats.'
                print 'Found: ',line
        f.close()

    widget = ChemPathTool (root, nodes, edgeVals, label)

    root.mainloop()

