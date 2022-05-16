


########################################################################################################
#  /$$    /$$                              /$$                                      /$$$$$$  /$$   /$$ #
# | $$   | $$                             |__/                                     /$$$_  $$| $$  | $$ #
# | $$   | $$ /$$$$$$   /$$$$$$   /$$$$$$$ /$$  /$$$$$$  /$$$$$$$   /$$$$$$       | $$$$\ $$| $$  | $$ #
# |  $$ / $$//$$__  $$ /$$__  $$ /$$_____/| $$ /$$__  $$| $$__  $$ /$$__  $$      | $$ $$ $$| $$$$$$$$ #
#  \  $$ $$/| $$$$$$$$| $$  \__/|  $$$$$$ | $$| $$  \ $$| $$  \ $$| $$$$$$$$      | $$\ $$$$|_____  $$ #
#   \  $$$/ | $$_____/| $$       \____  $$| $$| $$  | $$| $$  | $$| $$_____/      | $$ \ $$$      | $$ #
#    \  $/  |  $$$$$$$| $$       /$$$$$$$/| $$|  $$$$$$/| $$  | $$|  $$$$$$$      |  $$$$$$//$$   | $$ #
#     \_/    \_______/|__/      |_______/ |__/ \______/ |__/  |__/ \_______/       \______/|__/   |__/ #
########################################################################################################




from sympy import symbols, diff, sqrt

def incRipetute(sd: float, n: int, ris: float, sb: float) -> float:
    """
    Permette di calcolare l'errore per misure ripetute

        Parametri: 
            sd: Deviazione standard
            n: Numero di misure
            ris: Risoluzione dello strumento
            sb: Incertezza di tipo B
        Ritorna:
            sigma: Incertezza per misure ripetute
    """
    sigma=sqrt((sd/sqrt(n))**2 +(ris/sqrt(12))**2 + (sb)**2)
    return sigma

def incSingole(sd: float, ris: float, sb: float) -> float:
    """
    Permette di calcolare l'errore per misure singole

        Parametri: 
            sd: Deviazione standard
            ris: Risoluzione dello strumento
            sb: Incertezza di tipo B
        Ritorna:
            sigma: Incertezza per misure singole
    """
    sigma=sqrt((sd)**2 + (ris/sqrt(12))**2 + (sb)**2)
    return sigma

def incPropagate(f: symbols, x: symbols, y: symbols, z: symbols, xv: float=.0, yv: float=.0, zv: float=.0, s_x: float=.0, s_y: float=.0, s_z: float=.0) -> float:
    """
    Permette di calcolare la propagazione delle incertezze

        Parametri: 
            f (sympy equation): Formula su cui propagare le incertezze
            x, y, z: Incognite presenti nella formula
            xv, yv, zv: Valori veri delle incognite
            s_x, s_y, s_z: Errori delle incognite
        Ritorna:
            inc: Incertezza propagata
        Esempio:
            f = 3x+y
            incPropagate(f, x, y, z, 1.0, 2.0, 0, 0.5, 0.5, 0.0)) -> 1.5811
    """
    inc = sqrt((f.diff(x).subs({x:xv, y:yv, z:zv})**2) * (s_x**2) + (f.diff(y).subs({x:xv, y:yv, z:zv})**2) * (s_y**2) + (f.diff(z).subs({x:xv, y:yv, z:zv})**2) * (s_z**2))
    return inc
