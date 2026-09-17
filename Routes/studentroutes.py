from pydantic import BaseModel,Field
from typing import Annotated,Optional
from fastapi import APIRouter
from Models.Studentstruct import StudentStruct
from Models.updatestudent import UpdateStruct
from Database.connection import collection

router=APIRouter()

@router.post("/createstud")
def createstd(student:StudentStruct):
    sname=student.name
    sroll=student.roll
    sage=student.age
    semail=student.email

    sinfo = {
        "name":sname,
        "roll":sroll,
        "age":sage,
        "email":semail
    }

    collection.insert_one(sinfo)
    return{"message":"student Created successully"}


@router.get("/stundetlist")
def getall():
    alldata=list(collection.find({},{"_id":0}))
    return alldata


@router.put("/edit/{roll}")
def updatestudent(roll:int,studentinfo:UpdateStruct):
    alldata=list(collection.find({},{"_id":0}))

    data={}


    for i in alldata:
        if i["roll"]==roll:

            if studentinfo.name != None:
                data["name"]=studentinfo.name

            if studentinfo.age != None:
                data["age"]=studentinfo.age

            if studentinfo.email != None:
                data["email"]=studentinfo.email

            collection.update_one(
                {"roll":roll},
                {"$set":data}
            )

            return{"message":"User Created Succesfully"}

@router.delete("/delete/{roll}")
def deteletdata(roll:int):
    alldata=list(collection.find({},{"_id":0}))

    for i in alldata:
        if i["roll"]==roll:
            collection.delete_one({"roll":roll})
            return{"message":"student deleted siccesfully"}

