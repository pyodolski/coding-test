#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// box_len은 배열 box의 길이입니다.
int solution(int box[], size_t box_len, int n) {
    int answer = 0;
    int v = n*n*n;
    int a = box[0]-(box[0]%n);
    int b = box[1]-(box[1]%n);
    int c = box[2]-(box[2]%n); 
  
    
    answer = a*b*c/v;
    return answer;
}