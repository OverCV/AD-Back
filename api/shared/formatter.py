import base64
import io
import re
from typing import Callable
from numpy.typing import NDArray
import numpy as np
from fastapi import HTTPException, UploadFile, status
import openpyxl as op
import pandas as pd

from api.models.enums.extensions import FileExt
from api.models.props.structure import StructProps
from constants.format import S2C, S2P, S2S
from utils.consts import COLS_IDX

from icecream import ic


class Format:
    """Class Formatter is used to format the XSLX file from the user input."""

    def __init__(self, bytes: UploadFile = None, sheet: str = None, format: str = None) -> None:
        self.__array_file: UploadFile = bytes
        self.__sheet: str = sheet
        self.__format: str = format
        self.__array: NDArray[np.float64] | None = None
        self.__matrices: list[NDArray[np.float64]] = []

    def get_matrices(self) -> list[NDArray[np.float64]]:
        return self.__matrices

    async def set_array(self) -> None:
        if self.__array_file is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail='No file was provided.'
            )
        bytes_chunk = await self.__array_file.read()
        arr: NDArray[np.float64] = None
        if self.__array_file.filename.endswith(FileExt.EXCEL.value):
            xlsx = io.BytesIO(bytes_chunk)
            wb = op.load_workbook(xlsx)
            ws = wb[self.__sheet]
            # ws = wb.active
            lst = []
            for cells in ws.iter_rows():
                vector = [cell.value for cell in cells if cell.value is not None]
                lst.append(vector) if vector else None
            ic(lst)
            arr = np.array(lst, dtype=np.float64)
        elif self.__array_file.filename.endswith(FileExt.CSV.value):
            csv = io.BytesIO(bytes_chunk)
            df = pd.read_csv(csv, header=None)

            # Procesar cada fila para convertir las cadenas en listas de flotantes
            processed_list = []
            for row in df[0]:
                float_strings = re.findall(r'[-+]?\d*\.\d+|\d+', row)
                float_values = list(map(float, float_strings))
                processed_list.append(float_values)

            # Lista procesada en un array de NumPy
            arr = np.array(processed_list, dtype=np.float64)
        elif any(
            self.__array_file.filename.endswith(FileExt.TXT.value),
            self.__array_file.filename.endswith(FileExt.JSON.value),
        ):
            raise HTTPException(
                detail='Unavailable for JSON or TXT files.',
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            )
        else:
            raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
        # mat = np.delete(mat, np.where(mat.sum(axis=1) == 0), axis=0)
        self.__array = arr

    def set_matrices(self) -> None:
        if self.__format is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail='No format was provided.'
            )
        format_input: dict[str, Callable] = {
            S2S: lambda: print(f'Format {S2S} not implemented yet.'),
            S2C: self.__sc2sp,
            S2P: lambda: print(f'Format {S2P} not implemented yet.'),
        }
        format_input[self.__format]()

    def __sc2sp(self) -> None:
        # [s..s, c] -> [s..s, (1-c, c)] #
        arr = self.__array
        for col in range(arr.shape[COLS_IDX]):
            # Seleccionamos la columna
            column = arr[:, col]
            # Creamos una matriz con la misma cantidad de filas que la columnas y dos columnas.
            new_mat = np.zeros((arr.shape[0], 2))
            # Llenamos la primera columna con el complemento de la columna original
            new_mat[:, 0] = 1 - column
            # Llenamos la segunda columna con la columna original
            new_mat[:, 1] = column
            # Agregamos la nueva matriz a la lista de tensores
            self.__matrices.append(new_mat)

    def __ss2sp(self) -> None:
        # [s..s, s..s] -> [s..s, (1-c, c)] #
        # ! Here we need to marginalize ! #
        mat = self.__array
        for col in range(mat.shape[COLS_IDX]):
            # Seleccionamos la columna
            column = mat[:, col]
            # Creamos una matriz con la misma cantidad de filas que la columnas y dos columnas.
            new_mat = np.zeros((mat.shape[0], 2))
            # Llenamos la primera columna con el complemento de la columna original
            new_mat[:, 0] = 1 - column
            # Llenamos la segunda columna con la columna original
            new_mat[:, 1] = column
            # Agregamos la nueva matriz a la lista de tensores
            self.__matrices.append(new_mat)

    def serialize_tensor(self, tensor: NDArray[np.float64]) -> str:
        """Serializa y codifica en base64 un tensor NumPy."""
        buffer = io.BytesIO()
        np.savez_compressed(buffer, tensor=tensor)
        buffer.seek(0)
        encoded = base64.b64encode(buffer.read()).decode('utf-8')
        return encoded

    def deserialize_tensor(self, encoded_tensor: str) -> NDArray[np.float64]:
        """Deserializa un tensor codificado en base64 a un arreglo NumPy."""
        decoded = base64.b64decode(encoded_tensor)
        buffer = io.BytesIO(decoded)
        with np.load(buffer) as data:
            tensor = data[StructProps.TENSOR]
        return tensor
