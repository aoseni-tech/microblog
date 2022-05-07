from utils.mongo_schema import microblog_db

entry_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["content", "first_name", "last_name", "date_posted"],
        "properties": {
            "content": {
                "bsonType": "string",
                "minLength": 20,
                "description": "Article content can not be empty, it must be at least 20 characters",
            },
            "first_name": {"bsonType": "string", "minLength": 1, "description": "First name can not be empty"},
            "last_name": {"bsonType": "string", "minLength": 1, "description": "Last name can not be empty"},
            "date_posted": {"bsonType": "date", "description": "Date is required to post an article"},
        },
    }
}

entries = microblog_db.document('entries', entry_schema)