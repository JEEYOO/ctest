package hash;

import java.util.ArrayList;
import java.util.HashMap;

public class camouflage2 {
	public static int solution(String[][] clothes) {
		int answer = 1;
		
		HashMap<String, Integer> what = new HashMap<String, Integer>();
        for (int i=0; i<clothes.length; i++){
            if (!what.containsKey(clothes[i][1])) {// Map 에 대해서 너무 모른다. 문법 
                what.put(clothes[i][1], 1);
            } else { // 안에 있다면 
                // +1 해라 라고 하고싶은데 
                Integer thisisIT = what.get(clothes[i][1]);
                what.put(clothes[i][1], ++thisisIT);
            }
        }// 이제 what 안에 예쁘게 만들어졌겠찌 
        
        
        // 종류로 곱셈
        ArrayList<Integer> example = new ArrayList<Integer>();
        what.values().forEach((value)-> example.add(value+1)); 
		
        for (int nums: example) {
        	answer *= nums;
        }
        
		return answer-1;
	}
}
