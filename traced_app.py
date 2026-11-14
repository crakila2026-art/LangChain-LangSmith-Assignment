
from langchain_openai import ChatOpenAI

# Initialize the OpenAI model through LangChain
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Three different prompts
prompts = [
    "Explain Artificial Intelligence in simple terms.",
    
    "Explain the difference between Data Lake and Data Warehouse with examples.",
    
    "Explain how LangChain and LangSmith work together in an enterprise Generative AI application."
]

# Execute all three prompts
for i, prompt in enumerate(prompts, start=1):

    print("\n" + "=" * 60)
    print(f"RUN {i}")
    print("=" * 60)

    print("PROMPT:", prompt)

    response = llm.invoke(prompt)

    print("\nANSWER:")
    print(response.content)

    print("\nTOKEN USAGE:")
    print(response.usage_metadata)
