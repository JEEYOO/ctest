package heap;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class moreSpicy {
	public static int solution(int[] scoville, int K) {
        int answer = 0;
        // int[] 가 계속 바뀌네 사이즈가 그럼 차라리 하나 만드는게 
        ArrayList<Integer> temp = new ArrayList<Integer>();
        // 어차피 return 은 숫자 answer만 하면 돼.
        
        for (int k=0; k<scoville.length; k++){ 
        //이거 while 사용하면 count++ 해서 sizeㄴlength크기하고 같아질때까지
            temp.add(scoville[k]);
        }
        
        //@ temp.get(0)<K 이건 왜 안되지 
        while (!(judge(temp, K))) { // false여야나올수있으니!붙여줌     
        	if(temp.size()<2) { // K이상으로 만들수없는경우 구만 이게 
        		answer = -1;
        		break;
        	}
        	Collections.sort(temp); // 오름차순 sort 아니었나?
            int a = temp.get(0);                                // 3
            System.out.println(a);
            int b = temp.get(1);								// 5
            System.out.println(b);
            temp.remove(0);		
            temp.remove(0); // 아 이거구나  remove(1)이 아니다!
            int c = a + b*2;									// 13
            System.out.println(c);
            temp.add(c); // 하긴 이게 맨 처음으로 들어간다면 sort는 할 필요없겠지 
            answer++;
        }
        
        return answer;
    }
    
    public static boolean judge(ArrayList<Integer> whatever, int K2) {
        
    	for (int h=0; h<whatever.size(); h++){
            if (whatever.get(h) < K2){ //통과못하면  
                return false;
            }
        }
        return true; //통과하면 
    }
    
    // 역시나 효율성은 0%구만. 
    // heap 이 Queue 야? 
    public static void main(String[] args) {
    	int[] what = new int[] {1, 2, 3, 9, 10, 12};
    	System.out.println(solution(what, 7));
    	
    	/*
    	int[] what2 = new int[] {9,10,12,13};
    	ArrayList<Integer> temp2 = new ArrayList<Integer>();        
        for (int k=0; k<what2.length; k++){ 
            temp2.add(what2[k]);
        }
    	System.out.println(judge(temp2,7));
    	*/
    }
}
