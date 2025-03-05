from openai import OpenAI
import random

with open('irp.txt', 'r') as file:
    premise = file.read().strip()

message_history = [{
                "role": "system", 
                "content": [{"type": "text", "text":\
                             premise}]
            }]

first_time = 0
def chatbot(message, first=[0]):
    client = OpenAI()
    global first_time
    if (first_time == 0):
        message = {
                "role": "system", 
                "content": [{"type": "text", "text":\
                             premise}]}
        #print statement one
        print("This is the first time\n")
        print()
        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[message]
    )
        first_response = {"role": "assistant",
                "content": [{"type":"text", "text":completion.choices[0].message.content}]}
        #print statement two
        print("This is the first response\n")
        print(first_response)
        print()
        message_history.append(first_response)
        first_time+=1
        
    else:
        classification = classify_input(message)
        print("This is the return from classify input ")
        print(classification)
        print()
        history = generate_response()

        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=history 
        
    )

    
    new_item = {"role": "assistant",
                "content": [{"type":"text", "text":completion.choices[0].message.content}]
            }
    print("This is the new item after generating a response from the assistant\n")
    print(new_item)
    print()
    message_history.append(new_item)

    return completion.choices[0].message.content


def classify_input(message):
    client = OpenAI()
    
    classify_history = message_history.copy()

    content = "From: Tahani\n Strategy:<fill in>\n Message:" + message

    new_item = {
                "role": "user",
                "content": [{"type": "text", "text":content}]
            }
    print("This is inside classify input\n")
    print(new_item)
    print()
    classify_history.append(new_item)

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=classify_history
    )
    complete_item = {
            "role": "user",
            "content": [{"type": "text", "text":completion.choices[0].message.content}]
        }
    print("This is inside classify input but the completed item from the assistant\n")
    print(complete_item)
    print()
    message_history.append(complete_item)

    return completion.choices[0].message.content


def generate_response():
    strategies = [ "Interests", "Proposal", "Positive Expectations", "Rights", "Power", "Facts"]
    random.shuffle(strategies)
    strategy = random.choice(strategies)
    print(strategy + "\n")
    content = "From: Eleanor\n Cooperativeness:<fill in>\n Strategy:" + strategy + "\nMessage: <fill in>"

    to_generate = {

        "role": "user",
        "content": [{"type":"text", "text":content}]
    }
    print("inside generate response\n")
    print(to_generate)
    print()
    history = message_history.copy()
    history.append(to_generate)

    print(message_history)
    
    return history




