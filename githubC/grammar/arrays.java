package grammar;

import java.util.Arrays;

public class arrays {
	public static void main(String[] args) {
		String[] arr = { "hmm", "hmm1", "hmm2"};
		
		String[] what = Arrays.copyOfRange(arr, 2, 3);
		
		System.out.println(what.toString());
		System.out.println(Arrays.toString(what));
	}
}
