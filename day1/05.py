import config
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": 
         """
            # Intermediate - 1
            Solve the following logic puzzle step-by-step:
            Three friends, Alice, Bob, and Carol, have different favorite colors: red, blue, and green. We know that:
            1. Alice does not like red.
            2. Bob does not like blue.
            3. Carol likes green.

            Determine the favorite color of each friend.

            Step-by-step solution:
            1. Carol likes green.
            2. Alice can like red or blue.
            3. Alice likes blue because she doesn't like red.
            4. That's why rice likes the color red.

            Answer:
            - Alice: blue
            - Bob: red
            - Carol: green

            # Intermediate - 2
            Solve the following logic puzzle step-by-step:
            Four people (A, B, C, D) are sitting in a row. We know that:
            1. A is not next to B.
            2. B is next to C.
            3. C is not next to D.

            Determine the possible seating arrangements.

            Step-by-step solution:
            1. B must be next to C, so possible pairs are BC or CB.
            2. C cannot be next to D, so D must be placed next to B or A.
            3. A cannot be next to B, so A must be placed away from B.
            4. Arrangements that satisfy all conditions: BCAD, CABD.

            Answer:
            - Possible arrangements: BCAD, CABD
         """
         },
        {
            "role": "user",
            "content": """
            # Simple 결과 확인
            Solve the following problem step-by-step: 345 + 678 - 123
            """
        }
    ]
)

print(completion.choices[0].message)