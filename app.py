from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

component = input("Enter electronic component name: ")

prompt = f"Describe the electronic component {component}:"

result = generator(prompt, max_length=50, num_return_sequences=1)

print(result[0]['generated_text'])
