package grammar;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class asList { // 그냥 여기서 형변환 가지고 놀아볼까? 
	public static void main(String[] args) {
		
		// 일단 코테 질문들에서는 이거만 줄거아니야 
		String[] whatever = {"ab", "bc", "cd"};
		int[] haha = {4,5,7};
		
		
		List<String> dd = Arrays.asList(whatever);
		// List<Integer> ddd = Arrays.asList(haha); // List<int[]> 말이 안되는데 ㄷ
		
		
		// Map 만들어보자 
		HashMap<String, Integer> hmm = new HashMap<String, Integer>(); // Map Map 이 안 되네?
		for (int i =0; i<haha.length; i++) {
			hmm.put(whatever[i], haha[i]);
		}
		
		// 확인해보자 
		hmm.forEach((key, value) -> System.out.println("key: "+ key + ", value: "+value));
		// hmm.forEach((key)->System.out.println(key)); 두 개 다 해야하는군 
		dd.forEach((String)-> System.out.println(String));
		
	}
}
