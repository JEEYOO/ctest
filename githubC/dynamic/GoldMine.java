package dynamic;

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
	
	
	public static void dynamicStart(int[][] whatever,int b, int last, int each) { 
		int a = 0;								
		while (a+1 < last) { 
			if (b+1<each) { 
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
