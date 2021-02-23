rules = [('?*X HELLO ?*Y', ['How do you do. Please state your problem.'
         ]), ('?*X COMPUTER ?*Y', ['Do computers worry you?',
         'What do you think about machines?',
         'Why do you mention computers?',
         'What do you think machines have to do with your problem?']),
         ('?*X NAME IS ?*Y', ['I am not interested in names',
         'what do you do ?Y']), ('?*X NEED ?*Y', ['What if ?X get ?Y',
         'why ?X need ?Y'])]

default_responses = ['Very interesting',
                     'I am not sure I understand you fully',
                     'Please continue']
import random
from patternmatching import match_pattern

def replace(word, replacements):
    for (old, new) in replacements:
        if word == old:
            return new
    return word


def switch_viewpoint(words):
    replacements = [
        ('I', 'YOU'),
        ('YOU', 'I'),
        ('ME', 'YOU'),
        ('MY', 'YOUR'),
        ('AM', 'ARE'),
        ('ARE', 'AM'),
        ]
    return [replace(word, replacements) for word in words]


def respond(rules, input, default_responses):
    input = input.split()  # match_pattern expects a list of tokens
    matching_rules = []
    for (pattern, responses) in rules:
        pattern = pattern.split()
    bindings = match_pattern(pattern, input)
    if bindings:
        matching_rules.append((responses, bindings))
    if matching_rules:
        (responses, bindings) = random.choice(matching_rules)
        response = random.choice(responses)
    else:
        bindings = {}
        response = default_responses[0]
    for (variable, value) in bindings.items():
        value = ' '.join(switch_viewpoint(value))
        if value:
            response = response.replace('?' + variable, value)
        return response


def Eliza(prompt, rules, default_responses):
    while True:
        try:
            userinput = input(prompt).upper()
            if not userinput:
                continue
        except:
            break
        print(respond(rules, userinput, default_responses))

Eliza('Eliza> ', rules, default_responses)