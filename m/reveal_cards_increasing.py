class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        shuffle = []

        while len(deck):
            shuffle.insert(0, deck.pop())
            shuffle.insert(0, shuffle.pop())

        shuffle.append(shuffle.pop(0))
        return shuffle

        #48ms, 74.66%
