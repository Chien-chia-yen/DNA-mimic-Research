#
# -- basicCodeBlock.py
#
from __future__ import print_function
from pymol import cmd
from pymol import stored
from chempy import cpv
import numpy as np
#from mpl_toolkits import mplot3d
#import matplotlib.pyplot as plt

def centroid(selection='all', center=0, quiet=1):
    
    model = cmd.get_model(selection)
    nAtom = len(model.atom)

    centroid = cpv.get_null()

    for a in model.atom:
        centroid = cpv.add(centroid, a.coord)
    centroid = cpv.scale(centroid, 1. / nAtom)

    if not int(quiet):
        print(' centroid: [%8.3f,%8.3f,%8.3f]' % tuple(centroid))

    if int(center):
        cmd.alter_state(1, selection, "(x,y,z)=sub((x,y,z), centroid)",
                        space={'centroid': centroid, 'sub': cpv.sub})

    return centroid
    

def myFunction():#每轉幾度記錄一次
    
    dirPath=r"./test/"
    path='./test/' 
    data=[f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath,f))]
    for j in range(len(data)):
        data[j]=data[j][:-4]
        print(data[j])
    for i in range(len(data)):
        cmd.deselect()
        cmd.load(path+data[i]+'.pdb' )
        centroid('all',1)
        print('centroid ',data[i],' complete')
        cmd.save('./output/'+data[i]+'.pdb')
        cmd.delete (data[i] )
        
                             


cmd.extend( "myFunction", myFunction );
cmd.extend("centroid", centroid)
