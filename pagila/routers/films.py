from fastapi import APIRouter

router = APIRouter(prefix="/films", tags=["films"], )


@router.get("/")
def get_films():
    return {"success": True, "data": []}
