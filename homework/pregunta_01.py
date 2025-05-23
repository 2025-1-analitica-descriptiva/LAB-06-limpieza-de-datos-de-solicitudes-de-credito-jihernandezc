"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    input_file = "files/input/solicitudes_de_credito.csv"
    output_file = "files/output/solicitudes_de_credito.csv"

    df = pd.read_csv(input_file, sep=";").dropna()

    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()

    df["idea_negocio"] = (
        df["idea_negocio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
        .str.strip()
    )

    df["barrio"] = (
        df["barrio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    def normalize_date(date):
        parts = date.split("/")
        if len(parts[0]) == 4:
            return f"{parts[2]}/{parts[1]}/{parts[0]}"
        return date

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(normalize_date)

    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.replace(" ", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    df["línea_credito"] = (
        df["línea_credito"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    # Eliminar duplicados con base en columnas clave
    df = df.drop_duplicates(subset=[
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "estrato",
        "comuna_ciudadano",
        "fecha_de_beneficio",
        "monto_del_credito",
        "línea_credito",
    ])

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, sep=";", index=False)

pregunta_01()