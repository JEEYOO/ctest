package 동적;

public class GoldMine {
	static int result = 0; 
	
	public static int dynamics(int[][] whatever) {
		
		int len = whatever.length;  
						
		int each = whatever[0].length; // 3
		
		
		
		
		
		int start = 0, save=0;
		
		for (int k=0; k<each; k++) {
			if (start<whatever[0][k]) {
				save = k;
				start = whatever[0][k];
			}
		}
		System.out.println(save);
		result+=whatever[0][save];
		
		
		dynamicStart(whatever,save,len,each); 
		
		
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
					result += whatever[a][b+1];
					b++;
				}
				
			} else { 
				result += whatever[a+1][b];
				a++;
			}
		
			
		}
		
		
	}
	
	public static void main(String[] args) {
		
		int[][] hmm = {{1,2,0},{3,1,6},{3,4,4},{2,1,7}};
		System.out.println(dynamics(hmm));
		
	}
}

/*
 * Math.max(whatever[a+1][b], Math.max(whatever[a+1][b+1], whatever[a][b+1]));
 * 
 * 
 * int[][] hmm = {{1,3,3,2},{2,1,4,1},{0,6,4,7}};
 * */
