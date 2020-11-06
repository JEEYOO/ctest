package 동적;

public class 동적연습2 {
	public static int finalli(int hey) {
		
		//...?? 점화식이뭔데?
		
		//뭐 일일이 다 빼는 거보다 크진 않겠지 
		int[] hmm = new int[hey-1];
		
		for (int i=2; i<= 26; i++ ) {  
			hmm[i] = hmm[i-1] +1; // 아 이걸로 hmm[i] 끝이 아니라 후에 업데이트...
			// hmm[2] = hmm[1]+1 
			// 근데 애당초 hmm[1] 값도 없어 
			if (hey % 2 == 0) { hmm[i] = Math.min(hmm[i], hmm[i/2]+1);} // 즉 min으로 모든 케이스를 고려한다는 것 
			if (hey % 3 == 0) { hmm[i] = Math.min(hmm[i], hmm[i/3]+1);}
			if (hey % 5 == 0) { hmm[i] = Math.min(hmm[i], hmm[i/5]+1);} // 그럼 왜 +1이지? 
		}
		
		return count; // 이건 또 뭘 내놓아야하지?
	}
	
	public static void main(String[] args) {
		System.out.println(finalli(26));
	}
}

/*
int count = 0;
while (hey > 2) {
	if (hey % 5 == 0) { hey = hey/5; count++;} // hey /=  이게 문젠가?
	if (hey % 3 == 0) { hey = hey/3; count++;}
	if (hey % 2 == 0) { hey = hey/2; count++;}
	//심지어 이거도 -1 을 안넣었네 ㅅㅂ;; 

} // 아 이거아니야 최소한으로해야하잖아

if (hey==2) { // 2아니면 1이니 
	count++;
} 
*/