import config
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": 
         """
            # Simple - 1
            Solve the following problem step-by-step: 23 + 47

            Step-by-step solution:
            1. Divide 23 by 20 + 3
            2. Divide 47 by 40 + 7
            3. Add 20 and 40, then add 3 and 7.
            4. Find the sum of two numbers.

            Answer: 70

            # Simple - 2
            Solve the following problem step-by-step: 123 - 58

            Step-by-step solution:
            1. Let's make subtraction simple by matching the last digits of two numbers.
            2. Divide 123 by 128 - 5
            3. Subtract 58 from 128
            4. Subtract 5 from the result.

            Answer: 65
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