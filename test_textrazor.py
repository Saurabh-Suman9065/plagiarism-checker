import textrazor

# Set the correct API key
textrazor.api_key = "e2ea95cc09a2cacde98ca832582949935b21c5f5f1f65a3efb4971a1"  # Replace with your actual API key

# Initialize the TextRazor client
client = textrazor.TextRazor(extractors=["entities", "topics"])

# Sample input text
input_text = "TextRazor is an API that allows natural language processing and text analysis."

# Make a simple API call
response = client.analyze(input_text)

# Check if we received a valid response
if response:
    print("Entities:")
    for entity in response.entities():
        print(entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types)
    
    print("\nTopics:")
    for topic in response.topics():
        print(topic.label, topic.score)
else:
    print("No response from TextRazor API.")
