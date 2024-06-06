def test_ocr_file(test_client):
    file_id = "mock_file_id"  # Replace with a valid file_id if available

    response = test_client.post("/ocr", json={"file_id": file_id})

    assert response.status_code == 200
    assert response.json() == {"message": "OCR processing started"}
