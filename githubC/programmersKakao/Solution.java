package programmersKakao;

import java.util.ArrayList;
import java.util.Collections;

class Solution {
    int span = 0; // 아예 밖에 나둬놓음 

    public int[] solution(int m, int n, int[][] picture) {

        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        boolean[][] pathBool = new boolean[m][n];
        ArrayList<Integer> answerList = new ArrayList<>();
        int[] answer = new int[2];
        
        
        for (int i = 0; i < m; i++) { // 동서남북으로 하는 대신 전부 다 하네.
            for (int j = 0; j <n; j++) {
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

    public void findPath(int m, int n, int[][] picture, boolean[][] pathBool) {
        if (pathBool[m][n] == true)
            return; // 이미 거친 경로일 경우 바로 빠져나간다 이거지 
        long su = picture[m][n]; 
        int column = picture[0].length;
        int row = picture.length;
        pathBool[m][n] = true;
        span++;
        // 오른쪽 이동
        if ((n + 1 < column) && (pathBool[m][n + 1] == false && su == picture[m][n + 1])) {
            findPath(m, n + 1, picture, pathBool); // 아 재귀였네? 
        }
        // 아래쪽 이동
        if ((m + 1 < row) && (pathBool[m + 1][n] == false && su == picture[m + 1][n])) {
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
        int m = 4;
        int n = 4;
        int[][] picture = {
                {1,1,1,1},
                {1,4,1,1},
                {1,3,2,1},
                {1,1,1,1}};
        System.out.println(solution.solution(m, n, picture)[0] + ", " + solution.solution(m, n, picture)[1]);
    }
}