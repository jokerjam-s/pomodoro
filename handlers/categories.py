from typing import List

from fastapi import APIRouter

from fixtures import categories
from schema.category import Category

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/all", response_model=List[Category])
async def all_categories():
    return categories


@router.get("/{category_id}", response_model=Category)
async def category_by_id(category_id: int):
    for category in categories:
        if category["id"] == category_id:
            return category


@router.post("/", response_model=Category)
async def category_create(category: Category):
    categories.append(category)
    return category


@router.put("/{category_id}", response_model=Category)
async def category_update(category_id: int, category: Category):
    for c in categories:
        if c["id"] == category_id:
            c["name"] = category["name"]


@router.delete("/{category_id}", response_model=Category)
async def category_delete(category_id: int):
    for c in categories:
        if c["id"] == category_id:
            categories.remove(c)
