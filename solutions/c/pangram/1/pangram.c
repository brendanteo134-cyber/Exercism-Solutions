#include <stdint.h>
#include "pangram.h"
bool is_pangram(const char *sentence){
    char c = 0;
    uint32_t flags = 0;
    if(!sentence){
        return false;
    }
    for(int i = 0; (c = sentence[i]); i++){
        if(c >= 'A' && c <= 'Z'){
            c -= ('A' - 'a');
        }
        if(c >= 'a' && c <= 'z'){
            c -= 'a';
            flags |= (1 << c);
        }
    }
    for(int i = 0; i < 'z' - 'a'; i++){
        if(! (flags & (1 << i) )){
            return false;
        }
    }
    return true;
}
