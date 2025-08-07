import openai

# Set your API key
openai.api_key = 'YOUR_API_KEY'

def get_travel_advice(city_name):
    prompt = f"Here is the complete list of popular places to visit in {city_name}."

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful AI travel assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    advice = response.choices[0].message.content
    return advice

def main():
    city_name = input("Which city would you like to know the popular places to visit: ")
    advice = get_travel_advice(city_name)
    print(f"\n{advice}")

if __name__ == "__main__":
    main()
