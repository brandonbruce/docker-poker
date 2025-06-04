from collections import defaultdict

def evaluate_hands(hands):
    """
    Evaluate a list of poker hands and return the strongest hand.

    Args:
    hands (list): A list of lists, where each sublist contains 5 card strings.

    Returns:
    str: A string containing the name of the strongest hand and its cards.
    """
    if not hands:
        return "No hands provided."
    if are_invalid(hands):
        return "Error: Invalid cards were found."
    if are_dupes(hands):
        return "Error: Duplicate cards were found."

    strongest_hand = None
    strongest_hand_name = None
    hand_names = []
    winning_ranks = []

    sorted_hands = sort_hands(hands)

    for hand in sorted_hands:
        
        ranks = [get_card_rank(card[0]) for card in hand]
        result = evaluate_hand(hand)
        #Creates a list of the hand name, the ranks of the cards, and the result to print out
        current_result = []
        current_result.append(result.split("  ")[0])
        current_result.append(ranks)
        current_result.append(result)
        hand_names.append(current_result)

        if result.startswith("Error: "):
            return result
        
        hand_name, hand_cards = result.split("  ")
        hand_cards = hand_cards.strip("[]").replace('"', '').split(",")
        hand_cards = [card.strip() for card in hand_cards]

        if strongest_hand is None or get_hand_ranking(hand_name) < get_hand_ranking(strongest_hand_name):
            strongest_hand = hand_cards
            strongest_hand_name = hand_name
    #create a new list of just the hands that have the strongest hand name
    for currentResult in hand_names:
        if(strongest_hand_name in currentResult[0]):
            winning_ranks.append(currentResult)
    return tiebreaker(winning_ranks)

def tiebreaker(hands):
    winning_hand = hands[0][0]
    winners = []
    for i in range(5):
        values = [hand[1][i] for hand in hands]
        lowest = min(values)
        for index,hand in enumerate(hands):
            currentValue = hand[1][i]
            if(currentValue != lowest):
                hand[0] = "Lost"
    for hand in hands:
        if(hand[0] == winning_hand):
            winners.append(hand[2])
    if(len(winners) > 1):
        return f"Tie {winners}"
    else:
        return f"{hands[0][2]}"

def sort_hand(hand):
    sorted_hand = sorted(hand, key=lambda x: (x[1]))
    sorted_hand = sorted(sorted_hand, key=lambda x: (get_card_rank(x[0])))
    return sorted_hand

def sort_hands(hands):
    sorted_hands = []
    for hand in hands:
        sorted_hands.append(sort_hand(hand))
    return sorted_hands

def are_invalid(hands):
    allcards = [];
    for hand in hands:
        allcards.extend(hand)
    for card in allcards:
        if(len(str(card)) != 2):
            return True
        if(not set(card[0]).issubset("AKQJT98765432")):
            return True
        if(not set(card[1]).issubset("cshd")):
            return True
    return False

def are_dupes(hands):
    allcards = [];
    for hand in hands:
        allcards.extend(hand)
    if(len(allcards) != len(set(allcards))):
        return True
    return False

def evaluate_hand(cards):
    """
    Evaluate a poker hand.

    Args:
    cards (list): A list of 5 card strings.

    Returns:
    str: A string containing the name of the hand and its cards, or an error message.
    """
    
    if len(cards) != 5 or len(set(cards)) != 5:
        return "Error: Hand does not include exactly 5 unique valid cards."

    # Parse cards
    ranks = [card[0] for card in cards]
    suits = [card[1] for card in cards]

    # Check hand type
    is_flush = len(set(suits)) == 1
    is_straight = is_straight_hand(ranks)
    is_ace_low_straight = is_ace_low_straight_hand(ranks)

    if is_ace_low_straight:
        is_straight = True
        ace_card = cards.pop(0)
        cards.append(ace_card)

    if is_straight and is_flush:
        return f"Straight Flush  {cards}"
    elif is_four_of_a_kind(ranks):
        return f"Four of a Kind  {cards}"
    elif is_full_house(ranks):
        return f"Full house  {cards}"
    elif is_flush:
        return f"Flush  {cards}"
    elif is_straight:
        return f"Straight  {cards}"
    elif is_three_of_a_kind(ranks):
        return f"Three of a Kind  {cards}"
    elif is_two_pair(ranks):
        return f"Two Pair  {cards}"
    elif is_one_pair(ranks):
        return f"One Pair  {cards}"
    else:
        return f"High Card  {cards}"

