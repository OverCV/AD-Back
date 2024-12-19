from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request
from pyinstrument import Profiler
from pyinstrument.renderers.html import HTMLRenderer
from pyinstrument.renderers.speedscope import SpeedscopeRenderer
from typing import Callable
from pathlib import Path
import os


class ProfilingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
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

        output_path = self.output_dir / f'{endpoint}.{extension}'
        with open(output_path, 'w') as out:
            out.write(profiler.output(renderer=renderer))

        return response
