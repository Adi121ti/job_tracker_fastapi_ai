from pydantic import BaseModel

class Product(BaseModel):
    name : str
    price: int
    in_stock : bool = True
    
product = Product(name ="socks", price ="abc", in_stock= False)

print(product)