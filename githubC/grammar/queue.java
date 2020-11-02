package grammar;

import java.util.PriorityQueue;
import java.util.Queue;

public class queue {
	// poll 하고 peek 실험좀 해보자 
	public static void main(String[] args) {
		String[] hmm = new String[] {"da","3","4","5","6"};
		Queue<String> whatever = new PriorityQueue<String>();
		
		//System.out.println(whatever.size());
		
		while(whatever.size()<5) {	
			System.out.println(hmm[whatever.size()]);
			whatever.add(hmm[whatever.size()]);
			// 이건 잘 들어갔는데 
		}
		
		for (String what:whatever) {
			System.out.println(what);
			// 순서가 왜 3,5,4,da,6 이야??  
		}
		
		//peek
		System.out.println(whatever.peek()); // 이게 왜 3이지?
		System.out.println(whatever.peek());
		System.out.println(whatever.peek());
		
		//poll
		System.out.println(whatever.poll());
		System.out.println(whatever.poll());
		System.out.println(whatever.poll());
		
		
	}
}
