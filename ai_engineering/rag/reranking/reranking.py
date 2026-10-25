# %% Add imports and dependencies
import os
import cohere
from google import genai
from openai import OpenAI

# %% Iniailize API keys and clients
os.environ["COHERE_API_KEY"] = ""
os.environ["OPENAI_API_KEY"] = ""
os.environ["GEMINI_API_KEY"] = ""

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
co = cohere.Client(api_key=os.getenv("COHERE_API_KEY"))

# %% Define query prompt
query = """Compare and contrast the long-term societal, economic, 
        and philosophical consequences of Artificial General Intelligence (AGI) 
        emerging under three paradigms:
        1. Open-source decentralized AGI driven by global collaboration.
        2. Corporate-controlled proprietary AGI systems optimized for profit.
        3. Government-regulated AGI programs under national sovereignty.
        Discuss governance, inequality, innovation speed, and global cooperation.
        Conclude which path is most sustainable for humanity and why."""

# %% Define model responses functions
def safe_generate_openai(prompt):
    try:
        res = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        return f"Error fetching from OpenAI: {e}"

def safe_generate_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        res = model.generate_content(prompt)
        return res.text.strip()
    except Exception as e:
        return f"Error fetching from Gemini: {e}"

def dummy_response(prompt):
    return f"Simulated response for: {prompt[:300]}..."

# %% Collect responses from all models
candidates = [
    ("OpenAI GPT-4o-mini", safe_generate_openai(query)),
    ("Google Gemini 2.5 Flash", safe_generate_gemini(query)),
    ("Dummy Baseline", dummy_response(query))
]

# %% Debugging and Validating Candidates
print("=== Debug: Raw candidates ===\n")

valid_docs, model_names = [], []

for idx, (model, text) in enumerate(candidates):
    print(f"{idx}: <class 'str'> -> ({model}, {shorten(text, width=120)})\n")
    if text and not text.lower().startswith("error"):
        valid_docs.append(text)
        model_names.append(model)
    else:
        print(f"Skipping invalid or empty document from {model}\n")

print(f"Valid documents for reranking: {len(valid_docs)}\n")

if not valid_docs:
    raise ValueError("No valid text found for reranking.")

# %% Apply Cohere Reranking
rerank_results = co.rerank(
    model="rerank-english-v3.0",
    query=query,
    documents=valid_docs,
    top_n=len(valid_docs)
)

# %% Display Final Ranked Results
print("=== Final Ranked Results by Cohere Reranker ===\n")

scores, labels = [], []

for rank, result in enumerate(rerank_results.results, start=1):
    score = round(result.relevance_score, 3)
    model_name = model_names[result.index]
    doc_text = getattr(result.document, "text",
                       None) or valid_docs[result.index]
    snippet = shorten(doc_text, width=400)

    print(f"Rank {rank} | {model_name} | Score: {score}\n{snippet}\n")

    scores.append(score)
    labels.append(model_name)