# from numpy import 
# from numpy.typing import NDArray
from fastapi import Body, HTTPException, Query, Response, status, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pymongo.errors import ServerSelectionTimeoutError

from bson import ObjectId

from api.schemas.networks import NetworkCollection

from api.schemas.network.schema import NetworkSchema
from data.motors import get_mongo
from utils.consts import DATA

from server import conf


router: APIRouter = APIRouter()


@router.get(
    '/all',
    response_description='Obtiene todas las redes en la base de datos.',
    # Asegúrate de que NetworkCollection esté definido
    response_model=NetworkCollection,
    response_model_by_alias=False,
)
async def list_networks(quantity: int = Query(default=10, ge=1)):
    try:
        db = await get_mongo()
        networks = await db.find().to_list(length=quantity)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={DATA: jsonable_encoder(
                NetworkCollection(networks=networks)
            )}
        )
    except ServerSelectionTimeoutError:
        print('Error conectando a MongoDB remoto, caída en vuelta a MongoDB local.')
        conf.use_locale_nosql()
        db = await get_mongo()
        # Re-obtener la colección de la base de datos local
        networks = await db.find().to_list(length=quantity)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={DATA: jsonable_encoder(
                NetworkCollection(networks=networks)
            )}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    '/{id}',
    response_description='Obtiene una red por su ID.',
    response_model=NetworkSchema,
    response_model_by_alias=False,
)
async def get_network_by_id(id: str):
    try:
        db = await get_mongo()
        if (
            network := await db.find_one({'_id': ObjectId(id)})
        ) is not None:
            return network
    except ServerSelectionTimeoutError:
        print('Error connecting to remote MongoDB, falling back to local MongoDB.')
        conf.use_locale_nosql()
        db = await get_mongo()
        if (
            network := await db.find_one({'_id': ObjectId(id)})
        ) is not None:
            return network
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    '/',
    response_description='Añade una nueva red a la base de datos.',
    response_model=NetworkSchema,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_network(network: NetworkSchema = Body(...)):
    try:
        db = await get_mongo()
        new_network: any = await db.insert_one(
            network.model_dump(by_alias=True, exclude=['id'])
        )
        stored_network = await db.find_one({'_id': new_network.inserted_id})
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={DATA: jsonable_encoder(
                NetworkSchema(**stored_network)
            )}
        )
    except ServerSelectionTimeoutError:
        print('Error connecting to remote MongoDB, falling back to local MongoDB.')
        conf.use_locale_nosql()
        db = await get_mongo()

        new_network: any = await db.insert_one(
            network.model_dump(by_alias=True, exclude=['id'])
        )
        stored_network = await db.find_one({'_id': new_network.inserted_id})
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={DATA: jsonable_encoder(
                NetworkSchema(**stored_network)
            )}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put(
    '/{id}',
    response_description='Actualiza una red por su ID.',
    response_model=NetworkSchema,
    response_model_by_alias=False,
)
async def update_network(id: str, network: NetworkSchema = Body(...)):
    '''
    Actualiza un registro de Red única en la base de datos.
    '''
    try:
        db = await get_mongo()
        stored_network = await db.find_one({'_id': ObjectId(id)})
        if stored_network is not None:
            update_result = await db.update_one(
                {'_id': ObjectId(id)},
                {'$set': network.dict(by_alias=True, exclude={'id'})}
            )
            if update_result.modified_count == 1:
                return JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content={DATA: jsonable_encoder(
                        NetworkSchema(**network.dict(), id=id)
                    )}
                )
    except ServerSelectionTimeoutError:
        print('Error connecting to remote MongoDB, falling back to local MongoDB.')
        conf.use_locale_nosql()
        db = await get_mongo()
        stored_network = await db.find_one({'_id': ObjectId(id)})
        if stored_network is not None:
            update_result = await db.update_one(
                {'_id': ObjectId(id)},
                {'$set': network.dict(by_alias=True, exclude={'id'})}
            )
            if update_result.modified_count == 1:
                return JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content={DATA: jsonable_encoder(
                        NetworkSchema(**network.dict(), id=id)
                    )}
                )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'network {id} not found'
    )


@router.delete(
    '/{id}',
    response_description='La Red ha sido eliminada.'
)
async def delete_network(id: str):
    '''
    Elimina un registro de Red única de la base de datos.
    '''
    try:
        db = await get_mongo()
        delete_result = await db.delete_one({'_id': ObjectId(id)})
        if delete_result.deleted_count == 1:
            return Response(
                status_code=status.HTTP_204_NO_CONTENT
            )
    except ServerSelectionTimeoutError:
        print('Error connecting to remote MongoDB, falling back to local MongoDB.')
        conf.use_locale_nosql()
        db = await get_mongo()
        delete_result = await db.delete_one({'_id': ObjectId(id)})
        if delete_result.deleted_count == 1:
            return Response(
                status_code=status.HTTP_204_NO_CONTENT
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

# @router.get('/delete_all', response_description='Elimina todos los documentos en la colección')
# async def delete_all_documents():
#     try:
#         collection = await get_mongo()
#         result = await collection.delete_many(
#             {
#                 # Elimina todos los documentos

#             }
#         )
#         # return {'deleted_count': result.deleted_count}
#     except ServerSelectionTimeoutError:
#         print('Error connecting to remote MongoDB, falling back to local MongoDB.')
#         conf.use_locale_nosql()
#         collection = await get_mongo(locale=True)
#         result = await collection.delete_many({})
#         return {'deleted_count': result.deleted_count}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @router.delete(
#     '/all',
#     response_description='Todas las redes han sido eliminadas.'
# )
# @router.delete(
#     '/delete_all',
#     response_description='Elimina todos los documentos en la colección'
# )
# async def delete_all_networks():
#     '''
#     Elimina todos los registros de Red de la base de datos.
#     '''
#     try:
#         db = await get_mongo()
#         result = await db.delete_many({})
#         return {'deleted_count': result.deleted_count}
#     except ServerSelectionTimeoutError:
#         print('Error connecting to remote MongoDB, falling back to local MongoDB.')
#         conf.use_locale_nosql()
#         db = await get_mongo(locale=True)
#         result = await db.delete_many({})
#         return {'deleted_count': result.deleted_count}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# async def delete_all_documents():
