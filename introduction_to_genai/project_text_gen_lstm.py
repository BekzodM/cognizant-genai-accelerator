text = open("told_by_an_idiot.txt", encoding='utf-8').read()
text = text.lower()  # Normalize case
text = text.replace('\n', ' ').replace('\r', '') 

chars = sorted(set(text))
char_to_idx = {c: i for i, c in enumerate(chars)}
idx_to_char = {i: c for i, c in enumerate(chars)}



