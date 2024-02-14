from fastapi import FastAPI
import uvicorn
from user.infrastructure.routes.Routes import router, initialize_routes
from user.infrastructure.Factory.Repository import RepositoryFactory

repository_factory = RepositoryFactory()

repository = repository_factory.get_repository("sqlite")  

initialize_routes(repository)

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4321)