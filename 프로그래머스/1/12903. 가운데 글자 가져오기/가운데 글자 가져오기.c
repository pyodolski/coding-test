#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* s) {
    // 입력 문자열의 길이 계산
    int length = strlen(s);

    // 메모리 할당
    char* answer = (char*)malloc(sizeof(char) * 2);

    // 문자열의 가운데 글자 구하기
    if (length % 2 == 0) {
        // 짝수 길이인 경우
        answer[0] = s[length / 2 - 1];
        answer[1] = s[length / 2];
        answer[2] = '\0'; // 문자열 끝을 나타내는 널 문자 추가
    } else {
        // 홀수 길이인 경우
        answer[0] = s[length / 2];
        answer[1] = '\0'; // 문자열 끝을 나타내는 널 문자 추가
    }

    return answer;
}