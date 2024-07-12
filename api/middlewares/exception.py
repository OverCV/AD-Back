from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi import HTTPException

import traceback
import logging
import sys


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except HTTPException as http_err:
            return JSONResponse(
                status_code=http_err.status_code,
                content={'detail': http_err.detail},
            )
        except Exception as ex:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = exc_tb.tb_frame.f_code.co_filename
            line_no = exc_tb.tb_lineno
            trace = traceback.format_exc()
            logging.warning(trace)
            # printnl(trace.split('File')[-5:])
            last_trace = trace.split('File')[-1].strip()
            detail_error = {
                'type': str(exc_type.__name__),
                'message': str(ex),
                'file': fname,
                'line': line_no,
                'traceback': last_trace,
            }
            return JSONResponse(
                status_code=500,
                content={'detail': detail_error},
            )


# class ExceptionMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request: Request, call_next):
#         try:
#             response = await call_next(request)
#             return response
#         except HTTPException as http_err:
#             return JSONResponse(
#                 status_code=http_err.status_code,
#                 content={'detail': http_err.detail}
#             )
#         except Exception as ex:
#             if not isinstance(ex, HTTPException):
#                 # Si la excepción no es una HTTPException, mostrar el objeto de error original
#                 status_error = 500
#                 detail_error = f'Internal Server Error {ex}'
#             else:
#                 # Si la excepción es una HTTPException, usar los detalles proporcionados
#                 status_error = ex.status_code
#                 detail_error = ex.detail

#             return JSONResponse(
#                 status_code=status_error,
#                 content={'detail': detail_error}
#             )
