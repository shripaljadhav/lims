
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from ..hashing import Hash

def create(request: schemas.User,db:Session):
    new_user = models.User(firstname=request.firstname,lastname=request.firstname,bio=request.bio,email=request.email,companyname=request.companyname,website=request.website,address=request.address,country=request.country,state=request.state,city=request.city,
    zipcode=request.zipcode,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user