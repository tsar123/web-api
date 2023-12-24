import schemas

from sqlalchemy.orm import Session
from apps.User.models import User
from apps.Idea.models import Direction, Idea


# User
def create_user(db: Session, schema: schemas.UserCreate):
    db_user = User(**schema.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter_by(id=user_id).first()


def update_user(db: Session, user_id: int, data: schemas.UserUpdate):
    db_user = db.query(User).filter_by(id=user_id).first()
    data = data if isinstance(data, dict) else data.model_dump()

    if db_user:
        for key, value in data.items():
            if hasattr(db_user, key):
                setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user
    return None


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter_by(id=user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False


# Direction
def create_direction(db: Session, schema: schemas.DirectionCreate):
    db_direction = Direction(**schema.model_dump())
    db.add(db_direction)
    db.commit()
    db.refresh(db_direction)
    return db_direction


def get_directions(db: Session):
    return db.query(Direction).all()


def get_direction(db: Session, direction_id: int):
    return db.query(Direction).filter_by(id=direction_id).first()


def update_direction(db: Session, direction_id: int, data: schemas.DirectionUpdate | dict):
    db_direction = db.query(Direction).filter_by(id=direction_id).first()
    data = data if isinstance(data, dict) else data.model_dump()

    if db_direction:
        for key, value in data.items():
            if hasattr(db_direction, key):
                setattr(db_direction, key, value)
        db.commit()
        db.refresh(db_direction)
    return db_direction


def delete_direction(db: Session, direction_id: int):
    db_direction = db.query(Direction).filter_by(id=direction_id).first()
    if db_direction:
        db.delete(db_direction)
        db.commit()
        return True
    return False


# Idea
def create_idea(db: Session, schema: schemas.IdeaCreate):
    db_idea = Idea(**schema.model_dump())
    db.add(db_idea)
    db.commit()
    db.refresh(db_idea)
    return db_idea


def get_ideas(db: Session):
    return db.query(Idea).all()


def get_idea(db: Session, idea_id: int):
    return db.query(Idea).filter_by(id=idea_id).first()


def update_idea(db: Session, idea_id: int, data: schemas.IdeaUpdate | dict):
    db_idea = db.query(Idea).filter_by(id=idea_id).first()
    data = data if isinstance(data, dict) else data.model_dump()

    if db_idea:
        for key, value in data.items():
            if hasattr(db_idea, key):
                setattr(db_idea, key, value)

        db.commit()
        db.refresh(db_idea)
        return db_idea
    return None


def delete_idea(db: Session, idea_id: int):
    db_idea = db.query(Idea).filter_by(id=idea_id).first()
    if db_idea:
        db.delete(db_idea)
        db.commit()
        return True
    return False
