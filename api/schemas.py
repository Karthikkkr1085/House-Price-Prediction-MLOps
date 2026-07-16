from pydantic import BaseModel


class HouseData(BaseModel):
    property_type: str
    location: str
    city: str
    province_name: str
    latitude: float
    longitude: float
    baths: int
    purpose: str
    bedrooms: int
    Area_Type: str
    Area_Size: float
    Area_Category: str