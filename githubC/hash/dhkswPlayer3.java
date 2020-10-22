package hash;

import java.util.Arrays;

public class dhkswPlayer3 {
	public String solution(String[] participant, String[] completion) {
        //String answer = "";
        Arrays.sort(participant);
        Arrays.sort(completion);
        int i;
        for (i=0; i < completion.length; i++) {
            if (!participant[i].equals(completion[i])) {
                return participant[i]; // 아 정렬을 했고, 참가자가 무조건 더 많으니까 
            }
        }
        return participant[i];
        // 아 효율성위해서는 해시 쓰라는거야? 
        
        //return answer; 
    }
}
