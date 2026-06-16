import sys
import json
from main_controller import process_query

if __name__ == "__main__":
    try:
        data = json.loads(sys.argv[1])

        text = data["text"]
        user = data["user"]

        result = process_query(text, user)

        print(result)

    except Exception as e:
        print("Error:", e)