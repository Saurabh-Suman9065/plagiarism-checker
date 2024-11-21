import textrazor

# Replace with your actual API key
textrazor.api_key = "e2ea95cc09a2cacde98ca832582949935b21c5f5f1f65a3efb4971a1"

client = textrazor.TextRazor(extractors=["entities", "topics"])

# Test with a sample URL or plain text
response = client.analyze("TextRazor is a great service for natural language processing and text analysis.")

# Print the extracted entities and topics
print("Entities:")
for entity in response.entities():
    print(entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types)

print("\nTopics:")
for topic in response.topics():
    print(topic.label, topic.score)
