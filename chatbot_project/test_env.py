import os
from dotenv import load_dotenv
print("got here")
load_dotenv()
print("got here too")
print(os.getenv("SERPER_API_KEY"))