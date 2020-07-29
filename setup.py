#!/usr/bin/env python

from distutils.core import setup

setup(name="ChemPathTool",
      version="1.0",
      description="Chemical Path Diagram Drawing Tool",
      author="Marc Day and Joe Grcar",
      author_email="MSDay@lbl.gov",
      url="http://seesar.lbl.gov/CCSE",
      py_modules=['chemPathTool','MyPmwRadioSelect','mechinfo','genPathEdgeData',
                  'CanteraChemEdgeAnalysis','ChemEdge','ChemEdgeAnalysis',
                  'chemPathToolScr'],
      data_files=[('Lib\site-packages',['README.chemPathTool']),
                  ('Lib\site-packages\ChemPathToolData',['ChemPathToolData/leanVFI.ced',
                                                  'ChemPathToolData/leanVFI.clf',
                                                  'ChemPathToolData/pyCanteraEX.ced',
                                                  'ChemPathToolData/pyCanteraEX.clf'])]
     )

