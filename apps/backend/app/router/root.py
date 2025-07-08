from fastapi import APIRouter

from ..models.root import Root

router = APIRouter()


@router.get("/")
def read_root() -> Root:
    return Root(Hello="World")
