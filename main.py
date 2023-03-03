# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# -- coding: utf-8 --
import openai

openai.api_key = "your key"


def chatgpt():
    messages = []
    while True:
        input_ = input("please input your questions: ")
        messages.append({"role": "user", "content": input_})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = response['choices'][0]['message']['content'].encode('utf-8').decode('utf-8')
        messages.append({"role": response['choices'][0]['message']['role'], "content": answer})

        print(answer)

chatgpt()