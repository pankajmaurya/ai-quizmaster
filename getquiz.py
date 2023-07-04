from initopenai import openai

prompt="""
Generate a quiz of 10 questions based on the book 'Java 8 in action' in the following format

{ "quiz": [{"question" : "What is the main benefit of using the CompletableFuture class in Java 8 for asynchronous programming?" , "options": {"a": "It allows you to create and manage threads directly.", "b": " It enables you to define complex synchronous operations.", "c": "It provides a clean and easy-to-use API for managing asynchronous computations.", "d": "It allows you to perform parallel processing without using streams."}, "answer": "c"}]}
"""

def get_new_quiz(model="gpt-3.5-turbo"):
    messages = [
        {"role": "system", "content":
            "Your are an AI assistant tutor for teaching. You will generate the response in a json as described in the format requested."},
        {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

