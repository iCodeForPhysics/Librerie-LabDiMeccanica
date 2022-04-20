


######################################################################
# File con riunite tutte le librerie del professore F. Santanastasio #
#           ---La maggior parte non sono state testate---            #
######################################################################



import matplotlib.pyplot as plt
# per manipolare arrays e fare di conto
import numpy as np
from math import log10, floor, sqrt
# per fare cose piu' sofisticate come per esempio generare 
#numeri pseudo random
import scipy as sp
from scipy import stats

#########################################################################
# funzione per arrotondare con un certo numero di cifre significative
#########################################################################
def round_sig(x, sig=2):
        return round(x, sig-int(floor(log10(abs(x))))-1)

def PrintResult(name,mean,sigma,digits,unit):
    mean = round(mean,digits)
    sigma = round(sigma,digits)
    nu = sigma / mean
    result = (name+" = ({0} +/- {1} ) ".format(mean,sigma)+unit+" [{0:.2f}%]".format(nu*100))
    print (result)
    #return ""

#########################################################################
# funzione per fare un istogramma con una gaussiana sovrapposta
#########################################################################
#
def gaussHistogram(d, xl='x', yl='y', titolo='titolo', bin_scale=0.5, label='', color='b'):
    mean = d.mean()
    std = d.std()

# scelta del binning
    binsize = std*bin_scale # metà della standard deviation di default
    interval = d.max() - d.min()
    nbins = int(interval / binsize)
    
# 1) Crea un numpy array con 100 valori equamente separati nell'intervallo voluto dell'asse x
    lnspc = np.linspace(d.min()-std, d.max()+std, 100) 

# in questo modo posso raccogliere in vettori le informazioni sull'istogramma
    counts , bins , patches = plt.hist(d, bins=nbins,
                                       color=color, alpha=0.75, label=label)
    
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(label=titolo)
# ==> Disegna una distribuzione normale

# 2) Normalizza la funzione f(x) in modo che l'integrale da -inf a +inf sia il numero totale di misure
    norm_factor = d.size * binsize

# 3) Crea un numpy array con i valori f(x), uno per ciascun punto
# NOTA: Ho usato la distribuzione normale presa da "scipy" 
#      (vedi all'inizio del programma "from scipy import stats")
    f_gaus = norm_factor*stats.norm.pdf(lnspc, mean, std) 
# draw the function
    plt.plot(lnspc, f_gaus, linewidth=1, color='r',linestyle='--')
    print('counts      = ', len(d))
    print('mean        = ', round_sig(mean, 2))
    print('sigma       = ', round_sig(std, 2))
    print('sigma_mean  = ', round_sig(std/sqrt(len(d)), 2))

###########################################################################
#  funzioni per sistemare le cifre significative di misura ed incertezza
###########################################################################
#
def decimal_places(x):
    return int(str(x)[::-1].find('.'))

def present_result(measure, uncertainty, sig=2):
    uncertainty_rounded = round_sig(uncertainty, sig)
    measure_rounded = round(measure, decimal_places(uncertainty_rounded))
    if(uncertainty_rounded>1):
        measure_rounded = int(round(measure_rounded, 
                                    sig-int(np.floor(np.log10(abs(uncertainty))))-1))
    return (measure_rounded, uncertainty_rounded)

#########################################################################
# funzioni per fare il fit lineare
#########################################################################
#
def my_mean(x, w):
    return np.sum( x*w ) / np.sum( w )

def my_cov(x, y, w):
    return my_mean(x*y, w) - my_mean(x, w)*my_mean(y, w)

def my_var(x, w):
    return my_cov(x, x, w)

def my_line(x, m=1, c=0):
    return m*x + c

def y_estrapolato(x, m, c, sigma_m, sigma_c, cov_mc):
    y = m*x + c
    uy = np.sqrt(np.power(x, 2)*np.power(sigma_m, 2) +
                   np.power(sigma_c, 2) + 2*x*cov_mc ) 
    return y, uy

def lin_fit(x, y, sd_y, xlabel="x [ux]", ylabel="y [uy]", xm=0., xM=1., ym=0., yM=1., 
            verbose=True, plot=False, setrange=False):

    #pesi
    w_y = np.power(sd_y.astype(float), -2) 
    
    #m
    m = my_cov(x, y, w_y) / my_var(x, w_y)
    var_m = 1 / ( my_var(x, w_y) * np.sum(w_y) )
    
    #c
    c = my_mean(y, w_y) - my_mean(x, w_y) * m
    var_c = my_mean(x*x, w_y)  / ( my_var(x, w_y) * np.sum(w_y) )
    
    #cov
    cov_mc = - my_mean(x, w_y) / ( my_var(x, w_y) * np.sum(w_y) ) 
   
    #rho
    rho_mc = cov_mc / ( sqrt(var_m) * sqrt(var_c) )

    if (verbose):
        
        print ('m         = ', m.round(4))
        print ('sigma(m)  = ', np.sqrt(var_m).round(4))
        print ('c         = ', c.round(4))
        print ('sigma(c)  = ', np.sqrt(var_c).round(4))
        print ('cov(m, c) = ', cov_mc.round(4))
        print ('rho(m, c) = ', rho_mc.round(4))
        
    if (plot):
        
        # rappresento i dati
        plt.errorbar(x, y, yerr=sd_y, xerr=0, ls='', marker='.', 
                     color="black",label='dati')

        # costruisco dei punti x su cui valutare la retta del fit              
        xmin = float(np.min(x)) 
        xmax = float(np.max(x))
        xmin_plot = xmin-.2*(xmax-xmin)
        xmax_plot = xmax+.2*(xmax-xmin)
        if (setrange):
            xmin_plot = xm
            xmax_plot = xM  
        x1 = np.linspace(xmin_plot, xmax_plot, 100)
        y1 = my_line(x1, m, c)
        
        # rappresento la retta del fit
        plt.plot(x1, y1, linestyle='-.', color="green", label='fit')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title('Fit lineare')
        plt.xlim(xmin_plot,xmax_plot)
        if (setrange):
            plt.ylim(ym,yM)
        
        # rappresento le incertezze sulla retta 
        y1_plus_1sigma = y1+y_estrapolato(x1, m, c, np.sqrt(var_m), np.sqrt(var_c), cov_mc)[1]
        y1_minus_1sigma = y1-y_estrapolato(x1, m, c, np.sqrt(var_m), np.sqrt(var_c), cov_mc)[1]         
        plt.plot(x1,y1_plus_1sigma, linestyle='-', color="orange", label=r'fit $\pm 1\sigma$')
        plt.plot(x1,y1_minus_1sigma, linestyle='-', color="orange")
        
        plt.grid()
        
        plt.legend()
        
    return m, np.sqrt(var_m), c, np.sqrt(var_c), cov_mc, rho_mc

###########################################################################
# estraploazione lineare con incertezza
###########################################################################
#
# y
#
def y_estrapolato(xl, m, c, sigma_m, sigma_c, cov_mc):
    y = m*xl + c
    y_inc = np.sqrt(np.power(xl, 2)*np.power(sigma_m, 2) +
                   np.power(sigma_c, 2) + 2*xl*cov_mc ) 
    return y, y_inc
#
# x
#
def x_estrapolato(yl, m, c, sigma_m, sigma_c, cov_mc):
    if (m != 0): 
        x = yl / m - c
        x_inc = np.sqrt(np.power(yl/m, 2)*np.power(sigma_m, 2) +
                   np.power(sigma_c, 2) + 2*(-1)*(1/m)*cov_mc ) 
    else :
        x = -c   
        x_inc = sigma_c
    return x, x_inc
