from fastapi import FastAPI
from app.controllers.quote_controller import router as quote_router
from app.controllers.exchange_controller import router as exchange_router
from app.controllers.transaction_controller import router as transaction_router
from app.controllers.user_controller import router as user_router

#Nombre del API y la version 
def create_app() -> FastAPI:
    app = FastAPI(title="Currency Exchange API", version="1.0.0")

# controladores y nombres de los servicios
    app.include_router(user_router, prefix="/api/v1", tags=["Users"])
    app.include_router(quote_router, prefix="/api/v1", tags=["Exchange currency"])
    app.include_router(exchange_router, prefix="/api/v1", tags=["Exchange currency per Users"])
    app.include_router(transaction_router, prefix="/api/v1", tags=["Transactions"])
    return app
