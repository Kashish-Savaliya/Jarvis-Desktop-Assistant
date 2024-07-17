import openai
# from config import apikey
openai.api_key = "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"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Write an email to my boss for resignation",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].text.strip())
