import base64
import io
from typing import Callable
import numpy as np
from fastapi import HTTPException, UploadFile, status
import openpyxl as op
import pandas as pd

from api.models.enums.extensions import FileExt
from api.models.matrix import Matrix
from constants.format import S2C, S2P, S2S
from utils.consts import COLS_IDX
from utils.funcs import cout


class Format:
    ''' Class Formatter is used to format the XSLX file from the user input. '''

    def __init__(self, bytes: UploadFile = None, format: str = None) -> None:
        self.__array_file: UploadFile = bytes
        self.__format: str = format
        self.__array: np.ndarray | None = None
        self.__matrices: list[np.ndarray] = list()

    def get_matrices(self) -> list[np.ndarray]:
        return self.__matrices

    async def set_array(self) -> None:
        if self.__array_file is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='No file was provided.'
            )
        bytes_chunk = await self.__array_file.read()
        arr: np.ndarray = None
        if self.__array_file.filename.endswith(FileExt.EXCEL.value):
            xlsx = io.BytesIO(bytes_chunk)
            wb = op.load_workbook(xlsx)
            ws = wb.active

            lst = list()
            for cells in ws.iter_rows():
                vector = [cell.value for cell in cells if cell.value is not None]
                lst.append(vector)
            arr = np.array(lst, dtype=float)
        elif self.__array_file.filename.endswith(FileExt.CSV.value):
            csv = io.BytesIO(bytes_chunk)
            df = pd.read_csv(csv)
            arr = df.to_numpy(dtype=float)
        elif any(
            self.__array_file.filename.endswith(FileExt.TXT.value),
            self.__array_file.filename.endswith(FileExt.JSON.value)
        ):
            raise HTTPException(
                detail='Unavailable for JSON or TXT files.',
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_501_NOT_IMPLEMENTED
            )
        # mat = np.delete(mat, np.where(mat.sum(axis=1) == 0), axis=0)
        self.__array = arr

    def set_matrices(self) -> None:
        if self.__format is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='No format was provided.'
            )
        format_options: dict[str, Callable] = {
            S2S: lambda: print(f'Format {S2S} not implemented yet.'),
            S2C: self.__sc2sp,
            S2P: lambda: print(f'Format {S2P} not implemented yet.'),
        }
        format_options[self.__format]()

    def __sc2sp(self) -> None:
        # [s..s, c] -> [s..s, (1-c, c)] #
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

    def serialize_tensor(self, tensor: np.ndarray) -> str:
        """Serializa y codifica en base64 un tensor NumPy."""
        buffer = io.BytesIO()
        np.savez_compressed(buffer, tensor=tensor)
        buffer.seek(0)
        encoded = base64.b64encode(buffer.read()).decode('utf-8')
        return encoded

    def deserialize_tensor(self, encoded_tensor: str) -> np.ndarray:
        """Deserializa un tensor codificado en base64 a un arreglo NumPy."""
        decoded = base64.b64decode(encoded_tensor)
        buffer = io.BytesIO(decoded)
        with np.load(buffer) as data:
            tensor = data['tensor']
        return tensor

    # def serialize_tensor(self):
    #     """ Serializa y codifica en base64 un tensor NumPy. """
    #     subtensor = np.array(self.__matrices)
    #     if not isinstance(subtensor, np.ndarray):
    #         raise HTTPException(
    #             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #             detail='Tensor is not defined.'
    #         )
    #     serialized = np.savez_compressed(
    #         base64.b64encode(subtensor)
    #     )
        # return base64.b64encode(serialized)

    # def deserialize_tensor(self, encoded_tensor):
    #     """ Deserializa un tensor codificado en base64 a un arreglo NumPy. """
    #     decoded = base64.b64decode(encoded_tensor)
    #     buffer = io.BytesIO(decoded)
    #     tensor = np.load(buffer, allow_pickle=True)
    #     return tensor
