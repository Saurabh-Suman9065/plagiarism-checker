import os
import textrazor
from flask import Flask, request, jsonify, render_template

TEXT_RAZOR_API_KEY = os.getenv('TEXT_RAZOR_API_KEY')
if not TEXT_RAZOR_API_KEY:
    raise ValueError("TextRazor API Key is not set in environment variables.")

app = Flask(__name__)

textrazor.api_key = TEXT_RAZOR_API_KEY
client = textrazor.TextRazor(extractors=["entities", "topics"])

def check_plagiarism(input_text):
    try:
        response = client.analyze(input_text)

        sources = []  # To store matched URLs
        for entity in response.entities():
            if hasattr(entity, 'wikipedia_link') and entity.wikipedia_link:
                sources.append(entity.wikipedia_link)
            elif hasattr(entity, 'freebase_types') and entity.freebase_types:
                sources.extend(entity.freebase_types)

        # Ensure no duplicate URLs are returned
        unique_sources = list(set(sources))

        return {"matched_urls": unique_sources}

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
