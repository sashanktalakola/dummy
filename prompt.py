def report_count(token, case_sensitive=False):
    if len(token.split()) > 1:
        raise MoreThanOneToken(f"Expected 1 token, given {len(token.split())} tokens")
    with open("corpus.txt") as f:
        text = f.readlines()
    count = 0

    for line in text:
        words = line.split()
    
        for word in words:
            if not case_sensitive:
                if word.lower() == token.lower():
                    count += 1
            else:
                if word == token:
                    count += 1
    
    return count

class MoreThanOneToken(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)