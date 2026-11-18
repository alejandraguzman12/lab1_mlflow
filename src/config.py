"""Nombres del experimento y del modelo, y semilla.

`src/` lee estos valores desde aquí. Salen de `.env`; si falta el
archivo, se usan los de `.env.example`.

El objetivo, la partición y la métrica salen del prototipo de
`notebooks/01_exploracion.ipynb`: predecir `Sale Price` y elegir
el run con mayor R2.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parents[1]
load_dotenv(RAIZ / ".env")

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "sqlite:///mlflow.db")
MLFLOW_EXPERIMENT_NAME = os.getenv("MLFLOW_EXPERIMENT_NAME", "adidas-nike-price")
MLFLOW_MODEL_NAME = os.getenv("MLFLOW_MODEL_NAME", "adidas-nike-model")
MLFLOW_MODEL_ALIAS = os.getenv("MLFLOW_MODEL_ALIAS", "challenger")
RANDOM_SEED = int(os.getenv("RANDOM_SEED", "42"))

_ruta_datos = os.getenv("DATA_PATH", "data/adidas_nike.csv")
DATA_PATH = (
    Path(_ruta_datos)
    if Path(_ruta_datos).is_absolute()
    else RAIZ / _ruta_datos
)

# Decisiones cerradas en el notebook. No se repiten en el resto de src/.
TARGET = "Sale Price"
TEST_SIZE = 0.3
METRIC = "r2"
ID_COLUMN = "Product ID"
PRECIO_LISTA_MIN = 0
CATEGORICAS = ("Brand",)

COLUMNS_TO_DROP = (
    "Product Name",
    "Product ID",
    "Description",
    "Last Visited",
    "Discount",
)


def activar_seguimiento():
    """Apunta MLflow al almacén y al experimento de este proyecto."""
    import mlflow

    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)