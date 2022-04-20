

############################################################
# Come usare la funzione incPropragate                     #
############################################################


import my_lib_incertezze as inc
from sympy import symbols

##################
# Valori         #
##################
xm, ym, zm = .0, .0, .0 # Valori medi
s_xm, s_ym, s_zm = .0, .0, .0 # Errori dei valori medi
xs, ys, zs = symbols('x y z') # # #  Non cambiare le cose dentro symbols() # # # <----> ##### Esempio ##### -> ##### T_quad, L, m = symbols('x y z') #####
f = 0.0 # Formula con xs, ys, zs ##### Esempio ##### -> ##### 4*xs**2 + 6*ys**2 #####  

##################
# Stampa         #
##################
print("Incertezza propragata: ", inc.incPropagate(f, xs, ys, zs, xm, ym, zm, s_xm, s_ym, s_zm))
