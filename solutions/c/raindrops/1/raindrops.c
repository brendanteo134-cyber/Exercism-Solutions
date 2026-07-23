#include "raindrops.h"
#include <stdio.h>
#include <string.h>
char *convert(char result[], int nr) {
    strcpy(result, "");
    if (nr % 3 == 0)
        strcat(result, "Pling");
    if (nr % 5 == 0)
        strcat(result, "Plang");
    if (nr % 7 == 0)
        strcat(result, "Plong");
    if (!strcmp(result, ""))
        sprintf(result, "%d", nr);
    return result;
}