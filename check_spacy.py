import spacy

# Verifica a versão spaCy
print(spacy.__version__)

# Carrega o modelo em português
try:
    nlp = spacy.load("pt_core_news_sm")
    print("O modelo 'pt_core_news_sm' está disponível.")
except OSError:
    print("O modelo 'pt_core_news_sm' não foi encontrado. Você pode precisar baixar o modelo primeiro.")