from app import app
import os

if __name__ == "__main__":
    app.run(debug=bool(os.getenv("DEBUG")), host="0.0.0.0", port=80)