import os
import textrazor
from flask import Flask, request, jsonify, render_template

# Fetch TextRazor API key securely from environment variables
TEXT_RAZOR_API_KEY =('Te2ea95cc09a2cacde98ca832582949935b21c5f5f1f65a3efb4971a1')

# Initialize Flask app
app = Flask(__name__)

# Initialize TextRazor client
textrazor.api_key = TEXT_RAZOR_API_KEY
client = textrazor.TextRazor(extractors=["entities", "topics"])

# Function to check plagiarism using TextRazor API
def check_plagiarism(input_text):
    try:
        response = client.analyze(input_text)

        entities = []
        topics = []

        # Extract entities and topics from the response
        for entity in response.entities():
            entities.append({
                "id": entity.id,
                "relevance_score": entity.relevance_score,
                "confidence_score": entity.confidence_score,
                "freebase_types": entity.freebase_types
            })

        for topic in response.topics():
            topics.append({
                "label": topic.label,
                "score": topic.score
            })

        return {"entities": entities, "topics": topics}

    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-plagiarism', methods=['POST'])
def plagiarism_check():
    data = request.get_json()
    input_text = data['text']

    result = check_plagiarism(input_text)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
