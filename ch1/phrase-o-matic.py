from random import random


import random

verbs = ['Leverage', 'Sync', 'Target', 'Gamify', 'Offline',
         'Crowd-sourced', '24/7', 'Lean-in', '30,000 foot']

adjectives = ['A/B Tested', 'Freemium', 'Hyperlocal',
              "Siload", 'B-to-B', 'Oriented', 'Cloud-bases', 'API-based']

nouns = ['Early Adopter', 'Low-handing fruit', 'pipeline',
         'Splash Page', 'Productivity', 'Process', 'Tipping Point', 'paradigm']

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

phrase = verb + ' ' + adjective + ' ' + noun

print(phrase)
