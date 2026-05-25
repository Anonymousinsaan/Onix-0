import re

class SemanticNormalizer:
    """
    Linguistic Tokenizer & Semantic Intent Processor.
    Implements basic Porter Stemming heuristics and Synset mapping.
    """
    def __init__(self):
        # Basic Synset Mapping for Intent Distillation
        self.synsets = {
            "query": ["ask", "question", "search", "find", "what", "how"],
            "action": ["do", "run", "execute", "start", "perform"],
            "stop": ["halt", "quit", "end", "terminate", "cease"]
        }

    def tokenize(self, text):
        """Simple regex-based tokenizer."""
        return re.findall(r'\b\w+\b', text.lower())

    def stem(self, word):
        """Minimalist Porter Stemmer heuristic for 'ing', 'ed', 'es', 's'."""
        if word.endswith('ing'):
            return word[:-3]
        if word.endswith('ed'):
            return word[:-2]
        if word.endswith('es'):
            return word[:-2]
        if word.endswith('s') and not word.endswith('ss'):
            return word[:-1]
        return word

    def distill_intent(self, text):
        """Maps tokens to known semantic intents."""
        tokens = self.tokenize(text)
        stems = [self.stem(t) for t in tokens]

        intents = []
        for stem in stems:
            for intent, keywords in self.synsets.items():
                if stem in keywords:
                    intents.append(intent)

        return list(set(intents)) if intents else ["unknown"]

if __name__ == "__main__":
    normalizer = SemanticNormalizer()
    sample_text = "Running a query for searching data."
    print(f"Text: {sample_text}")
    print(f"Intents: {normalizer.distill_intent(sample_text)}")
