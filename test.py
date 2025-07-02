import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.getcwd(), ".env")
print("Looking for .env at:", dotenv_path)

# Load .env file
load_dotenv(dotenv_path)

# Print out the value
print("DATABASE_URL =", os.getenv("DATABASE_URL"))
