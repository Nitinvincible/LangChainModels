from langchain import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI(model_name="gpt-3.5-turbo")

result = llm.invoke("Hello, how are you?")
print(result)