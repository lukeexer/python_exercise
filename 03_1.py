def get_user_input():
    quote = input('What is the quote?') or 'These aren\'t the droids you\'re looking for.'
    author = input('Who said it?') or 'Luke'
    return (quote, author)

def show_result(quote, author):
    print(author + ' says, "' + quote + '"')

(quote, author) = get_user_input()
show_result(quote, author)