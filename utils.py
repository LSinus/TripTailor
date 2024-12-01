import requests

def query_chatgpt(prompt, client):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a master travel planner."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=2000,
        temperature=0.4,
    )
    return response.choices[0].message.content

def query_chatgpt_for_images(prompt, client):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You must understand the most important place in a piece of text."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=2000,
        temperature=0.2,
    )
    return response.choices[0].message.content



def create_prompt(form_data):
    prompt = (
        "Give clear, structured, informations about trip, choose the most environmental friendly transportations and activities, divided by days, in every activity specify prices and follow the following informations"
        f"Place: {form_data['place']}\n"
        f"Period: {form_data['period']}\n"
        f"Duration: {form_data['duration']}\n"
        f"Number of people: {form_data['num_people']}\n"
        f"Price: {form_data['price']}\n"
        f"Interests: {form_data['interests']}\n"
        f"Other specifications: {form_data['others']}\n"
        "Don't be discursive (don't say anything like 'ok!, Certainly!' ecc...), create a point list with all the activities in each day\n"
        "Format in a table the result with columns for days, activities and budget, create different rows for different activities.\n"
        "Find at least two different ideas for this trip.\n"
        "Be rich in describe every activity for each day.\n"
        "If, and only if, restaurants are mentioned, search real existings restaurants.\n"
        "Try to propose eco friendly public transport and activities.\n"

    )
    return prompt
