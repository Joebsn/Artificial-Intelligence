# %% Imports and models
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

inputs = tokenizer("Explain AI in simple terms", return_tensors="pt")

# %% Temperature sampling
output = model.generate(**inputs, max_length=50, temperature=0.7, do_sample=True)
print(tokenizer.decode(output[0], skip_special_tokens=True))

# %% Top K sampling
output = model.generate(**inputs, max_length=50, top_k=50, do_sample=True)
print(tokenizer.decode(output[0], skip_special_tokens=True))

# %% Top P sampling
output = model.generate(**inputs, max_length=50, top_p=0.9, do_sample=True)
print(tokenizer.decode(output[0], skip_special_tokens=True))