import logging
import uvicorn
from dotenv import load_dotenv

from api.models.enums.backend import ExecConfig
load_dotenv(dotenv_path='.venv\\.dev.env')


logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='app.log',
    encoding='utf-8', level=logging.WARNING
)

if __name__ == '__main__':
    uvicorn.run(
        app=ExecConfig.MAIN_APP_FILE.value,
        host=ExecConfig.LOCALHOST.value,
        port=ExecConfig.APP_PORT.value,
        reload=True
    )
