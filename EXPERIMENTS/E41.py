import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

KNOWLEDGE_BASE = [
    ("What is artificial intelligence?", "Artificial intelligence is the simulation of human intelligence by computer systems."),
    ("What is machine learning?", "Machine learning is a subset of AI where models learn patterns from data without explicit programming."),
    ("What is deep learning?", "Deep learning uses multi-layer neural networks to model complex patterns in data like images and text."),
    ("What is natural language processing?", "Natural language processing helps computers understand, interpret, and generate human language."),
    ("Hello", "Hi there! Ask me a question about AI, machine learning, or NLP."),
    ("Bye", "Goodbye! Good luck with your experiments."),
]


def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()


class NLPChatbot:
    def __init__(self, qa_pairs):
        self.questions = [q for q, _ in qa_pairs]
        self.answers = [a for _, a in qa_pairs]
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform([preprocess(q) for q in self.questions])

    def reply(self, user_input: str, threshold: float = 0.25) -> str:
        processed = preprocess(user_input)
        if not processed:
            return "Please type a valid message."
        query_vec = self.vectorizer.transform([processed])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix)[0]
        best_idx = int(similarities.argmax())
        if similarities[best_idx] < threshold:
            return "I'm not sure about that yet. Try asking about AI, machine learning, deep learning, or NLP."
        return self.answers[best_idx]


if __name__ == "__main__":
    bot = NLPChatbot(KNOWLEDGE_BASE)
    sample_queries = ["hello", "explain machine learning", "what is nlp?", "bye"]
    for q in sample_queries:
        print(f"You: {q}")
        print(f"Bot: {bot.reply(q)}\n")

    # Uncomment below for interactive chat in terminal:
    # while True:
    #     msg = input("You: ").strip()
    #     if msg.lower() in {"exit", "quit"}:
    #         break
    #     print("Bot:", bot.reply(msg))