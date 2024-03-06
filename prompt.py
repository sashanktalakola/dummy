def report_count(token):
    text = open("corpus.txt")
    split_text = text.split()
    count = 0
    for word in split_text:
        if word == token:
            count += 1
    
    return count