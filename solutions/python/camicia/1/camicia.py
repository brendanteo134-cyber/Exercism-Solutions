from collections import deque
from typing import Any
def transform(card: str) -> int:
    match card:
        case "J": return 1
        case "Q": return 2
        case "K": return 3
        case "A": return 4
        case _: return 0
def simulate_round(ab: list[deque[int]], turn: int) -> tuple[int, list[int]]: 
    pile = []
    due = 0
    while True:
        if not ab[turn]:
            return turn, pile
        card = ab[turn].popleft()
        pile.append(card)
        turn ^= 1
        if card > 0:
            due = card
            break
    while True:
        if not ab[turn]:
            return turn, pile
        card = ab[turn].popleft()
        pile.append(card)
        if card > 0:
            due = card
            turn ^= 1
            continue
        due -= 1
        if due == 0:
            return turn, pile
def simulate_game(player_a: list[str], player_b: list[str]) -> dict[str, Any]:
    ab = [deque(map(transform, player_a)), deque(map(transform, player_b))]
    seen = set()
    cards = 0
    tricks = 0
    status = "finished"
    turn = 0
    while all(ab):
        key = tuple(ab[0]), tuple(ab[1])
        if key in seen:
            status = "loop"
            break
        seen.add(key)
        turn, pile = simulate_round(ab, turn)
        cards += len(pile)
        turn ^= 1
        ab[turn].extend(pile)
        tricks += 1
    return {"status": status, "cards": cards, "tricks": tricks}