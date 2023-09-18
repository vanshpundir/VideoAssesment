import openai
openai.api_base = 'http://localhost:1234/v1'
openai.api_key = ''
prefix = "### Instruction:\n"
suffix = "\n### Response:"

def get_completion(prompt, model = "local model",temperature =0.0):
    formatted_prompt =f"{prefix}{prompt}{suffix}"
    messages = [{"role": "user", "content": formatted_prompt}]
    print("you prompted", prompt)
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = temperature
    )
    return response.choices[0].message['content']

print(get_completion("What is capital of china?"))