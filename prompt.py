def report_count(token):
    
    with open("corpus.txt") as f:
        text = f.readlines()
    count = 0

    for line in text:
        words = line.split()
    
        for word in words:
            if word == token:
                count += 1
    
    return count