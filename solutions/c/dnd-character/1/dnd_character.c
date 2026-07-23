#include "dnd_character.h"
#include <stdlib.h>
#include <math.h>
int ability(void) {
    int sum = 0;
    int minDice = 6;
    
    for (int i = 0; i < 4; i++) {
        int diceRoll = rand() % (6 + 1 -1) + 1;
        sum += diceRoll;
        if (diceRoll < 6) {
            minDice = diceRoll;
        }
    }
    sum -= minDice;
    return sum;
    
}
int modifier(int score) {
    return (int)floor((score - 10) / 2.0);
}
dnd_character_t make_dnd_character(void) {
    dnd_character_t player;
    player.strength = ability();
    player.dexterity = ability();
    player.intelligence = ability();
    player.wisdom = ability();
    player.charisma = ability();
    player.constitution = ability();
    player.hitpoints = 10 + modifier(player.constitution);
    return player;
}
