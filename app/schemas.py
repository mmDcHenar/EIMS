from pydantic import BaseModel


class ProductBase(BaseModel):
    id: str
    name: str
    stock: int
    minimum_stock: int


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    class Config:
        from_attributes = True


class ProductUpdate(ProductBase):
    pass
