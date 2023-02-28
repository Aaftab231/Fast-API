from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(pswd):
        return pwd_context.hash(pswd)
    
    def verify(hashed_password, plain_password):
        return pwd_context.verify(plain_password, hashed_password)