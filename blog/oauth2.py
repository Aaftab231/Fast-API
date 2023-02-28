from fastapi import Depends, HTTPException, status
from . import JWTtoken
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate your request",
        headers={"WWW-Authenticate":"Bearer"}
        )
    
    return JWTtoken.verify_access_token(token, credentials_exception)