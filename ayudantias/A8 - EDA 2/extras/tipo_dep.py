import pandas as pd
import numpy as np


def remplazar_cod_depe(x):
    if x == 1 or x == 2 or x == 6:
        return 'GRATUITO'
    elif x == 3:
        return 'PARTICULAR SUBVENCIONADO'
    elif x == 4:
        return 'PARTICULAR'
    elif x == 5:
        return 'CORPORACION'
    elif x == 0:
        return 'NO INFO'