package grammar;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;

public class IteratorTest {
	public static void main(String[] args) {
		ArrayList<String> whatever = new ArrayList<String>(); // ArrayList하니까 안되나?
		whatever.add("테스");
		whatever.add("형");
		
		Iterator<String> thisis = whatever.iterator(); // 이름 때문이었구만 
		while (thisis.hasNext()) {
			System.out.println(thisis.next());
		}
	}
}
