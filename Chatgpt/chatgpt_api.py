from openai import OpenAI

# It automatically get the API key from your environment variables,
# Note: you need to add API key in your environment variable, 
# Variable name must be->  OPENAI_API_KEY
client=OpenAI()

prompt="Tye your prompt here"
# Generating the SOP
completion = client.chat.completions.create(
    model="o1-mini",
    temperature=1,  # Controls randomness; higher values make it more creative result (range from 0 to 2)
    messages=[
        {
            "role": "user",
            "content": prompt + f"You can add any additional prompt here also"
        }
    ]
)

result = completion.choices[0].message.content.strip()
print(result)
