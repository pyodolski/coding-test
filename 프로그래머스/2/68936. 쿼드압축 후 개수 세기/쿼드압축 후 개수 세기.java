// 학번 : 22213489 이름 : 표주원
class Solution {
    public int[] solution(int[][] arr) {
        int[] answer = new int[2]; // 0 1 배열 생성
        // 분할 정복 시작
        compress(arr, 0, 0, arr.length, answer);
        return answer;
    }
    // 2차원 배열에서 값이 모두 같은지 확인하는 로직
    private boolean checkSame(int[][] arr, int row, int col, int size) {
        int value = arr[row][col];
        for (int i = row; i < row + size; i++) {
            for (int j = col; j < col + size; j++) {
                if (arr[i][j] != value) {
                    return false; 
                }
            }
        }
        return true;
    }

    // 분할 정복 함수
    private void compress(int[][] arr, int row, int col, int size, int[] answer) {
        if (checkSame(arr, row, col, size)) {
            answer[arr[row][col]]++; 
            return;
        }

        int half = size / 2;
        compress(arr, row, col, half, answer);                 // 좌상
        compress(arr, row, col + half, half, answer);          // 우상
        compress(arr, row + half, col, half, answer);          // 좌하
        compress(arr, row + half, col + half, half, answer);   // 우하
    }
}
