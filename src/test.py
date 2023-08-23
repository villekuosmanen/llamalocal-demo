from llama_cpp import Llama

prompt = "What is the largest country in the world by population?"
print(prompt)

llm = Llama(model_path="../models/llama-2-7b-chat.ggmlv3.q2_K.bin", verbose=False)

output = llm(prompt, max_tokens=124, echo=False, temperature=0.9)


print(output.get("choices")[0].get("text"))