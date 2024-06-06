def test_extract_attributes(test_client):
    file_id = "mock_file_id"  # Replace with a valid file_id if available
    query = "mock_query_text"

    response = test_client.post("/extract", json={"query": query, "file_id": file_id})

    assert response.status_code == 200
    assert "attributes" in response.json()
