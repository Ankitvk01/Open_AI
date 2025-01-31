from openai import OpenAI

client=OpenAI(api_key="your api key" , base_url="https://api.deepseek.com")

prompt="Tye your prompt here"
# Generating the SOP
completion = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {
            "role": "user",
            "content": prompt + f"You can add any additional prompt here also"
        }
    ]
)

reasoning_content=completion.choices[0].message.reasoning_content
content = completion.choices[0].message.content.strip()
print(content)