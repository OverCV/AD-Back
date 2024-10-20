import logging
import uvicorn
from dotenv import load_dotenv
from api.models.enums.backend import ExecConfig

load_dotenv(dotenv_path=ExecConfig.DOTENV_PATH.value)


logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=ExecConfig.LOGGER_DIR.value,
    encoding=ExecConfig.LOGGER_ENCODING.value,
    level=logging.INFO,
)

if __name__ == ExecConfig.__MAIN__:
    uvicorn.run(
        app=ExecConfig.MAIN_APP_FILE.value,
        host=ExecConfig.LOCALHOST.value,
        port=ExecConfig.APP_PORT.value,
        reload=ExecConfig.YES.value,
    )
