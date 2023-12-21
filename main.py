import apps.Idea.models as modelsI
import apps.User.models as modelsU

from fastapi import FastAPI
from database import engine


modelsI.Base.metadata.create_all(bind=engine)
modelsU.Base.metadata.create_all(bind=engine)

app = FastAPI()