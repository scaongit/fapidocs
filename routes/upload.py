from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from utils.storage import save_to_storage
from utils.auth import get_current_user

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...), current_user: str = Depends(get_current_user)):
    if file.content_type not in ["application/pdf", "image/tiff", "image/png", "image/jpeg"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    file_id = await save_to_storage(file)
    return {"file_id": file_id}
