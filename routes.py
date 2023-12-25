import schemas

from typing import List
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from database import get_db
from sqlalchemy.orm import Session
from crud import (
    create_user, get_users, get_user, update_user, delete_user,
    create_direction, get_directions, get_direction, update_direction, delete_direction,
    create_idea, get_ideas, get_idea, update_idea, delete_idea
)

router_websocket = APIRouter()
router_users = APIRouter(prefix='/users', tags=['user'])
router_directions = APIRouter(prefix='/directions', tags=['direction'])
router_ideas = APIRouter(prefix='/ideas', tags=['idea'])


# WebSocket
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []


    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)


    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)


    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)


    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


async def notify_clients(message: str):
    for connection in manager.active_connections:
        await connection.send_text(message)


@router_websocket.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(websocket)
    await manager.send_personal_message(f"Hi!")
    try:
        while True:
            data = await websocket.receive_text()
            create_idea()
            await manager.broadcast(f"User #{user_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)


# Users
@router_users.post("/", response_model=schemas.User)
async def create_user_route(schema: schemas.UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, schema)
    await notify_clients(f"user created: {user.first_name}")
    return user


@router_users.get("/", response_model=List[schemas.User])
async def read_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users


@router_users.get("/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    return user


@router_users.put("/{user_id}")
async def update_user_route(user_id: int, schema: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, schema)
    if updated_user:
        await notify_clients(f"user updated: {updated_user.name}")
        return updated_user
    return {"error": "User not found"}


@router_users.delete("/{user_id}")
async def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user(db, user_id)
    if deleted:
        await notify_clients(f"User deleted: ID {user_id}")
        return {"message": "Use deleted"}
    return {"error": "User not found"}


# Directions
@router_directions.post("/", response_model=schemas.Direction)
async def create_direction_route(direction_data: schemas.DirectionCreate, db: Session = Depends(get_db)):
    direction = create_direction(db, direction_data)
    await notify_clients(f"new direction added: {direction.name}")
    return direction


@router_directions.get("/", response_model=List[schemas.Direction])
async def read_directions(db: Session = Depends(get_db)):
    directions = get_directions(db)
    return directions


@router_directions.get("/{direction_id}", response_model=schemas.Direction)
async def read_direction(direction_id: int, db: Session = Depends(get_db)):
    direction = get_direction(db, direction_id)
    return direction


@router_directions.put("/{direction_id}", response_model=schemas.Direction)
async def update_direction_route(direction_id: int, direction_data: schemas.DirectionUpdate, db: Session = Depends(get_db)):
    updated_direction = update_direction(db, direction_id, direction_data)
    if updated_direction:
        await notify_clients(f"Direction {updated_direction.name} updated")
        return updated_direction
    return {"error": "Direction not found"}


@router_directions.delete("/{direction_id}")
async def delete_direction_route(direction_id: int, db: Session = Depends(get_db)):
    deleted = delete_direction(db, direction_id)
    if deleted:
        await notify_clients(f"Direction deleted: ID {direction_id}")
        return {"message": "Direction deleted"}
    return {"error": "Direction not found"}


# Ideas
@router_ideas.post("/", response_model=schemas.Idea)
async def create_idea_route(data: schemas.IdeaCreate, db: Session = Depends(get_db)):
    idea = create_idea(db, data)
    await notify_clients(f"new idea added: {idea.name}")
    return idea



@router_ideas.get("/", response_model=List[schemas.Idea])
async def read_ideas(db: Session = Depends(get_db)):
    ideas = get_ideas(db)
    return ideas


@router_ideas.get("/{idea_id}", response_model=schemas.Idea)
async def read_idea(idea_id: int, db: Session = Depends(get_db)):
    idea = get_idea(db, idea_id)
    return idea


@router_ideas.put("/{idea_id}")
async def update_idea_route(idea_id: int, schema: schemas.IdeaUpdate, db: Session = Depends(get_db)):
    updated_idea = update_idea(db, idea_id, schema)
    if updated_idea:
        await notify_clients(f"Idea updated: {updated_idea.name}")
        return updated_idea
    return {"error": "Idea not found"}


@router_ideas.delete("/{idea_id}")
async def delete_idea_route(idea_id: int, db: Session = Depends(get_db)):
    deleted = delete_idea(db, idea_id)
    if deleted:
        await notify_clients(f"Idea deleted: ID {idea_id}")
        return {"message": "Idea deleted"}
    return {"error": "Idea not found"}
