import requests

API_KEY = "AIzaSyCjugXskX23_lCEesAa7AZMCHHns6kDT1w"
SEARCH_ENGINE_ID = "041d5b819619848fd"

def google_search(query, api_key='AIzaSyCjugXskX23_lCEesAa7AZMCHHns6kDT1w', cse_id='041d5b819619848fd'):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id,
    }
    response = requests.get(url, params=params)
    results = response.json()

    if "items" not in results:
        return "Sorry, no results were found."

    answer = ""
    for item in results["items"][:3]:  
        answer += f"Title: {item['title']}\n"
        answer += f"Snippet: {item['snippet']}\n"
        answer += f"Link: {item['link']}\n\n"
    return answer.strip()

def chatbot():
    print("Ask me anything (type 'exit' to quit):")
    while True:
        question = input("You: ").strip()
        if question.lower() == "exit":
            print("Bot: Goodbye!")
            break
        answer = google_search(question)
        print("Bot:\n" + answer)

if __name__ == "__main__":
    chatbot()
