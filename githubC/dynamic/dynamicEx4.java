package 동적;

public class 동적ex4 {// 백준 11727 행렬 2xn 
	
	public static int dynamics(int a) {
		if (a==1) {
			return 1;
		} else if(a==2) {
			return 3;
		}
		
		int result =0;
		result += dynamics(a-1);
		result += dynamics(a-2)*2; // 사실 3이라해도되긴 
		
		return result;
	}
	
	public static void main(String[] args) {
		System.out.println(dynamics(8));
		
	}

}
