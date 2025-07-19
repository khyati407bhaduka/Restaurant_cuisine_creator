from fastapi import FastAPI
from enum import Enum
app = FastAPI()  #created instance of fast api
class Available_cuisine(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

food_items = {
    "indian" :["samosa","Dosa"],
    "american" :["Hot Dog","Apple pie"],
    "italian" :["pasta","pizza"]
}

valid_cuisines =food_items.keys()

@app.get("/get_items/{cuisine}")

async def get_items(cuisine :Available_cuisine):
    return food_items.get(cuisine)

discount_code = {
    1: "10%",
    2: "20%",
    3: "30%"
}

@app.get("/get_coupon/{code}")

async def coupon_code(code :int):
    return {"discount":discount_code.get(code)}