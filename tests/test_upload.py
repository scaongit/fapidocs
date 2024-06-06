import io


def test_upload_file(test_client):
    # Mock file to upload
    file_content = b"test file content"
    file = io.BytesIO(file_content)
    files = {'files': ('testfile.txt', file, 'text/plain')}

    response = test_client.post("/upload", files=files)

    assert response.status_code == 200
    assert "file_id" in response.json()
