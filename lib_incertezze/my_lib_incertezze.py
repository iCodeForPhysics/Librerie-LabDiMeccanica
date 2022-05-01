


########################################################################################################### 
#  /$$    /$$                              /$$                                      /$$$$$$      /$$$$$$  #
# | $$   | $$                             |__/                                     /$$$_  $$    /$$__  $$ #
# | $$   | $$ /$$$$$$   /$$$$$$   /$$$$$$$ /$$  /$$$$$$  /$$$$$$$   /$$$$$$       | $$$$\ $$   |__/  \ $$ #
# |  $$ / $$//$$__  $$ /$$__  $$ /$$_____/| $$ /$$__  $$| $$__  $$ /$$__  $$      | $$ $$ $$      /$$$$$/ #
#  \  $$ $$/| $$$$$$$$| $$  \__/|  $$$$$$ | $$| $$  \ $$| $$  \ $$| $$$$$$$$      | $$\ $$$$     |___  $$ #
#   \  $$$/ | $$_____/| $$       \____  $$| $$| $$  | $$| $$  | $$| $$_____/      | $$ \ $$$    /$$  \ $$ #
#    \  $/  |  $$$$$$$| $$       /$$$$$$$/| $$|  $$$$$$/| $$  | $$|  $$$$$$$      |  $$$$$$//$$|  $$$$$$/ #
#     \_/    \_______/|__/      |_______/ |__/ \______/ |__/  |__/ \_______/       \______/|__/ \______/  #
########################################################################################################### 



from sympy import symbols, diff, sqrt

def incRipetute(sd, n, ris, sb):
    """
    Permette di calcolare l'errore per misure ripetute

        Parametri: 
            sd (float): Deviazione standard
            n (int): Numero di misure
            ris (float): Risoluzione dello strumento
            sb (float): Incertezza di tipo B
        Ritorna:
            sigma (float): Incertezza per misure ripetute
    """
    sigma=sqrt((sd/sqrt(n))**2 +(ris/sqrt(12))**2 + (sb)**2)
    return sigma

def incSingole(sd, ris, sb):
    """
    Permette di calcolare l'errore per misure singole

        Parametri: 
            sd (float): Deviazione standard
            ris (float): Risoluzione dello strumento
            sb (float): Incertezza di tipo B
        Ritorna:
            sigma (float): Incertezza per misure singole
    """
    sigma=sqrt((sd)**2 + (ris/sqrt(12))**2 + (sb)**2)
    return sigma

def incPropagate(f, x, y, z, xv=.0, yv=.0, zv=.0, s_x=.0, s_y=.0, s_z=.0): # Propagazione delle incertezze
    """
    Permette di calcolare la propagazione delle incertezze

        Parametri: 
            f (sympy equation): Formula su cui propagare le incertezze
            x, y, z (sympy symbols): Incognite presenti nella formula
            xv, yv, zv (float): Valori veri delle incognite
            s_x, s_y, s_z (float): Errori delle incognite
        Ritorna:
            inc (float): Incertezza propagata
        Esempio:
            f = 3x+y
            incPropagate(f, x, y, z, 1.0, 2.0, 0, 0.5, 0.5, 0.0)) -> 1.5811
    """
    inc = sqrt((f.diff(x).subs({x:xv, y:yv, z:zv})**2) * (s_x**2) + (f.diff(y).subs({x:xv, y:yv, z:zv})**2) * (s_y**2) + (f.diff(z).subs({x:xv, y:yv, z:zv})**2) * (s_z**2))
    return inc
