blackjack-ai/chromosome.md


chromosome structure: 10 [possible dealer up cards] x 34 (16 + 8 + 10) [hard hands + soft hands + pairs]

--

'T' is Jack, Queen, or King 

'A' is Ace

'A' followed '-' indicates an Ace paired with it's corresponding number card, these hands are specifically marked since the Ace card can either count as 11 or 1 points.

'D' indicates doubles of the corresponding after the '-'

possible dealer upcards: [2, 3, 4, 5, 6, 7. 8, 9, T, A]

possible hands: [5, 6, 7. 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, A-2, A-3, A-4, A-5, A-6, A-7. A-8, A-9, D-2, D-3, D-4, D-5, D-6, D-7. D-8, D-9, D-T, D-A] 

--

Subsets of Possible Hands:

possible hard hands: [5, 6, 7. 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

possible soft hands: [A-2, A-3, A-4, A-5, A-6, A-7. A-8, A-9]

possible pairs: [D-2, D-3, D-4, D-5, D-6, D-7. D-8, D-9, D-T, D-A]

--


340 total cells

4 possible options for cells: 
- S for stand
- H for hit
- P for split (only possible for pairs)
- D for double down 
