from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from src.schema import ReviewAnalysis

load_dotenv()

class ReviewAnalyzer:

    def __init__(self):

        self.model = ChatOpenAI(
            model="gpt-5-mini",
            temperature=0
        )

        self.structured_model = self.model.with_structured_output(
            ReviewAnalysis
        )

    def analyze_review(self, review: str):

        result = self.structured_model.invoke(review)

        return result