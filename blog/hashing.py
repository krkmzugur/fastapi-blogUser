from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"],deprecated ="auto")


class Hash():
    def bcrypt(password: str):
         hashed_password = pwd_ctx.hash(password)
         return hashed_password
    
    def verify(hashed_password,plain_password):
         return pwd_ctx.verify(plain_password,hashed_password)