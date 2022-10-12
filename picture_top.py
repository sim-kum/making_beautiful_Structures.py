#!/usr/bin/env python
from ase.io import *
from ase import Atoms , Atom
from ase_povray import povray_parameter
import numpy as np

image_list = ['14']

for l in image_list:
        B=read('CONTCAR_'+l)
        A=B.repeat((3,3,1))

        #A_trans = [atom.index for atom in A if atom.position[2] < 32]
        del A[[atom.index for atom in A if atom.position[2] < 32]]
        PovRay=povray_parameter(A,atoms_radii={'In':1.2,'O':0.74,'H':0.4,'Sn':1.2, 'Pt':1.5})

        PovRay.set_colors({'In':(0.7765,0.7765,0.8745),
                               'O':(0.8275,0.1725,0.1216),
                               'H':(0.9216,0.9176,0.9176),
                               'Sn':(0.4353,0.5255,0.8549),
                               'Pt':(0.4510,0.4510,0.4549)})
        PovRay.set_textures({'In':'jmol' ,
                               'O':'jmol',
                               'H':'jmol',
                               'Pt':'jmol',
                               'Sn':'jmol'})


#Set bounding box and resolution
        PovRay.kwargs['bbox']=(15, 14, 29, 27) #this id defines as X1,Y1, X2, Y2 on the diagonal
        PovRay.kwargs['canvas_width']=200
#PovRay.kwargs['bondatoms']=[['In','O'],['Sn','O'],['O','H'],['Pt','Pt'],['Pt','Sn'],['Pt','In'],['Pt','H']]


#Set different colors for specific atoms different colors
#at.append(568)
#at.append(569)
#at_color.append((1.0,0.5,0.0))
#at_color.append((0.5,0.2,0.05))
#PovRay.set_specific_colors(at,at_color)
#PovRay.set_specific_textures(at,at_text)

        renderer = write(l+'.pov',A,**PovRay.kwargs)
