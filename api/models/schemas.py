from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SandwichBase(BaseModel):
    sandwich_name: str
    price: float


class SandwichCreate(SandwichBase):
    pass


class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None


class Sandwich(SandwichBase):
    id: int

    class ConfigDict:
        from_attributes = True


class ResourceBase(BaseModel):
    item: str
    amount: int


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None


class Resource(ResourceBase):
    id: int

    class ConfigDict:
        from_attributes = True


class RecipeBase(BaseModel):
    amount: int


class RecipeCreate(RecipeBase):
    amount: int
    sandwich_id: int
    resource_id: int
    recipe_name: str

    # Added to help ensure the validation for optional fields
    class Config:
        orm_mode = True  # This helps FastAPI to work correctly with SQLAlchemy models


class RecipeUpdate(BaseModel):
    sandwich_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount: Optional[int] = None
    recipe_name: Optional[str] = None  # Added for consistency in updates

    class Config:
        orm_mode = True


class Recipe(RecipeBase):
    id: int
    sandwich: Sandwich = None
    resource: Resource = None
    recipe_name: str  # Added this for consistency and correct mapping to the database model

    class Config:
        orm_mode = True  # Helps with automatic data transformation for responses


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    sandwich_id: int
    quantity: int


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    amount: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    sandwich: Sandwich = None

    class ConfigDict:
        from_attributes = True


class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = [None]

    class ConfigDict:
        from_attributes = True
