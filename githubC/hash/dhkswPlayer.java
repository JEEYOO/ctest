package hash;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import empty.Solution;

public class dhkswPlayer {
	public static String solution(String[] participant, String[] completion) {
        String answer = "";
        int a = participant.length;
        int b = completion.length;
        
        List<String> listP = new ArrayList<String>(Arrays.asList(participant));
        List<String> listC = new ArrayList<String>(Arrays.asList(completion));
        
        for (int i=0; i<a; i++) {
            int count = 0;
            String temp = participant[i];
            for (int k=0; k<b; k++) {
                if (participant[i].equals(completion[k])) {
                         count++;
                }
            }   
            System.out.println("count " + count);  
            System.out.println("P "+ Collections.frequency(listP,temp));
            System.out.println("C " + Collections.frequency(listC,temp));
            if (count==0){ 
                return participant[i];
            } else if (count>1 && ((Collections.frequency(listP,temp)-Collections.frequency(listC,temp))==1)) {
                return temp;
            }               //2개 이상이면 participant찾은거-completion찾은거= 1이면 return?
       
        }
              
            
        
        //answer = temp.get(0);
        return answer; 
    }

	public static void main(String[] args) {
		String[] a = {"mislav", "stanko", "mislav", "ana"};
		String[] b = {"stanko", "ana", "mislav"};
		solution(a,b);
	}
}
