
from fit_expnorm import fit_one as fit_one_expnorm
from fit_expsmooth import fit_one as fit_one_expsmooth

if __name__=='__main__':
    fit_one_expsmooth()
    for _ in range(5):
        fit_one_expnorm()

