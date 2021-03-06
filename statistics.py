from math import sqrt

def wilson_score(pos, n):
    """ 
    ta funkcja jest wykorzystywana do policzenia "sprawiedliwego score'u
    dla pytan i odpowiedzi
    z = 1.969964 dla p = 0.05
    """
    if n == 0:
        return 0
    # confidence level 0.05
    z = 1.959964
    phat = 1.0*pos/n
    return (phat + z*z/(2.0*n) - z * sqrt((phat*(1.0-phat)+z*z/(4.0*n))/n))/(1.0+z*z/n)
    

