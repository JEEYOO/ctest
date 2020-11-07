package grammar;

import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Set;

public class Map { // 뭐 실험하려고 했었는데 흠 
	public String solution(String[] participant, String[] completion) {
		
		HashMap<String, Integer> whatever = new HashMap<String, Integer>();
		whatever.put("test",11);
		whatever.get(11);
		Collection<Integer> test1 = whatever.values();
		
		
		Set<String> test2 = whatever.keySet();
		return null;
	
	}
	
	public static void main(String[] args) {
		HashMap<String, Integer> whatever = new HashMap<String, Integer>();
		whatever.put("test",11);
		System.out.println(whatever.get("test")); // 11은 안되지만 
		
		/*     그냥 이런 형태가 안 된다.
		HashMap<Integer, Integer> whatever2 = new HashMap<Integer, Integer>();
		whatever.put(13,12);
		*/
		
	}
}
