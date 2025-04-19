#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long answer = 0;
    
    if (a < b) {
        for (int i = a; i <= b; i++) {
            answer += i;
        }
    } else if (a > b) {
        for (int i = b; i <= a; i++) {
            answer += i;
        }
    } else { // a와 b가 같은 경우
        answer = a;
    }

    return answer;
}
