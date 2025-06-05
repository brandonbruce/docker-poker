from parameterized import parameterized
import unittest
from pokerhands import *

class TestPokerHands(unittest.TestCase):
    @parameterized.expand([
        (
            "Four Cards",
            [["Ac","7d","Qc","Jc"]],
            "Error: Hand does not include exactly 5 unique valid cards."
        ),
        (
            "Six Cards",
            [["Ac","7d","Qc","Jc","Tc","9d"]],
            "Error: Hand does not include exactly 5 unique valid cards."
        ),
        (
            "Empty",
            [],
            "No hands provided."
        ),
        (
            "Invalid Rank",
            [["1c","7d","Qc","Jc","Tc"]],
            "Error: Invalid cards were found."
        ),
        (
            "Invalid Suit",
            [["Ag","7d","Qc","Jc","9d"]],
            "Error: Invalid cards were found."
        ),
        (
            "Invalid Rank and Suit",
            [["1g","7d","Qc","Jc","9d"]],
            "Error: Invalid cards were found."
        ),
        (
            "Not a list",
            "Not a list",
            "Error: Invalid cards were found."
        ),
        (
            "List with non-list elements",
            [ ["Ac","7d","Qc","Jc","9d"],"Not a list"],
            "Error: Invalid cards were found."
        ),
        (
            "List with invalid list elements",
            [ ["Ac","7d","Qc","Tc","9d"],[1,2,3,4,5]],
            "Error: Invalid cards were found."
        ),
        (
            "List with empty elements",
            [ ["Ac","7d","Qc","Jc","Tc"],[]],
            "Error: Hand does not include exactly 5 unique valid cards."
        ),
        (
            "Card description too short",
            [ ["A","7d","Qc","Jc","Tc"]],
            "Error: Invalid cards were found."
        ),
        (
            "Card description too long",
            [ ["Ace","7d","Qc","Jc","Tc"]],
            "Error: Invalid cards were found."
        ),
    (
            "Duplicate within same hand",
            [ ["Ac","7d","Qc","Tc","Tc"],["Ad","7c","Ks","Jd","Ts"]],
            "Error: Duplicate cards were found."
        ),
        (
            "Duplicate between hands",
            [ ["Ac","7d","Qc","Jc","Tc"],["Ad","7c","Qc","Jd","Ts"]],
            "Error: Duplicate cards were found."
        ),
        (
            "Ace High Straight Flush",
            [["Ac","Kc","Qc","Jc","Tc"]],
            "Straight Flush  ['Ac', 'Kc', 'Qc', 'Jc', 'Tc']"
        ),
        (
            "King High Straight Flush",
            [["9c","Kc","Qc","Jc","Tc"]],
            "Straight Flush  ['Kc', 'Qc', 'Jc', 'Tc', '9c']"
        ),
        (
            "Ace Low Straight Flush",
            [["Ac","5c","4c","3c","2c"]],
            "Straight Flush  ['5c', '4c', '3c', '2c', 'Ac']"
        ),
        (
            "Four Of A Kind",
            [["Ac","Ah","Ad","As","Tc"]],
            "Four of a Kind  ['Ac', 'Ad', 'Ah', 'As', 'Tc']"
        ),
        (
            "Full House",
            [["Ac","Ad","Ah","Kc","Kd"]],
            "Full house  ['Ac', 'Ad', 'Ah', 'Kc', 'Kd']"
        ),
        (
            "Flush",
            [["Ac","Kc","Qc","Jc","5c"]],
            "Flush  ['Ac', 'Kc', 'Qc', 'Jc', '5c']"
        ),
        (
            "Ace High Straight",
            [["Ac","Kd","Qc","Jc","Tc"]],
            "Straight  ['Ac', 'Kd', 'Qc', 'Jc', 'Tc']"
        ),
    (
            "Ace Low Straight",
            [["Ac","2d","3c","4c","5c"]],
            "Straight  ['5c', '4c', '3c', '2d', 'Ac']"
        ),
        (
            "Three of a Kind",
            [["Ac","Ad","As","Jc","Tc"]],
            "Three of a Kind  ['Ac', 'Ad', 'As', 'Jc', 'Tc']"
        ),
        (
            "Two Pair",
            [["Ac","Ad","Qc","Qd","Tc"]],
            "Two Pair  ['Ac', 'Ad', 'Qc', 'Qd', 'Tc']"
        ),
        (
            "One Pair",
            [["Ac","Ad","Qc","Jc","Tc"]],
            "One Pair  ['Ac', 'Ad', 'Qc', 'Jc', 'Tc']"
        ),
        (
            "High Card",
            [["Ac","7d","Qc","Jc","Tc"]],
            "High Card  ['Ac', 'Qc', 'Jc', 'Tc', '7d']"
        ),
        (
            "Straight Flush Multiple",
            [
                ["Ac","Kc","Qc","Jc","Tc"],
                ["Kd","7s","Qs","Jd","5s"],
            ],
            "Straight Flush  ['Ac', 'Kc', 'Qc', 'Jc', 'Tc']"
        ),
        (
            "Full House Multiple",
            [
                ["Ac","Ad","Kc","Kd","Ks"],
                ["As","Ah","Qs","Qd","Qh"],
            ],
            "Full house  ['Ac', 'Ad', 'Kc', 'Kd', 'Ks']"
        ),
(
            "Pair Multiple",
            [
                ["Ac","Jd","Qc","8c","Jc"],
                ["Kd","Ks","Qs","Jh","5s"],
            ],
            "One Pair  ['Kd', 'Ks', 'Qs', 'Jd', '5s']"
        ),

        (
            "High Card Multiple",
            [
                ["Kc","7h","Qd","Js","6s"],
                ["Kd","7s","Qs","Jd","5s"],
            ],
            "High Card  ['Kc', 'Qd', 'Js', '7h', '6s']"
        ),
    (
            "High Card Multiple Tie",
            [
                ["Kc","7h","Qd","Js","Ts"],
                ["Kd","7s","Qs","Jd","Td"],
            ],
            "Tie [\"High Card  ['Kc', 'Qd', 'Js', 'Ts', '7h']\", \"High Card  ['Kd', 'Qs', 'Jd', 'Td', '7s']\"]"
        ),
    (
            "Ace High Card Multiple",
            [
                ["Kc","Ah","Qd","Js","6s"],
                ["Kd","As","Qs","Jd","5s"],
            ],
            "High Card  ['Ah', 'Kc', 'Qd', 'Js', '6s']"
        ),
        (
            "Ace High Card Multiple Tie",
            [
                ["Kc","Ah","Qd","Js","5s"],
                ["Kd","As","Qs","Jd","5d"],
            ],
            "Tie [\"High Card  ['Ah', 'Kc', 'Qd', 'Js', '5s']\", \"High Card  ['As', 'Kd', 'Qs', 'Jd', '5d']\"]"

        ),
        (
            "Ace High Card Multiple",
            [
                ["Kc","Ah","Qd","Js","6s"],
                ["Kd","As","Qs","Jd","5s"],
            ],
            "High Card  ['Ah', 'Kc', 'Qd', 'Js', '6s']"
        ),
    ])

    def test_hands(self,description,test_input,expected):
        self.assertEqual(evaluate_hands(test_input), expected )

if __name__ == "__main__":
    unittest.main()