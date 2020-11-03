package challengeKit;

import java.util.ArrayList;

public class peClothes {
	public static int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        int minus = 0;
        
        if (lost.length==0) {
            return n;
        } else if (reserve.length==0) {
        	return n-lost.length;
        }
        
        ArrayList<Integer> lost2 = new ArrayList<Integer>();
        for (int k=0; k<lost.length; k++) {
            lost2.add(lost[k]);
        }
        
        ArrayList<Integer> reverse2 = new ArrayList<Integer>();
        for (int k=0; k<reserve.length; k++) {
            reverse2.add(reserve[k]);
        }
        
        /* 같은 거 있으면 제거하기 */
                                 /// 계속 반복되고 있는 문제점은 for 의 전체범위를 손대고있다는것 remove 로 인해서 
        for (Integer what:lost) {//이거인거같은데 ㅇㅇ 전체범위는 손대면안돼.
        	
        	if (reverse2.contains(what)) {
        		int e = reverse2.indexOf(what);
        		reverse2.remove(e);
        		int f = lost2.indexOf(what);
        		lost2.remove(f); // 이게 잘못되었다. 계속 변하잖아 
        	} 
        }
        // lost 기준으로
        for (int k=0; k<lost2.size(); k++){
        	boolean a = reverse2.contains(lost2.get(k)-1); // 이거도처음 사용해보고 
	        boolean b = reverse2.contains(lost2.get(k)+1);
            
	        if ((a||b)==false){
            	minus++;
            } else {
                if(a){ // 아 값제거해야하네
                    int c = reverse2.indexOf(lost2.get(k)-1);  // 이거도 처음사용해보니까 검증을 거쳐야하나? 거침v  
                    reverse2.remove(c); //이건 위치제거고 
                } else {
                    int d = reverse2.indexOf(lost2.get(k)+1);
                    reverse2.remove(d);
                } // 아 그건가? 둘 다빌려줄수있는데 remove 해버려서? <> 근데 이거면 -1 부터 하면되는거아님?  
            }
        // +-1이 lost 에 있는지 확인해서 있으면 remove (이것도 [] 에 없네)
        // 배열은 search(이건 Stack) 못하잖아   !아 contains(Key는 Map꺼고) 
        }
        
        
        return answer-minus;
     // 어차피 결과는 integer 니까 딱히 [] 유지안해도 상관없을듯
    }
	
	public static void main(String[] args) {
		int[] lost = {3};
		int[] reverse = {1};
		System.out.println(solution(3,lost,reverse));
	}
}

/*
 * 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
 
 문제 잘읽기 
 * */
