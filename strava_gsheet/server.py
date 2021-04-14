"""Main API entrypoint."""

# Standard Library
import os
from datetime import timedelta

# Third Party Libraries
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from .api.auth import authenticate_user, create_access_token, get_current_active_user
from .core.models.token import Token
from .core.models.user import User

load_dotenv()

app = FastAPI()


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """Load details about currently logged in user."""
    return current_user


@app.get("/greet")
async def greet(current_user: User = Depends(get_current_active_user)):
    """Greet logged in user."""
    return {"message": "Hello World", "user": current_user}


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Generate Access Token by posting an OAuth2 compliant POST request."""
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
