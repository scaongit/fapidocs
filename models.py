from pydantic import BaseModel, Field
from typing import List, Dict


# File Upload Models
class FileUploadResponse(BaseModel):
    file_id: str = Field(..., description="Unique identifier for the uploaded file")


class FileUploadRequest(BaseModel):
    files: List[bytes] = Field(..., description="List of files to be uploaded")


# OCR Models
class OCRRequest(BaseModel):
    file_id: str = Field(..., description="Unique identifier of the file to process with OCR")


class OCRResponse(BaseModel):
    message: str = Field(..., description="Status message for the OCR request")


# Attribute Extraction Models
class ExtractRequest(BaseModel):
    query: str = Field(..., description="Query text for attribute extraction")
    file_id: str = Field(..., description="Unique identifier of the file to extract attributes from")


class ExtractResponse(BaseModel):
    attributes: Dict[str, str] = Field(..., description="Extracted attributes based on the query")


# Authentication Models
class Token(BaseModel):
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(..., description="Type of token, typically 'Bearer'")


class TokenData(BaseModel):
    username: str = Field(..., description="Username extracted from the token")


class User(BaseModel):
    username: str = Field(..., description="Username of the user")
    password: str = Field(..., description="Password of the user")
