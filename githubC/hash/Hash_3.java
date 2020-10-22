package hash;

import java.util.HashMap;
import java.util.Map;

public class Hash_3 {

	public static void main(String[] args) {
		String[][] clothes = {
				{"yellow_hat", "headgear"}, 
				{"green_turban", "headgear"},
				
				{"blue_sunglasses", "eyewear"}, 
				
				{"green_turban", "top"},
				
				{"ss","pants"},
				{"ss","pants"}
		};
		//int sum = clothes.length;
		int sum = 1;
		int index = 0 ;
		int[] num = new int[30]; //여기서 나왔는데 
		
		Map<String,Integer> cnt = new HashMap<String,Integer>();
		for(int i=0; i<clothes.length; ++i) { // 이게 i++가 아님 
			String wear = clothes[i][1];
			try {
				
				++num[cnt.get(wear)]; // 이건 뭐야 ??
				
			}catch(Exception e) {
				
				cnt.put(wear,index);
				num[index++] = 1; // 와 + 센스 지리농. 이렇게 되면 굳이 for (int i =.... 이런 식으로 할 필요 없)
			}
		}
		for(int i=0; i<cnt.size(); ++i) {
			sum *= num[i]+1;
		}
		System.out.println(--sum);

	}

}

/*
 * 머리:2, 얼굴:1, 상의:1,  바지:2 일 때,
 * 순열 이니까, 0인 경우만 추가해서 해주면 끝
 * 대신 아무것도 안 입은 경우는 없으니까 1을 빼준다.
 * (2+1) * (1+1)*(1+1) *(2+1) -1 = 35
 */