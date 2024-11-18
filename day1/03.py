import config
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": 
         """
            Convert the following natural language requests into SQL queries:
            1. "Please select employees whose salary is over 5000": SELECT * FROM employees WHERE salary > 50000;
            2. "Give me a list of out of stock products": SELECT * FROM products WHERE stock = 0;
            3. "Pick the names of students who scored over 90 points in math.": SELECT name FROM students WHERE math_score > 90;
            4. "Please select a list of orders with an order date within 30 days.": SELECT * FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
            5. "Group your customers by city and tell us the city and its number": SELECT city, COUNT(*) FROM customers GROUP BY city;
         """
         },
        {
            "role": "user",
            "content": """
            Request: "Find the average salary of employees in the marketing department."
            SQL Query:"""
        }
    ]
)

print(completion.choices[0].message)