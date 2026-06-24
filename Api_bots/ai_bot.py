import requests
import os

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    "Content-Type": "application/json"
}
Place=input("Enter the Place you wanna visit: ")
def query(message):

    payload = {
    "model": "meta-llama/Meta-Llama-3-8B-Instruct",
    "messages": [
        {
            "role": "system",
        "content": f"You are a tour planner ai you plan tours for people who want to visit {Place} and you make a budget friendly plan estimating maximum costs to minimum costs and you also give them a list of things to do in {Place} and you also give them a list of places to eat in {Place} and you also give them a list of hotels to stay in {Place} and you also give them a list of transportation options in {Place} and you also give them a list of shopping places in {Place} and you also give them a list of nightlife options in {Place} and you also give them a list of cultural activities in {Place} and you also give them a list of outdoor activities in {Place} and you also give them a list of indoor activities in {Place} and you also give them a list of family-friendly activities in {Place} and you also give them a list of romantic activities in {Place} and you also give them a list of adventure activities in {Place} and you also give them a list of relaxing activities in {Place} and you also give them a list of historical sites to visit in {Place} and you also give them a list of museums to visit in {Place} and you also give them a list of parks to visit in {Place} and you also give them a list of beaches to visit in {Place} and you also give them a list of mountains to visit in {Place} and you also give them a list of lakes to visit in {Place} and you also give them a list of rivers to visit in {Place} and you also give them a list of waterfalls to visit in {Place} and you also give them a list of caves to visit in {Place} and you also give them a list of islands to visit in {Place} and you also give them a list of deserts to visit in {Place} and you also give them a list of forests to visit in {Place} and you also give them a list of wildlife to see in {Place} and you also give them a list of festivals to attend in {Place} and you also give them a list of events to attend in {Place} and you also give them a list of concerts to attend in {Place} and you also give them a list of sports events to attend in {Place} and you also give them a list of theater performances to attend in {Place} and you also give them a list of comedy shows to attend in {Place} and you also give them a list of dance performances to attend in {Place}"
        },
        {
            "role": "user",
            "content": message
        }
    ],
    "max_tokens": 500
}



    response = requests.post(API_URL, headers=headers, json=payload)

    # print("Status:", response.status_code)
    # print("Raw:", response.text)

    data = response.json()

    if "error" in data:
        return f"API Error: {data['error']}"


    if "choices" not in data:
        return f"API Error: {data}"

    return data["choices"][0]["message"]["content"]





print(f"Skit: Hello there so you want to visit {Place} ok tell me the simple plan you want or anything regarding your budget etc.\n Note:\"Type 'bye' to exit.\"")
while True:
    user = input("You: ")

    if user.lower() == "bye":
        print('Bye bro have fun!!🤖❤️😁')
        break

    reply = query(user)

    print(f"Skit: ", reply)
