import pandas as pd 
import numpy as np

def remplazar_ponderado(df, df_ponderados):
    df["PTJE_PONDERADO"] = df.apply(lambda x: buscar_ponderado(x.MRUN, x.CODIGO_CARRERA, x.VIA_ADMISION, df_ponderados), axis=1)
    df.PTJE_PONDERADO = df.PTJE_PONDERADO.str.replace(",", ".")
    df.PTJE_PONDERADO = df.PTJE_PONDERADO.astype(float)
    return df

def buscar_ponderado(MRUN, COD_CARRERA, VIA_ADMISION, df_ponderados):
    if VIA_ADMISION == 1:
        df_filtrado = df_ponderados[df_ponderados.MRUN == MRUN]
        if COD_CARRERA in df_filtrado.values:
            column_index = np.where(df_filtrado.values == COD_CARRERA)[1][0] + 2
            return df_filtrado.iloc[:, column_index].values[0]
    else:
        return 0