def get_card_rank(rank):
    """
    Get the rank of a card.

    Args:
    rank (str): The rank of the card.

    Returns:
    int: The rank of the card.
    """
    rank_order = "AKQJT98765432"
    return rank_order.index(rank)

def get_hand_ranking(hand_name):
    """
    Get the ranking of a hand.

    Args:
    hand_name (str): The name of the hand.

    Returns:
    int: The ranking of the hand.
    """
    hand_rankings = [
        "Straight Flush",
        "Four of a Kind",
        "Full house",
        "Flush",
        "Straight",
        "Three of a Kind",
        "Two Pair",
        "One Pair",
        "High Card"
    ]
    return hand_rankings.index(hand_name)

def is_straight_hand(ranks):
    """
    Check if a hand is a straight.

    Args:
    ranks (list): A list of card ranks.

    Returns:
    bool: True if the hand is a straight, False otherwise.
    """
    rank_order = "AKQJT98765432"
    rank_values = [rank_order.index(rank) for rank in ranks]
    rank_values.sort()
    return rank_values == list(range(min(rank_values), max(rank_values) + 1))

def is_ace_low_straight_hand(ranks):
    """
    Check if a hand is an ace low straight.

    Args:
    ranks (list): A list of card ranks.

    Returns:
    bool: True if the hand is a straight, False otherwise.
    """
    if("A" not in ranks):
        return False
    rank_order = "KQJT98765432A"
    rank_values = [rank_order.index(rank) for rank in ranks]
    rank_values.sort()
    return rank_values == list(range(min(rank_values), max(rank_values) + 1))

def is_four_of_a_kind(ranks):
    """
    Check if a hand is four of a kind.

    Args:
    ranks (list): A list of card ranks.

    Returns:
    bool: True if the hand is four of a kind, False otherwise.
    """
    rank_counts = defaultdict(int)
    for rank in ranks:
        rank_counts[rank] += 1
    return 4 in rank_counts.values()

def is_full_house(ranks):
    """
    Check if a hand is a full house.

    Args:
    ranks (list): A list of card ranks.

    Returns:
    bool: True if the hand is a full house, False otherwise.
    """
    rank_counts = defaultdict(int)
    for rank in ranks:
        rank_counts[rank] += 1
    return sorted(rank_counts.values()) == [2, 3]

def is_three_of_a_kind(ranks):
    """
    Check if a hand is three of a kind.

    Args:
    ranks (list): A list of card ranks.

    Returns:
    bool: True if the hand is three of a kind, False otherwise.
    """
    rank_counts = defaultdict(int)
    for rank in ranks:
        rank_counts[rank] += 1
    return 3 in rank_counts.values()

def is_two_pair(ranks):
    """
    Check if a hand is two pair.

    Args:
    ranks (list): A list of card ranks.

    Returns:
    bool: True if the hand is two pair, False otherwise.
    """
    rank_counts = defaultdict(int)
    for rank in ranks:
        rank_counts[rank] += 1
    pair_count = sum(1 for count in rank_counts.values() if count == 2)
    return pair_count == 2

def is_one_pair(ranks):
    """
    Check if a hand is one pair.

    Args:
    ranks (list): A list of card ranks.

    Returns:
    bool: True if the hand is one pair, False otherwise.
    """
    rank_counts = defaultdict(int)
    for rank in ranks:
        rank_counts[rank] += 1
    return 2 in rank_counts.values()

# Example usage:
if __name__ == "__main__":
    hands = [
        ["Ac","Kc","Qc","Jc","Td"],
        ["Ks","Qs","Js","Ts","9s"]
    ]
    print(evaluate_hands(hands))
