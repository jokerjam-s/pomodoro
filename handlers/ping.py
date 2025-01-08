from fastapi import APIRouter


router = APIRouter(prefix="/ping", tags=["ping"])

@router.get("/app")
async def ping():
    return {'message': 'ok'}