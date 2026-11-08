# %% Model parameters
from transformers import AutoModelForCausalLM, AutoTokenizer

gen_config = {
    "model_name": "gpt2",           
    "max_length": 128,          # maximum number of tokens to generate in the output.   
    "temperature": 0.8,         # controls randomness as lower is more focused and higher is more random     
    "top_p": 0.9,               # nucleus sampling as picks tokens from the smallest set whose total probability ≥ 0.9   
    "top_k": 50,                # limits choices to the top 50 most likely tokens. 
    "repetition_penalty": 1.2,  # discourages repeating the same words or phrases by lowering their probability    
    "num_return_sequences": 3   # umber of separate outputs the model should generate for the same prompt   
}
tokenizer = AutoTokenizer.from_pretrained(gen_config["model_name"])
model = AutoModelForCausalLM.from_pretrained(gen_config["model_name"])

prompt = "Write a short, upbeat mission statement for a student studying AI at night:"

input_ids = tokenizer(prompt, return_tensors="pt").input_ids
outputs = model.generate(
    input_ids,
    max_length=gen_config["max_length"],
    do_sample=True,
    temperature=gen_config["temperature"],
    top_p=gen_config["top_p"],
    top_k=gen_config["top_k"],
    repetition_penalty=gen_config["repetition_penalty"],
    num_return_sequences=gen_config["num_return_sequences"],
    eos_token_id=tokenizer.eos_token_id,
)
for i, out in enumerate(outputs):
    text = tokenizer.decode(out, skip_special_tokens=True)
    print(f"Generation {i+1}\n{text}\n")
# %%
