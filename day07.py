FILENAME = 'data/day07.txt'

class hand:
  def __init__(self, cards, bid):
    self.cards = cards
    self.bid = bid
  
  def getType(self, jokerWild=False):
    labels = {
      '2': 0,
      '3': 0,
      '4': 0,
      '5': 0,
      '6': 0,
      '7': 0,
      '8': 0,
      '9': 0,
      'T': 0,
      'J': 0,
      'Q': 0,
      'K': 0,
      'A': 0,
    }

    for card in self.cards:
      labels[card] += 1

    if jokerWild:
      jokers = labels['J']
      labels['J'] = 0
      maxKey = max(labels, key=labels.get)
      labels[maxKey] += jokers

    maxValue = max(labels.values())

    type = ''
    if maxValue == 1:
      type = 'high'
    elif maxValue == 2:
      pairs = sum(value == 2 for value in labels.values())
      if pairs > 1:
        type = 'twoPair'
      else:
        type = 'onePair'
    elif maxValue == 3:
      if 2 in labels.values():
        type = 'full'
      else:
        type = 'three'
    elif maxValue == 4:
      type = 'four'
    else:
      type = 'five'

    return type
  
  def winnings(self, rank):
    return self.bid * rank
  
  def __str__(self) -> str:
    return f'{self.cards} {self.bid}'

def sortHands(hand):
  cardRanks = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
  }
  return tuple(cardRanks[card] for card in hand.cards)

def sortWildHand(hand):
  cardRanks = {
    'J': 0,      
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'Q': 10,
    'K': 11,
    'A': 12,
  }
  return tuple(cardRanks[card] for card in hand.cards)

hands = []
with open(FILENAME) as f:
  for line in f:
    cards, bid = line.split()
    hands.append(hand(cards, int(bid)))


# Part 1
sortedHands = sorted(hands, key=sortHands)

rankedHands = {
  'high': [],
  'onePair': [],
  'twoPair': [],
  'three': [],
  'full': [],
  'four': [],  
  'five': []
}

for currentHand in sortedHands:
  type = currentHand.getType()
  rankedHands[type].append(currentHand.bid)

currentRank = 1
winnings = 0
for currentType in rankedHands.values():
  for currentHand in currentType:
    winnings += currentHand * currentRank
    currentRank += 1

print(f'Part 1: {winnings}')


# Part 2
for typeList in rankedHands.values():
  typeList.clear()

sortedHands = sorted(hands, key=sortWildHand)

for currentHand in sortedHands:
  type = currentHand.getType(jokerWild=True)
  rankedHands[type].append(currentHand.bid)

currentRank = 1
winnings = 0
for currentType in rankedHands.values():
  for currentHand in currentType:
    winnings += currentHand * currentRank
    currentRank += 1

print(f'Part 2: {winnings}')