package challengeKit;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class SAT {
	public int[] solution(int[] answers) {
        int[] answer = {};
        int len = answers.length;
        // 1번  12345
        int a = 0;
        int[] one = {1,2,3,4,5};
        for (int i=0; i<len; i++){
            if(one[i%5]==answers[i%5]){ 
                a++;
            }
        }
        
        // 2번  2와 1345 번갈아가면서 -> 2 4 6 8 위치 
            // 홀짝으로 나눌까. /2 %2
        int b = 0;
        int[] two = {2,1,2,3,2,4,2,5};
        for (int i=0; i<len; i++){
            if(two[i%8]==answers[i%8]){ 
                b++;
            }
        }
        
        // 3번  3 1 2 4 5 쌍으로
            // 이건 뭐 10번이고 
        int c = 0;
        int[] three = {3,3,1,1,2,2,4,4,5,5};
        for (int i=0; i<len; i++){
            if(three[i%10]==answers[i%10]){ // 이유 ㅣ발 ㅋㅋㅋㅋ  
                c++;
            }
        }
        //<> 아님 각각 배열을 만들어서 비교하든가  this was an answer
        
        
        // answer 추리기 ... 3중비교를 어떻게하지? 
        int[] temp = {a,b,c}; 
        
        int d = Math.max(a,Math.max(b,c));
        
        // add 못하잖아 
        ArrayList<Integer> answer2 = new ArrayList<Integer>();
        for (int k=0; k<3; k++){
            if(temp[k]==d){
                answer2.add(k+1); // 최대값을 넣는게 아니라 몇번째수포자인지를
            }
        }
        // Collections.sort(answer2); //add가 참 안좋아      근데 이 케이스는 있으나마나인데? 

        // 이식
        answer = new int[answer2.size()];
        for (int last=0; last<answer2.size(); last++){
            answer[last] = answer2.get(last);
        }
        
        return answer;
    }
}
