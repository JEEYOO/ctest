package grammar;

public class 동적fib {
	public static int fib(int whatever) {
		if (whatever <2) {
			return 1;
		}
		
		int result = fib(whatever-1) + fib(whatever-2); 
		
		return result;
	}
	
	public static void main(String[] args) {
		System.out.println(fib(10));
	}
}
