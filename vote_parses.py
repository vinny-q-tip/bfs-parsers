import numpy as np
import pandas as pd

from utils import pd_convert_to_int


def parse_eidgenoessische_volksabstimmungen(path: str):
    """
    Table: Eidgenössische Volksabstimmungen: detaillierte Ergebnisse
    BFS number: je-d 17.03.01.02
    Last update: 09.02.2020
    """
    sheet_names = ['2020', '2010-2019', '2000-2009', '1990-1999',
                   '1980-1989', '1970-1979', '1950-1969', '1900-1949', '1848-1899']
    header_skip_rows = [2, 2, 6, 6, 6, 6, 6, 6, 6]
    footer_skip_rows = [16, 24, 15, 14, 14, 14, 14, 14, 15]
    column_names = ['Nr. der Vorlage', 'Datum', 'Gegenstand', 'Art', 'Stimmberechtigte',
                    'Abgegebene Stimmen', 'Stimmbeteiligung in %', 'Leer', 'Ungültig',
                    'Gültige Stimmen', 'JA-Stimmen', 'NEIN-Stimmen', 'JA in %',
                    'Angenommen (A) Verworfen (V)', 'Annehmende Stände', 'Ablehnende Stände']
    column_dtypes = {
        column_names[0]: object,
        column_names[2]: object,
        column_names[3]: object,
        column_names[6]: np.float64,
        column_names[9]: np.int32,
        column_names[10]: np.int32,
        column_names[11]: np.int32,
        column_names[12]: np.float64,
        column_names[13]: object,
        column_names[14]: object,
        column_names[15]: object
    }
    converters = {
        column_names[4]: pd_convert_to_int,
        column_names[5]: pd_convert_to_int,
        column_names[7]: pd_convert_to_int,
        column_names[8]: pd_convert_to_int}

    df = None
    for sheet_nr in reversed(range(len(sheet_names))):
        df_part = pd.read_excel(path,
                                sheet_name=sheet_names[sheet_nr],
                                skiprows=list(
                                    range(header_skip_rows[sheet_nr])),
                                skipfooter=footer_skip_rows[sheet_nr],
                                names=column_names,
                                dtype=column_dtypes,
                                converters=converters,
                                parse_dates=[column_names[1]])
        if sheet_nr < len(sheet_names) - 1:
            df = df.append(df_part, ignore_index=True)
        else:
            df = df_part
