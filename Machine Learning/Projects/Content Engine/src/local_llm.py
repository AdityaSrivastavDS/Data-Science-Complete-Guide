from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load GPT-2 Model and Tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
