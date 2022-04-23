package 동적;

public class GoldMine {
	static int result = 0; // static 없어도되니? 
	
	public static int dynamics(int[][] whatever) {
		
		int len = whatever.length;  // 근데 이거 각 라인별로 내려가면안돼. 
									// 밑으로 내려갈수도있음 
		int each = whatever[0].length; // 3
		
		
		
		
		
		int start = 0, save=0;
		// 이거하기도뭐한게 혹시 값이 겹치면어떡함 <> 이건일단생각하지말고하
		for (int k=0; k<each; k++) {
			if (start<whatever[0][k]) {
				save = k;
				start = whatever[0][k];
			}
		}
		System.out.println(save);
		result+=whatever[0][save]; // 이거도 밑에서 해서 필요없어짐? 
		
		
		/* 출발점은 (0,k)  
		   빠져나가는거만방지해서하면될듯 */ 
		dynamicStart(whatever,save,len,each); 
		//만약 저 밑에서 다 할거같으면 이거 필요없을거같긴... 아 물론 오른쪽항은 해야지. void 로만들던가   
		
		return result;
	}
	
	// 출발점 반영해서 함수하나더만들어야겠는데
	public static void dynamicStart(int[][] whatever,int b, int last, int each) { // 아어차피 x는 0이구만 
		int a = 0;									// 스타트y,    4,        3 
		while (a+1 < last) { /* 이렇게 하면 a 라는 마지막에서 */
			if (b+1<each) { // 물론 거기서 없으면 찾지말고 out of bounds 처리
				System.out.println("check");
				if (whatever[a+1][b]>whatever[a][b+1]) {
					result += whatever[a+1][b];
					a++;
				} else {
					result += whatever[a][b+1]; // 똑같으면 라인걸치는게낫지 ...? -> 이생각이 틀린거같은데 
					b++;
				}
				// 먼저 Max 값찾고 <> 근데 이거 바로 계산하면 위치 못찾을걸 
				/*아 같은 값있으면 옆부터 먼저가야하는데
				 * 아 아니다. 대각선은 생각하는게 아니네. 무조건 거쳐서가는게낫잖아? 대각선은 페이크임* */  
				
			} else { // 한줄각 
				result += whatever[a+1][b];//뭐지 한 템포빠른거같은데 
				a++;
			}
			// 거기로 이동한 다음에  
			
		}
		// 끝이라 나왔다.	
		
	}
	
	public static void main(String[] args) {
		
		int[][] hmm = {{1,2,0},{3,1,6},{3,4,4},{2,1,7}};
		System.out.println(dynamics(hmm));
		/* 아 m-1번에 거쳐서 = 굳이 끝까지 안가도 수만크다면ㄱㅊ? 
		   + 이렇게 되면 3개 다 해야겠네
		   
		   새로운 국면이구만  <> 걍 답지볼까? 어차피내가하는거는 DP가 아닌거같은
		*/
	}
}

/*
 * Math.max(whatever[a+1][b], Math.max(whatever[a+1][b+1], whatever[a][b+1]));
 * 
 * 
 * int[][] hmm = {{1,3,3,2},{2,1,4,1},{0,6,4,7}};
 * */
