from pydantic import BaseModel

# We created a class and we have to inherit the base model if want to use 
# pydantic. In this, we have to specify what variables are going to be in post method
class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float