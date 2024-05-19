from flask import Flask, render_template
import requests
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)

def fetch_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from the API")
        return None

def compute_similarity(response, context, model):
    response_embedding = model.encode(response, convert_to_tensor=True)
    context_embedding = model.encode(context, convert_to_tensor=True)

    cosine_similarity = util.pytorch_cos_sim(response_embedding, context_embedding)
    return cosine_similarity.item()

def extract_citations(item, model):
    citations = []
    response = item.get("response", "")
    sources = item.get("source", [])
    for source in sources:
        context = source.get("context", "")
        similarity_score = compute_similarity(response, context, model)
        if similarity_score > 0.4:
            citations.append({"id": source["id"], "link": source["link"]})
        
    return citations

@app.route('/')
def index():
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    data = fetch_data_from_api(api_url)
    if data:
        data_list = data.get("data", {}).get("data", [])
        results = []
        
        # Initialize model once
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        
        for item in data_list:
            response = item.get("response", "")
            citations = extract_citations(item, model)
            results.append({"response": response, "citations": citations})
        return render_template('index.html', results=results)
    else:
        return "Failed to fetch data from the API"

if __name__ == '__main__':
    app.run(debug=True)
