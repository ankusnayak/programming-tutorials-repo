from source.db import save_user


def test_save_user(mocker):
    # Mock database connection
    mock_conn = mocker.patch("sqlite3.connect")

    mock_cursor = mock_conn.return_value.cursor.return_value

    # Function Call
    save_user("Ankus", 27)

    """
        ==========================================
        calling function to check if it's actually
        calling using the these data after mock.
        ==========================================
    """

    # Check if it's(mock function) actually calling using the parmas "users.db"
    mock_conn.assert_called_once_with("users.db")
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO users (name, age) VALUES (?, ?)", ("Ankus", 27)
    )
