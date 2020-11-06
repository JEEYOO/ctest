package 동적;

import java.util.ArrayList;

public class 동적ex {
	
	public static int dynamics(int[] hmm) { 
		int nn = hmm.length;
		  
		//ArrayList<Integer> wow = new ArrayList<Integer>(); 아냐 이게 더 말이안됨 
		
		int[] arrr = new int[nn];  //카피본하나떠놓고 <> 필없
		 
		arrr[0] = hmm[0]; // 1
		arrr[1] = Math.max(hmm[0], hmm[1]); // 1 or 3 -> 3
		for (int i=2; i<nn; i++) {
			arrr[i] = Math.max(arrr[i-1], arrr[i-2]+hmm[i]);// 근데 여기서 Max를 생각해내는 거는 수학적 sense 야. 다 공식이 아니라
		}
		// 굳이 재귀한다! 라고 할 필요는 없구나 포인트는 (어떻게해서든)그 전 두 값에서 끌어오는 것 
		return arrr[nn-1];
	}
	
	public static void main(String[] args) {
		int[] what = {1,3,1,5};
		System.out.println(dynamics(what));
	}
}

/*
public static int whatever(int[] hmm) {
	int answer = 0;
	
	
	return answer;
}

public static int dynamics(int[] hmm) { //일단 manual 로 몇개는 계산 때리고 
	int result = 0;
	
	if (hmm.length==1) {
		return hmm[0];
	} else if (hmm.length==2) {
		result = (hmm[0] > hmm[1])? hmm[0] : hmm[1]; // 이거 어떻게하더라?
		                                             // 잘 배우긴했는데 걍 max 쓰면되는데;;
		return result;
	}
	
	// int[] 안에 들어가있으니까 이걸 어떻게해야

	
	return result;
}
*/