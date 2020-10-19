package programmersKakao;

import java.util.ArrayList;
import java.util.Collections;

class Solution {
    int span = 0;

    public int[] solution(int m, int n, int[][] picture) {

        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        boolean[][] pathBool = new boolean[m][n];
        ArrayList<Integer> answerList = new ArrayList<>();
        int[] answer = new int[2];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j <n; j++) { // 0, 0 에 대해서 
                if (picture[i][j] > 0) {
                    findPath(i, j, picture, pathBool);
                    if(span > 0){
                        answerList.add(span);
                        span = 0;
                    }
                }
            }
        }
        numberOfArea = answerList.size();
        if(numberOfArea == 0){
            return new int[]{0, 0};
        }
        Collections.sort(answerList, Collections.reverseOrder());
        maxSizeOfOneArea = answerList.get(0);
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    public void findPath(int m, int n, int[][] picture, boolean[][] pathBool) { // 재귀에서 돌려벼리니까 solution 갈 필요도 없이 여기서 span 값이 완성되는구나 
        if (pathBool[m][n] == true)
            return; // 이미 거친 경로일 경우
        long su = picture[m][n]; // 현재 포인터위치의 이미지 값 1,1
        int column = picture[0].length; // 이게 사실상  m 6
        int row = picture.length;       // 이게 사실상  n 4
        pathBool[m][n] = true;
        span++; // 얘로 판가름 내는구만 지금 span 4
        // 오른쪽 이동
        if ((n + 1 < column) && (pathBool[m][n + 1] == false && su == picture[m][n + 1])) { // 0,1 도 1이니? //0,2
            findPath(m, n + 1, picture, pathBool); // 맞다면 얘도 재 //재귀
        }
        // 아래쪽 이동
        if ((m + 1 < row) && (pathBool[m + 1][n] == false && su == picture[m + 1][n])) { // 1,0 //2,0
            findPath(m + 1, n, picture, pathBool); 
        }
        // 왼쪽 이동
        if ((n - 1 >= 0) && (pathBool[m][n - 1] == false && su == picture[m][n - 1])) {
            findPath(m, n - 1, picture, pathBool);
        }
        // 위쪽 이동
        if ((m - 1 >= 0) && (pathBool[m - 1][n] == false && su == picture[m - 1][n])) {
            findPath(m - 1, n, picture, pathBool);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int m = 6;
        int n = 4;
        int[][] picture = {
                {1, 1, 1, 0},
                {1, 2, 2, 0},
                {1, 0, 0, 1},
                {0, 0, 0, 1},
                {0, 0, 0, 3},
                {0, 0, 0, 3}};
        System.out.println(solution.solution(m, n, picture)[0] + ", " + solution.solution(m, n, picture)[1]);
    }
}
