package stackQueue;

import java.util.ArrayList;
import java.util.Arrays;

public class stockPrice {
	public static int[] solution(int[] prices) { // 시박 효율성테스트 깔끔하게 통과를 못하노 아 Stack? 
        int len = prices.length;
        int[] answer = new int[len];
        
        // 아 이거 공부 ㄱ 
        ArrayList<Integer> demoAns = new ArrayList<Integer>();
            
        int count;    
        for (int k=0; k<len; k++) { // for (int what:prices) {// 하나하나 
        // 아 이번엔 이거 안되겠네 밑에 i=k+1로 써야함 
            count = 0;
            for (int i=k+1; i<len; i++) {
            	count++;
                if (prices[k]>prices[i] || (i==len-1)) { //아 최대일때 나가버리는구만 이렇게 조건 하는 거 아니면 count++하다가 조건 맞으면 break; 방법도 있음  
                	System.out.println(count);
                    demoAns.add(count);
                    break; // 아 break 타이밍도 알아야해 
                } 
            }
        }
        demoAns.add(0);
        // ArrayList<Integer>를 int[] 로 바꾸는 법 <> for 말고 쉐캬
        answer = demoAns.stream().mapToInt(Integer::intValue).toArray();
        // System.out.println(Arrays.toString(demoAns));                흠 얘는 어떻게 출력? 
        return answer;
    }
	
	public static void main(String[] args) {
		int[] test = {1,2,3,2,3};
		System.out.println(Arrays.toString(solution(test)));
	}
}
