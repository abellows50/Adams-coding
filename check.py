import db
import build.solutions as solutions

def test_check_db():
    # Test valid database
    valid_result = db.check_db("build/valid_db.txt")
    expected_valid_result = solutions.check_db("build/valid_db.txt")
    assert valid_result is not None, "check_db returned None for valid database"
    assert expected_valid_result is not None, "Solution check_db returned None for valid database"
    assert valid_result[0] == expected_valid_result[0], f"Expected {expected_valid_result}, got {valid_result}"
    assert valid_result[1] == expected_valid_result[1], f"Expected {expected_valid_result}, got {valid_result}"

    # Test invalid database
    invalid_result = db.check_db("build/invalid_db.txt")
    expected_invalid_result = solutions.check_db("build/invalid_db.txt")
    assert invalid_result is not None, "check_db returned None for invalid database"
    assert expected_invalid_result is not None, "Solution check_db returned None for invalid database"
    assert invalid_result[0] == expected_invalid_result[0], f"Expected {expected_invalid_result}, got {invalid_result}"
    assert invalid_result[1] == expected_invalid_result[1], f"Expected {expected_invalid_result}, got {invalid_result}"

def test_query_for():
    # Test querying by name
    name_query_result = db.query_for("build/valid_db.txt", name="book1")
    expected_name_query_result = solutions.query_for("build/valid_db.txt", name="book1")
    assert name_query_result is not None, "query_for returned None for name query"
    assert expected_name_query_result is not None, "Solution query_for returned None for name query"
    assert len(name_query_result) == len(expected_name_query_result), f"Expected {len(expected_name_query_result)} results, got {len(name_query_result)}"

    # Test querying by fantastical rating
    fantastical_query_result = db.query_for("build/valid_db.txt", fantastical=3)
    expected_fantastical_query_result = solutions.query_for("build/valid_db.txt", fantastical=3)
    assert fantastical_query_result is not None, "query_for returned None for fantastical query"
    assert expected_fantastical_query_result is not None, "Solution query_for returned None for fantastical query"
    assert len(fantastical_query_result) == len(expected_fantastical_query_result), f"Expected {len(expected_fantastical_query_result)} results, got {len(fantastical_query_result)}"

def test_remove_entry():
    # Create a test book to remove
    book_to_remove = db.Book.Book("book_to_remove", 3, 3, 3, 3)
    db.add_entry("build/test_db.txt", book_to_remove)

    # Remove the book
    remove_result = db.remove_entry("build/test_db.txt", book_to_remove)
    expected_remove_result = solutions.remove_entry("build/test_db.txt", book_to_remove)
    assert remove_result == expected_remove_result, f"Expected {expected_remove_result}, got {remove_result}"

    # Verify the book is removed
    query_result = db.query_for("build/test_db.txt", name="book_to_remove")
    assert len(query_result) == 0, f"Expected 0 results, got {len(query_result)}"

if __name__ == "__main__":
    test_check_db()
    test_query_for()
    test_remove_entry()
    print("All tests passed!")



