from fastapi import APIRouter, Depends
from user.infrastructure.controllers.CreateUserController import create_user_router, initialize_endpoints as initialize_create_user
from user.infrastructure.controllers.VerifyUserController import verify_user_router, initialize_endpoints as initialize_verify_user
from user.infrastructure.controllers.listUsersController import get_list_user_router, initialize_endpoints as intialize_getList_Users
from user.infrastructure.controllers.LoginController import login_router, initialize_endpoints as initialize_login
from user.infrastructure.controllers.UserByIdController import get_user_by_id_router, initialize_endpoints as initialize_get_user_by_id
from user.infrastructure.controllers.PutUserController import update_user_router, initialize_endpoints as initialize_update_user
from user.infrastructure.controllers.DeleteUserController import delete_user_router, initialize_endpoints as initialize_delete_user
from user.infrastructure.middleware.auth import get_current_user
from user.infrastructure.controllers.LogoutController import logout_router, initialize_endpoints as initialize_logout


router = APIRouter()

def initialize_routes(repository):
    initialize_create_user(repository)
    initialize_verify_user(repository)
    intialize_getList_Users(repository)
    initialize_login(repository)
    initialize_get_user_by_id(repository)
    initialize_update_user(repository)
    initialize_delete_user(repository)
    initialize_logout(repository)
    
    router.include_router(create_user_router, prefix="/users", tags=["users"])
    router.include_router(verify_user_router, prefix="/users/{uuid}/verification", tags=["users"])
    router.include_router(login_router, prefix="/SignIn", tags=["users"])
    router.include_router(get_list_user_router, prefix="/users",tags=["users"], dependencies=[Depends(get_current_user)])
    router.include_router(get_user_by_id_router, prefix="/users/{user_id}", tags=["users"], dependencies=[Depends(get_current_user)])
    router.include_router(update_user_router, prefix="/users/{user_id}", tags=["users"], dependencies=[Depends(get_current_user)])
    router.include_router(delete_user_router, prefix="/users/{user_id}", tags=["users"], dependencies=[Depends(get_current_user)])
    router.include_router(logout_router, prefix="/logout", tags=["users"], dependencies=[Depends(get_current_user)])