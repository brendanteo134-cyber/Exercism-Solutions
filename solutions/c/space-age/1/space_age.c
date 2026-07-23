#include "space_age.h"
#define EARTH_YEAR 31557600
float age(planet_t planet, int64_t seconds){
    if (planet < 0 || planet > 8){
        return -1;
    }
    
    float year_length[] = {0.2408467, 0.61519726, 1, 1.8808158, 11.862615, 29.447498, 84.016846, 164.79132};
    return seconds / (year_length[planet] * EARTH_YEAR);
}
#ifndef SPACE_AGE_H
#define SPACE_AGE_H
#include <stdint.h>
typedef enum planet {
   MERCURY,
   VENUS,
   EARTH,
   MARS,
   JUPITER,
   SATURN,
   URANUS,
   NEPTUNE,
} planet_t;
float age(planet_t planet, int64_t seconds);
#endif
