from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter(tags=["inventory"])


class InventoryItem(BaseModel):
    sku: str
    quantity: int
    warehouse: str


class InventoryResponse(BaseModel):
    items: list[InventoryItem]
    page: int
    page_size: int
    total: int


@router.get("/inventory", response_model=InventoryResponse)
def get_inventory(page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)) -> InventoryResponse:
    seed = [
        InventoryItem(sku="SKU-RED-001", quantity=120, warehouse="PHX"),
        InventoryItem(sku="SKU-BLU-002", quantity=48, warehouse="LAX"),
    ]
    return InventoryResponse(items=seed, page=page, page_size=page_size, total=len(seed))
