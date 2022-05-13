package 동적;

public class IntegerTriangle {
	public int solution(int[][] triangle) {
        int answer = 0;
        // 카피로 하나 떠놓고 (이거는 합계만 계산하는거)
        int[][] copy = triangle;
        int len = triangle.length;
                    for (int k=1; k<len; k++){
                        for (int i=0; i<=k; i++){
/*null 로 exception 만들기?! */if (i==0 || i==k) {
                                if (i==0) {
                                    copy[k][i] = triangle[k][i] +copy[k-1][i];
                                } else {
                                    copy[k][i] = triangle[k][i] + copy[k-1][i-1];
                                }
                            } else {
                                copy[k][i] = triangle[k][i] + Math.max(copy[k-1][i-1], copy[k-1][i]);
                            }                
                        }
                    }
        
        answer = copy[len-1][0];
        for (int h=0; h<len; h++) {
            if (answer < copy[len-1][h]) {
                answer = copy[len-1][h];
            }
        }
        
        return answer;
    }
    
}

