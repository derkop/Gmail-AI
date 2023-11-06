import os
import openai
openai.api_key = os.getenv("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")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)