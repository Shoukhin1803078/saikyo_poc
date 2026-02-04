from typing import List, Literal
from pydantic import BaseModel
from langchain_ollama import ChatOllama

# Predefined intents
ALL_INTENTS = ["identity", "work_content", "requirements", "compensation", "benefits", "logistics", "hiring_flow"]

# Pydantic model with Literal for strict validation
class IntentResponse(BaseModel):
    matched_intents: List[Literal[
        "identity", "work_content", "requirements", "compensation", "benefits", "logistics", "hiring_flow"
    ]]
llm = ChatOllama(
    model="qwen2.5:7b", 
    temperature=0,
    base_url="http://host.docker.internal:11434"
    )
llm_structured = llm.with_structured_output(IntentResponse)



def classify_intent(user_query: str) -> list[str]:

    # Defining the intent descriptions based on your chunking logic
    intent_definitions = """
    - identity: General job info (Media Site, Company Name, Job Title, Catchphrase, Industry, Category, Employment Type).
    - work_content: What the job involves (Job Description, Day-to-day work details, tasks, specific technologies/languages like Python/AI).
    - requirements: Necessary qualifications (Skills, Experience, Certifications, Education).
    - compensation: Money and trial periods (Salary, Pay details, Trial period terms).
    - benefits: Perks and time off (Social insurance, Welfare, Holidays, Leaves, specific tags).
    - logistics: Physical/time constraints (Working hours, Location, Address, Nearest station, Access details, Postal code).
    - hiring_flow: The process (Selection steps, Interview flow, Recruiter messages).
    """

    # prompt = (
    #     f"Classify this user query into relevant intents from the list: {ALL_INTENTS}\n"
    #     f"User query: {user_query}\n"
    #     "Return the intents only. Do not include any text outside the list."
    # )

    prompt = (
        "You are an expert intent classifier for a job search system. "
        "Analyze the user query and map it to the most relevant categories based on the definitions below:\n\n"
        f"{intent_definitions}\n"
        "---\n"
        f"User Query: \"{user_query}\"\n\n"
        "Task: Identify all intents that match the information provided or requested in the query."
    )

    llm_response=llm_structured.invoke(prompt)
    # print(F"llm_response======= {llm_response}")
    matched_intents=llm_response.matched_intents
    # print(F"matched_intents======== {matched_intents}")
    return matched_intents






# # Example usage
# user_query = "私はソフトウェアエンジニアです。AI/ML、Pythonの経験が4年あります。ダッカの勤務地で私の経験に基づいて仕事を提案してください。"
# response = classify_intent(user_query)
# print(response)  
# print(response.matched_intents)  # ['work_content', 'requirements']
















# # ----------------------------Using instructor----------------------------
# from typing import List, Literal
# from pydantic import BaseModel, Field
# import instructor

# ALL_INTENTS = ["identity", "work_content", "requirements", "compensation", "benefits", "logistics", "hiring_flow"]

# # Pydantic model with descriptions
# class IntentResponse(BaseModel):
#     matched_intents: List[Literal[
#         "identity", "work_content", "requirements", "compensation", "benefits", "logistics", "hiring_flow"
#     ]] = Field(..., description="List of intents that match the user query, chosen from the predefined list")

# # Instructor client
# client = instructor.from_provider("ollama/llama3")  # or any provider

# def classify_intent(user_query: str) -> IntentResponse:
#     """
#     Takes a user query and returns matched intents as a Pydantic IntentResponse.
#     """
#     # No need for extra prompt instructions; the Field description guides the LLM
#     llm_response = client.create(
#         response_model=IntentResponse,
#         messages=[{"role": "user", "content": user_query}]
#     )
#     return llm_response

# # Example usage
# user_query = "私はソフトウェアエンジニアです。AI/ML、Pythonの経験が4年あります。ダッカの勤務地で私の経験に基づいて仕事を提案してください。"
# response = classify_intent(user_query)

# print(f"response======= {response}")
# print(f"matched_intents======== {response.matched_intents}")  # ['work_content', 'requirements']

# # # Example usage
# # user_query = "私はソフトウェアエンジニアです。AI/ML、Pythonの経験が4年あります。ダッカの勤務地で私の経験に基づいて仕事を提案してください。"
# # response = classify_intent(user_query)
# # print(response)
# # print(response.matched_intents)