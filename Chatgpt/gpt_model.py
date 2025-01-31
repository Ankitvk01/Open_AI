from openai import OpenAI

# It automatically get the API key from your environment variables,
# Note: you need to add API key in your environment variable, 
# Variable name must be->  OPENAI_API_KEY
client=OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    temperature=0.3,  # Controls randomness; higher values make it more creative range from 0 to 2 (optional)
    top_p=0.9,  # Limits token selection to top probable tokens for natural flow (optional)
    presence_penalty=0.6,  # Encourages the model to explore less-used phrases (optional)
    frequency_penalty=0.4,  # Reduces repetitiveness (optional)
    messages=[
        {
            "role": "system",
            "content": ("Type system prompt here...."),
        },
        {
            "role": "user",
            "content": ("Type user prompt....."),
        },
    ]
    )

# Extract the generated introduction
result = completion.choices[0].message.content.strip()