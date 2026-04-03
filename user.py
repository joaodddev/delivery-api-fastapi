# proteção na rota

from app.api.deps import get_current_user

@router.get("/me")
def get_me(user: str = Depends(get_current_user)):
    return {"user": user}