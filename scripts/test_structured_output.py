import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

# 1. Define the structured output shape
class CodeReview(BaseModel):
    verdict: str = Field(description="'pass' or 'fail'")
    issues: list[str] = Field(description="List of problems found in the code")
    score: int = Field(description="Code quality score from 0 to 10")
    suggestion: str = Field(description="One concrete improvement suggestion")


# 2. LLM with structured output — uses native tool-calling, no format instructions needed
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
)
structured_llm = llm.with_structured_output(CodeReview, method="json_mode")

# 3. Prompt — instruct the model to return JSON explicitly
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a senior Python code reviewer. "
        "You must respond with a JSON object only using exactly these keys: "
        "verdict (string: 'pass' or 'fail'), "
        "issues (array of strings), "
        "score (integer 0-10), "
        "suggestion (string).",
    ),
    ("human", "Review this code:\n\n{code}"),
])

# 4. Chain
chain = prompt | structured_llm

# 5. Invoke
result = chain.invoke({
    "code": """
def get_user(id):
    import db
    user = db.query("SELECT * FROM users WHERE id=" + id)
    return user
""",
})

# result is a CodeReview object — not a string
print("Verdict   :", result.verdict)
print("Score     :", result.score)
print("Issues    :", result.issues)
print("Suggestion:", result.suggestion)
