# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:25:11 2020

@author: Martin
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
bg_color = 'black'
fg_color = 'white'
plt.rcParams['axes.titlesize'] = 30
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['font.size'] = 25
plt.rcParams['xtick.labelsize']=20
plt.rcParams['ytick.labelsize']=20
import seaborn as sns

# Fijo un punto y una normal

point  = np.array([1, 2, 3])
normal = np.array([1, 1, 2])

# el plano es a*x+b*y+c*z-d=0
# [a,b,c] es normal. Por lo tanto tenemos que calcular d
# como? con el producto interno del punto elegido
d = point.dot(normal)

# creo una malla de puntos x,y
xx, yy = np.meshgrid(range(10), range(10))

# calculo el z
z = (-normal[0] * xx - normal[1] * yy + d) * 1. /normal[2]

# setup plot
plt3d = plt.figure(figsize=(10,10)).gca(projection='3d');
plt3d.set_xlabel('x');
plt3d.set_ylabel('y');
plt3d.set_zlabel('z');

# plot the surface
plt3d.plot_surface(xx, yy, z, alpha=0.7);

# plot the point
plt3d.plot([point[0]], [point[1]], [point[2]], color='red', marker='o', markersize=20, alpha=0.8);

# Dejo el vector normal en el centro del plano
startX = np.mean(plt3d.get_xlim())
startY = np.mean(plt3d.get_ylim())
startZ = (-normal[0] * startX - normal[1] * startY +d) * 1 /normal[2]

# Dibujo la normal al plano
plt3d.quiver([startX], [startY], [startZ], [normal[0]], [normal[1]], [normal[2]], linewidths = (5,), edgecolor="red");
# Dibujo un vector en el plano desde el origen
plt3d.quiver([0], [0], [0], [startX], [startY], [startZ], linewidths = (5,),arrow_length_ratio=0.1, edgecolor="red");

# simulo 6 vectores en el plano
startX=plt3d.get_xlim()[0]+(plt3d.get_xlim()[1]-plt3d.get_xlim()[0])*np.random.rand(6,1)
startY=plt3d.get_ylim()[0]+(plt3d.get_ylim()[1]-plt3d.get_ylim()[0])*np.random.rand(6,1)
startZ = (-normal[0] * startX - normal[1] * startY + d) * 1 /normal[2]

# es normal al vector diferencia
#v1 y v2 apoyan en el plano. sus extremos descansan en el plano
v1=startX[0][0],startY[0][0],startZ[0][0]
v1=list(v1)
v2=startX[1][0],startY[1][0],startZ[1][0]
v2=list(v2)
# el vector dif habita en el plano dif por ser la diferencia de dos vectores del plano
dif=np.array(v1) -np.array(v2)
# simplemente lo multiplico por la normal 
# ecuacion del plano (X0-X)*Normal=0 → X0*N + (-X*Normal)=0 → X0*Normal+Sesgo=0
dif.dot(normal)
# grafica 6 normales y 6 vectores en el plano
plt3d.quiver([startX], [startY], [startZ], [normal[0]], [normal[1]], [normal[2]], linewidths = (1,), edgecolor="red");
plt3d.quiver([0], [0], [0], [startX], [startY], [startZ], linewidths = (3,), arrow_length_ratio=0.01,edgecolor="blue");

#grafica un vector que vive "sobre" el plano

plt3d.quiver([v2[0]], [v2[1]], [v2[2]], [dif[0]], [dif[1]], [dif[2]], linewidths = (3,), arrow_length_ratio=0.01,edgecolor="magenta");


# un punto sobre el planto da -9
-normal.dot(point)

-normal.dot(point+[1,2,3])

arriba=point+[1,2,3]
startX_, startY_, startZ_=arriba
plt3d.plot([arriba[0]], [arriba[1]], [arriba[2]], color='red', marker='*', markersize=20, alpha=0.8);

abajo=point-[0.5,0.7,1.3]
startX_, startY_, startZ_=abajo
plt3d.quiver([0], [0], [0], [startX_], [startY_], [startZ_], linewidths = (5,), arrow_length_ratio=0.01,edgecolor="yellow");
plt3d.plot([abajo[0]], [abajo[1]], [abajo[2]], color='magenta', marker='s', markersize=20, alpha=0.8);



# producto vectoriañ o cruz de 2 vectores
a=[1,2,3]
b=[3,-1,5]

normal_=np.cross(a,b)
print(normal_.dot(a))



# creo una malla de puntos x,y
xx_, yy_ = np.meshgrid(range(-5,10), range(-5,10))

# calculo el z
z_ = (-normal_[0] * xx_ - normal_[1] * yy_ + 0) * 1. /normal_[2]

# setup plot
plt3d = plt.figure(figsize=(10,10)).gca(projection='3d');
plt3d.set_xlabel('x');
plt3d.set_ylabel('y');
plt3d.set_zlabel('z');

# plot the surface
plt3d.plot_surface(xx_, yy_, z_, alpha=0.7);
plt3d.plot([0], [0], [0], color='magenta', marker='s', markersize=20, alpha=0.8);
