import requests

queries = [
    "What is the certificate about?",
    "Who completed the course?",
    "When was the certificate issued?"
]

for q in queries:

    response = requests.post(
        "http://127.0.0.1:8000/query",
        json={"query": q}
    )

    print("\nQuery:", q)
    print("Response:", response.json())