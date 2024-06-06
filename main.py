from fastapi import FastAPI
from fastapi import APIRouter, HTTPException, BackgroundTasks, UploadFile, File, Depends

from routes.extract import extract_attributes
from routes.ocr import process_ocr
from utils.auth import get_current_user
from utils.storage import save_to_storage

app = FastAPI()
router = APIRouter()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/ocr")
async def ocr_file(file_id: str, background_tasks: BackgroundTasks, current_user: str = Depends(get_current_user)):
    background_tasks.add_task(process_ocr, file_id)
    return {"message": "OCR processing started"}


@router.post("/upload")
async def upload_file(file: UploadFile = File(...), current_user: str = Depends(get_current_user)):
    if file.content_type not in ["application/pdf", "image/tiff", "image/png", "image/jpeg"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    file_id = await save_to_storage(file)
    return {"file_id": file_id}


@router.post("/extract")
async def extract(query: str, file_id: str, current_user: str = Depends(get_current_user)):
    attributes = await extract_attributes(query, file_id)
    return {"attributes": attributes}
