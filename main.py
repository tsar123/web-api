import apps.Idea.models as modelsI
import apps.User.models as modelsU

from fastapi import FastAPI
from database import engine
from routes import router_websocket, router_users, router_directions, router_ideas


modelsI.Base.metadata.create_all(bind=engine)
modelsU.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_websocket)
app.include_router(router_users)
app.include_router(router_directions)
app.include_router(router_ideas)