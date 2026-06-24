import os
import requests

# ## API END POINT WHERE REQUEST WILL BE SENT
Api_url="http://router.huggingface.co/v1/chat/completions"

# ## HEADERS CARRY THE REQUEST IDENTITY AND CONTENT TYPE THAT WILL BE RETURNED

headers={
    "authorization":f"Bearer {os.getenv('HF_TOKEN')}",
    'content_type':'application/json'
}

# LESS IMPORTANT PART CUSTOMISABLE
name=input("Enter the character you wanna talk to: ").title()

# THE FUNCTION DEFINITION THAT HOLDS THE PAYLOAD
def custom(message):
    #body of the engine is it's payload ESSENTIAL OR MOST IMP PART
    payload = {
    "model": "meta-llama/Meta-Llama-3-8B-Instruct",
    "messages": [
        {
            "role": "system",
"content": f"You are role‑playing as {name}. From now on, you must fully embody {name} — speak, think, and respond exactly as {name} would. Use {name}'s tone, personality, and worldview. Do not break character or mention that you are an AI. Avoid describing actions or stage directions; only produce dialogue. Stay consistent with {name}'s traits and knowledge, and interact naturally with the user as if you truly are {name}."
        },
        {
            "role": "user",
            "content": message
        }
    ],
    "max_tokens": 500
}
    #sents post req to huggingface api
    response=requests.post(Api_url,headers=headers,json=payload)
    # print("Status:", response.status_code)# FOR DEBUGGING
    # print("Raw:", response.text)# FOR DEBUGGING
    data=response.json() #IN CASE CONTENT TYPE FAILS JSONIFY AGAIN THE DATA RECEIVED
    if 'error' in data:
        return f"API Error: {data['error']}"
    
    if "choices" not in data:
        return f"API Error: {data}"

    return data["choices"][0]["message"]["content"]
    


#Body of the acctual working code
print(f"{name}: Hello HUMAN!!!  \n Note:\"Type 'bye' to exit.\"")
while True:
    user = input("You: ")

    if user.lower() == "bye" or 'bye' in user:
        print('Bye bro have fun!!🤖❤️😁')
        break

    reply = custom(user)

    print(f"{name}: ", reply)


