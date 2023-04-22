from app import *

def get_response_of_text(prompt):

    prompt = f"""you are a helpful assistant, answer the following question: {prompt}"""

    answer = openai.Completion.create(
        prompt=prompt,
        temperature=1,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model=COMPLETIONS_MODEL
    )["choices"][0]["text"].strip(" \n")

    return answer

