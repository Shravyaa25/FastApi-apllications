from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from models.address import Address
from schemas.address import AddressCreate, AddressResponse
from models.user import User

router = APIRouter(prefix="/address", tags=["Address"])

@router.post("/", response_model=AddressResponse)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    """Create a new address for a given user."""
    
    # Check if user exists
    user = db.query(User).filter(User.id == address.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Create new address
    new_address = Address(**address.dict())  # user_id is now inside AddressCreate
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address

@router.get("/{user_id}", response_model=list[AddressResponse])
def get_user_addresses(user_id: int, db: Session = Depends(get_db)):
    """Retrieve all addresses for a specific user."""
    
    # Check if user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch user addresses
    addresses = db.query(Address).filter(Address.user_id == user_id).all()
    return addresses
