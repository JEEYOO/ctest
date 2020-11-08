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

/*
<> 실험하는 거는 좋은데 이 경우는 아예 bound error 나버려서 내가 미리조치해야함 

public int dynamics(int[][] triangle, int floor) {
       
   }
*/

/*
 * public int solution(int[][] triangle) {
        int answer = 0;
        //1번째 2번째까지만 한 다음에
        int floor = triangle.size(); // 나중에 -1해야겠지 
        // k k+1 로 하면 되겠는데 <> out of bounds도 안 걸릴거고 
        
        return answer;
    }
    
    public int dynamics(int[][] triangle, int floor) {
        if (floor ==1) { return triangle[0][0]; }
        
        int x=0;
        while (x != floor) {
            [그대로 x][+1]
            x++;
        }
        //... 개념도 확실하지 않은데 담는 법을 어찌알겟누
    }
 * */
 