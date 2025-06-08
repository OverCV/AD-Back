from fastapi.testclient import TestClient
from dotenv import load_dotenv
from api.models.enums.backend import ExecConfig
from main import app


"""
NEXT_LCL_URL = "http://localhost:3000"

REMOTE_MONGO_URI = "mongodb+srv://localhost:mongo-uri"
LOCAL_MONGO_URI = "mongodb://localhost:27017"

MONGO_CLIENT = "ada"
MONGO_COLLECTION = "networks"

SQLITE_URL = "sqlite:///data/base/.sqlite"
"""
load_dotenv(dotenv_path=ExecConfig.DOTENV_PATH.value)

# os.environ['NEXT_LCL_URL'] = 'http://localhost:3000'

# os.environ['REMOTE_MONGO_URI'] = (
#     'mongodb+srv://ada-user:ada-pass@cluster0.6gpnf7u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
# )
# os.environ['LOCAL_MONGO_URI'] = 'mongodb://localhost:27017'

# os.environ['MONGO_CLIENT'] = 'ada'
# os.environ['MONGO_COLLECTION'] = 'networks'

# os.environ['SQLITE_URL'] = 'sqlite:///data/base/.sqlite'


# Crear el cliente de pruebas
client = TestClient(app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello algorithms!'}


def setup():
    client.get('/analyze/sia-pyphi/')


# def test_pyphi_strategy():
#     # Define los parámetros de la solicitud
#     params = {
#         'title': 'R5A',
#         'istate': '10000',
#         'subsys': '11100',
#         'effect': '11111',
#         'actual': '11111',
#         'dual': False,
#     }

#     # Realiza la solicitud GET al endpoint
#     response = client.get('/analyze/sia-pyphi/', params=params)

#     # Verifica el código de estado de la respuesta
#     assert response.status_code == 200

#     # Verifica el contenido de la respuesta
#     data = response.json()
#     assert 'data' in data  # Ajusta según la estructura esperada de la respuesta
#     # Puedes agregar más aserciones para verificar el contenido específico de la respuesta
