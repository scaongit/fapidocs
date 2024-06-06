from aiofiles import open as async_open

async def save_to_storage(file: UploadFile) -> str:
    async with async_open(f"/storage/{file.filename}", 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    return file.filename
