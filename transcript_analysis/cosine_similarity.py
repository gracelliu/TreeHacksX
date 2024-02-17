from transformers import BertTokenizer, BertModel
import torch
from scipy.spatial.distance import cosine

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Example documents
documents = [
    "The benefits of regular exercise cannot be overstated. Exercise is not only good for physical health but also has numerous mental health benefits. From reducing stress and anxiety to improving mood and cognitive function, incorporating regular exercise into your routine can greatly enhance your overall well-being.",
    "Healthy eating habits are essential for maintaining a balanced lifestyle. By choosing nutritious foods and avoiding processed junk, you can fuel your body with the necessary nutrients it needs to thrive. From fruits and vegetables to lean proteins and whole grains, making smart food choices can lead to improved energy levels, better digestion, and overall better health.",
    "The history of ancient civilizations is a fascinating subject that continues to intrigue historians and archaeologists alike. Exploring the mysteries of ancient societies, from the majestic pyramids of Egypt to the intricate ruins of Machu Picchu, offers insights into human culture, technology, and societal structures that have shaped our world today."
]

# Tokenize and encode the documents
inputs_list = [tokenizer(doc, return_tensors='pt', truncation=True) for doc in documents]

# Get BERT embeddings for the documents
embeddings = []
with torch.no_grad():
    for inputs in inputs_list:
        outputs = model(**inputs)
        embedding = torch.mean(outputs.last_hidden_state, dim=1).numpy()
        embeddings.append(embedding.squeeze())

# Compute cosine similarity between document embeddings
similarities = []
for i in range(len(documents)):
      similarity = 1 - cosine(embeddings[0], embeddings[i])
      similarities.append((i, similarity))

# Print cosine similarity between each pair of documents
for i, sim in similarities:
    print(f"Cosine Similarity between Document {0} and Document {i}: {sim}")
