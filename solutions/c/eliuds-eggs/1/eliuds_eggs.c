#include "eliuds_eggs.h"
int egg_count(unsigned int value)
{
    unsigned int count=0;
    while (value>0)
    {
        if(value & 1)
        {
            count++;
        }
        value>>=1;
    }
    return count;
}