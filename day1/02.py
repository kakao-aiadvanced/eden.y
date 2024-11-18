import config
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": 
         """
         Decide if a given movie review is positive or negative.
         It's so bored. -> Negative
         The best movie of my life. -> Positive
         Must see movies -> Positive
         I hated this movie. -> Negative
         """
         },
        {
            "role": "user",
            "content": "The storyline was dull and uninspiring. ->"
        }
    ]
)

print(completion.choices[0].message)