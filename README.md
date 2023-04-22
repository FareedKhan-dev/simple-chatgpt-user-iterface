# A Simple GPT-3 Chatbot

Created a Flask application that uses the GPT API to build a chatbot. The chatbot can generate responses based on user input using the GPT language model.

<img src="https://img.shields.io/badge/python-3.9.0-blue.svg"> <img src="https://img.shields.io/badge/license-MIT-blue.svg">

## Demo

<img src="https://miro.medium.com/v2/resize:fit:828/0*omM9OlgMz49vCBOe.gif" width=600px>

## How to use it

```bash
git clone https://github.com/FareedKhan-dev/simple-chatgpt-user-iterface.git
```

Go to the project directory

```bash
cd simple-chatgpt-user-iterface
```

Install dependencies

```bash
pip install -r requirements.txt
```

Enter your OpenAI API key within `app.py`

```bash
...

# insert your key here
openai.api_key = ''

...
```

If you dont have `api` key, and want to test the frontend, you can replace the `get_response_of_text` function code in `aiapi.py` file.

FROM

```bash
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
```
TO

```bash
from app import *

def get_response_of_text(prompt):

  import time
  time.sleep(3)
  return 'this is a sample text generated because you dont provide an OpenAI API key to generate response.'
```

you can run the app using

```bash
python app.py
