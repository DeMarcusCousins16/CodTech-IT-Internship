from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, sentence_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

if __name__ == "__main__":
    sample_text = """
    Natural Language Processing (NLP) is a sub-field of artificial intelligence that focuses on enabling computers to understand and process human languages. Applications of NLP include text summarization, translation, sentiment analysis, and more. Summarization is particularly useful for condensing long articles into short, informative paragraphs.
    """
    summary = summarize_text(sample_text)
    print("Original Text:\n", sample_text)
    print("\nSummary:\n", summary)