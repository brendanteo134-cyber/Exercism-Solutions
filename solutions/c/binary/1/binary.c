#include "binary.h"
int convert(const char *input) {
    int res = 0;
    for (char* c=(char *) input; *c != '\0'; c++) {
        if (*c!='0' &&  *c!='1') return -1;
        res = res*2 + (*c == '0' ? 0 : 1);
    }
    return res;
}