def get_user_input():
    noun = input('Enter a noun: ') or 'dog'
    verb = input('Enter a verb: ') or 'walk'
    adjective = input('Enter an adjective: ') or 'blue'
    adverb = input('Enter an adverb: ') or 'quickly'
    return (noun, verb, adjective, adverb)

def display_output(noun, verb, adjective, adverb):
    print(f'Do you {verb} your {adjective} {noun} {adverb}? That\'s hilarious!')

(noun, verb, adjective, adverb) = get_user_input()
display_output(noun, verb, adjective, adverb)