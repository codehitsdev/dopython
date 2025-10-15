from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models, schemas

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed = pwd.hash(user.password)
    obj = models.User(email=user.email, password_hash=hashed)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def verify_password(plain: str, hashed: str) -> bool:
    return pwd.verify(plain, hashed)

def authenticate(db: Session, email: str, password: str):
    u = get_user_by_email(db, email)
    if not u:
        return None
    if not verify_password(password, u.password_hash):
        return None
    return u

def create_item(db: Session, item: schemas.ItemCreate) -> models.Item:
    obj = models.Item(name=item.name, price=item.price)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def list_items(db: Session):
    return db.query(models.Item).order_by(models.Item.id.desc()).all()
