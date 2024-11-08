from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tree import Tree

def nlp_information_extraction(text):
    words = word_tokenize(text)
    ne_tree = ne_chunk(pos_tag(words))
    entities = []
    for subtree in ne_tree:
        if isinstance(subtree, Tree):
            entity = " ".join(c[0] for c in subtree)
            entities.append((entity, subtree.label()))
    return entities