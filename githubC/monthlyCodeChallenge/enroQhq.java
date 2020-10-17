package monthlyCodeChallenge;
import java.util.*;
public class enroQhq {

    public static int[] solution(int[] numbers) {
    	 int[] answer = {};
         ArrayList<Integer> temp = new ArrayList<Integer>(); 
         
         for (int i =0; i<numbers.length; i++) { // 0
             // +- 1하는 기준을 찾아야할 것 같은데 
             for (int k = 1; k<numbers.length-i; k++) { // 1
             // 아 int array 에 add 하는 법 
                 int a = numbers[i] + numbers[i+k]; // 2+1
                 //System.out.println(a);
                 
                 if (!temp.contains(a)) { // 겸사겸사 얘찾자  
                     temp.add(a); // temp 에만업데이트되니까 문제였
                 } 
             }
         }
         
         answer = new int[temp.size()];
        //System.out.println(temp.size());
         for (int i=0; i< temp.size(); i++) {
             answer[i] = temp.get(i);
             
         }
         Arrays.sort(answer);
         return answer;
    }
    
    public static void main(String[] args) {
    	int[] what = new int[] {2,1,3,4,1};
    	System.out.println(Arrays.toString(solution(what)));
    }
    
	
}
