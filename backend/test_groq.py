from app.config.groq_client import client

response = client.chat.completions.create(
    model="gemma2-9b-it",
    messages=[
        {
            "role": "user",
            "content": "Reply with only: Groq Working"
        }
    ]
)

print(response.choices[0].message.content)