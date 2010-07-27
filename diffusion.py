#!/opt/local/bin/python

# --------------------------------------------
# diffusion.py - Resolution du probleme de diffusion
# dans une barre de longueur L
# --------------------------------------------
# Author: Taurus Olson
#
# Copyright (C) 2009, Taurus Olson
#

from numpy import zeros,linspace
import numpy as np
#import matplotlib #.pyplot as plt

#def box_dimension(ini,fin,N):
    #f=[]
    #multi = [i for i in range(0,N)]

    #f=multi[:]*((fin-ini)/float((N+1)))
    #print f
    
# Constantes
A=127E-7
T0 = 293

t0 = 0
tf = 120000
Nt = 10000;             # Nb de points dans le temps
t  = linspace(t0,tf,Nt) # Duree de la simpulation

x0 = 0
xf = 2
Nx = 20;                # Nb de points dans l'espace
x  = linspace(x0,xf,Nx)

dx, dt = 0, 0
dx = x[1]-x[0]
dt = t[1]-t[0]
s = A*dt/((dx)**2) 
##----------------------

T = zeros((Nx,Nt))
T[0][:] = 500
T[Nx-1][:] = 350
T[:][0] = T0
T[:][1] = T0
#% j  = > x
#% n  = > t

for n in range(1,len(t)-1):
    for j in range(1,len(x)-1):
        T[j][n+1] = s * T[j-1][n] + np.dot([1-2*s],T[j][n]) + s*T[j+1][n]

#Stockage de la matrice T pour tous les n*h (n un entier) dans le fichier eqdiff.dat 
#fid=fopen('eqdiff.dat','w');
#h=250;
#for i=1:Nx
    #for j=1:250:Nt
        #fprintf(fid,'%e %e %e\n',T(i,j));
    #end
#fprintf(fid,' %e\n',x(i));
#end
#fclose(fid);

#fid2=fopen('diffusion_posit.dat','w');
        #fprintf(fid,'%e \n',x);
#fclose(fid2);

#Affichage de la courbe T(x) pour differents pas de temps (ici h)
#for k in range(0,Nt):
#k =linspace(0,Nt,40)
#for i in k:
    #plt.plot(x,T[:,i])


