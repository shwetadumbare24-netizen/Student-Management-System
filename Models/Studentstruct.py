from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,Optional




class StudentStruct(BaseModel):

    name: Annotated[str, Field(title="Enter Your Name")]

    roll: Annotated[int, Field(title="Enter Your Roll")]

    age: Annotated[int, Field(title="Enter Your Age")]

    email: Annotated[EmailStr, Field(title="Enter Your Email")]






