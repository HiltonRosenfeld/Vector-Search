import openai

from config import getSettings


# load settings adn keys
settings = getSettings()

# define openai Key
openai.api_key = settings.OPENAI_API_KEY

# define the embedding model
model_id = "text-embedding-ada-002"

# Use the embeddings
customer_input = "What equipement would you recommend for a computer workstation setup costing less than $2000?"
embedding = openai.Embedding.create(input=customer_input, model=model_id)['data'][0]['embedding']
print(embedding)

