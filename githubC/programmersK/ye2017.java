package programmersKakao;

import java.util.ArrayList;
import java.util.Collections;

public class ye2017 {
	int span = 0;

    public int[] solution(int m, int n, int[][] picture) {

        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        boolean[][] pathBool = new boolean[m][n];
        ArrayList<Integer> answerList = new ArrayList<>();
        int[] answer = new int[2];
        for (int i = 0; i < m; i++) {
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
            return; // 이미 거친 경로일 경우 바로 나가버림(?) 
        long su = picture[m][n]; // 이미지 값
        int column = picture[0].length;
        int row = picture.length;
        pathBool[m][n] = true;
        span++;
        // 오른쪽 이동
        if ((n + 1 < column) && (pathBool[m][n + 1] == false && su == picture[m][n + 1])) {
            findPath(m, n + 1, picture, pathBool);
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
    	ye2017 solution = new ye2017();
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
