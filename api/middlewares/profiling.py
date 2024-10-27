from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from pyinstrument import Profiler
from pyinstrument.renderers.html import HTMLRenderer
from pyinstrument.renderers.speedscope import SpeedscopeRenderer
from typing import Callable
from pathlib import Path
import os


class ProfilingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app) -> None:
        super().__init__(app)
        # Crear directorio profiles si no existe
        self.output_dir = Path('data/profiles')
        if not self.output_dir.exists():
            os.makedirs(self.output_dir)

    async def dispatch(self, request: Request, call_next: Callable):
        """Profile the current request if profile=true is in query params"""

        if not request.query_params.get('profile', False):
            return await call_next(request)

        profile_type_to_ext = {'html': 'html', 'speedscope': 'speedscope.json'}
        profile_type_to_renderer = {
            'html': HTMLRenderer,
            'speedscope': SpeedscopeRenderer,
        }

        # Default to speedscope format
        profile_type = request.query_params.get('profile_format', 'speedscope')

        with Profiler(interval=0.001, async_mode='enabled') as profiler:
            response = await call_next(request)

        # Generate unique filename based on endpoint
        endpoint = request.url.path.replace('/', '_').strip('_')
        extension = profile_type_to_ext[profile_type]
        renderer = profile_type_to_renderer[profile_type]()

        output_path = self.output_dir / f'profile_{endpoint}.{extension}'
        with open(output_path, 'w') as out:
            out.write(profiler.output(renderer=renderer))

        return response


""""""
# from fastapi import Request
# from starlette.middleware.base import BaseHTTPMiddleware
# from fastapi.responses import Response
# from pyinstrument import Profiler
# from pyinstrument.renderers.html import HTMLRenderer
# from pyinstrument.renderers.speedscope import SpeedscopeRenderer
# from typing import Callable
# import os
# from datetime import datetime


# class ProfilingMiddleware(BaseHTTPMiddleware):
#     def __init__(
#         self,
#         app,
#         output_dir: str = 'data/profiles',
#     ):
#         super().__init__(app)
#         self.output_dir = output_dir

#         # Crear el directorio de salida si no existe
#         if not os.path.exists(output_dir):
#             os.makedirs(output_dir)

#     async def dispatch(self, request: Request, call_next: Callable) -> Response:
#         # Solo perfilar si se solicita mediante query param
#         if not request.query_params.get('profile', False):
#             return await call_next(request)

#         # Configurar el formato de salida (html o speedscope)
#         profile_format = request.query_params.get('profile_format', 'speedscope')

#         # Iniciar el profiler
#         profiler = Profiler(interval=0.001, async_mode='enabled')
#         profiler.start()

#         # Ejecutar la request
#         response = await call_next(request)

#         # Detener el profiler
#         profiler.stop()

#         # Generar nombre de archivo único
#         timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
#         endpoint = request.url.path.strip('/').replace('/', '_')
#         filename = f'{endpoint}_{timestamp}'

#         # Configurar el renderer según el formato
#         if profile_format == 'html':
#             renderer = HTMLRenderer()
#             ext = 'html'
#         else:  # speedscope
#             renderer = SpeedscopeRenderer()
#             ext = 'speedscope.json'

#         # Guardar el resultado
#         output_path = os.path.join(self.output_dir, f'{filename}.{ext}')
#         with open(output_path, 'w') as f:
#             f.write(profiler.output(renderer=renderer))

#         return response

""""""

# from fastapi import Request
# from fastapi.responses import Response
# from pyinstrument import Profiler
# from pyinstrument.renderers.html import HTMLRenderer
# from pyinstrument.renderers.speedscope import SpeedscopeRenderer
# from typing import Callable
# import os
# from datetime import datetime


# class ProfilingMiddleware:
#     def __init__(
#         self,
#         output_dir: str = 'profiles',
#         enabled: bool = True,
#         interval: float = 0.001,
#     ):
#         self.output_dir = output_dir
#         self.enabled = enabled
#         self.interval = interval

#         # Crear el directorio de salida si no existe
#         if not os.path.exists(output_dir):
#             os.makedirs(output_dir)

#     async def __call__(self, request: Request, call_next: Callable) -> Response:
#         # Solo perfilar si está habilitado y se solicita mediante query param
#         if not self.enabled or not request.query_params.get('profile', False):
#             return await call_next(request)

#         # Configurar el formato de salida (html o speedscope)
#         profile_format = request.query_params.get('profile_format', 'speedscope')

#         # Iniciar el profiler
#         profiler = Profiler(interval=self.interval, async_mode='enabled')
#         profiler.start()

#         # Ejecutar la request
#         response = await call_next(request)

#         # Detener el profiler
#         profiler.stop()

#         # Generar nombre de archivo único
#         timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
#         endpoint = request.url.path.strip('/').replace('/', '_')
#         filename = f'{endpoint}_{timestamp}'

#         # Configurar el renderer según el formato
#         if profile_format == 'html':
#             renderer = HTMLRenderer()
#             ext = 'html'
#         else:  # speedscope
#             renderer = SpeedscopeRenderer()
#             ext = 'speedscope.json'

#         # Guardar el resultado
#         output_path = os.path.join(self.output_dir, f'{filename}.{ext}')
#         with open(output_path, 'w') as f:
#             f.write(profiler.output(renderer=renderer))

#         return response


""""""

# from typing import Callable

# from uuid import uuid4

# from fastapi import FastAPI

# from api.shared.profiling.execution import profiler
# from exec import logger


# class ProfilingMiddleware:
#     def __init__(self, app: FastAPI):
#         self.app = app

#     async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
#         if scope['type'] != 'http':
#             await self.app(scope, receive, send)
#             return

#         request_id = str(uuid4())
#         path = scope.get('path', 'unknown')

#         profiler.push_context(request_id, f'request:{path}')
#         try:
#             await self.app(scope, receive, send)
#         finally:
#             func_name, execution_time = profiler.pop_context(request_id)
#             profiler.add_execution(func_name, execution_time)
#             profiler.clear_request_context(request_id)
#             logger.info(f'Request: {path} - Total Time: {execution_time:.4f}s')
