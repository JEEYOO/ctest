package grammar;

import java.util.ArrayList;

public class rmsid10wlstnwlstn {
	public static void main(String[] args) {
		int example = 109239;
		System.out.println(changer(46,7));
	}
	
	public static int changer(int what, int n) { // whatever를 n진수로 바꿔보겠다.
		
		// ArrayList 는 안 좋은게 add 하면 순서가 -> 대체제 찾기      A. 대체제 없
		ArrayList<Integer> hmm = new ArrayList<Integer>();
		
		do { // 0이 되면 빠져나온다 이거
			
			hmm.add(what%n); // 밑의 update 에 의해 값이 바뀔 수 있으니  
			
			what = what/n; //몫은 계속끌고가야 //33
		
			// 10씩 곱할 거 아니면 arrayList가 나으려나? 
		} while (what/n!=0);
		
		hmm.add(what%n); // 0추가 
		hmm.add(what/n); //딱 나누어떨어지는값추가 
		
		
		double temp = 0;
		// 지금 들어간건 역순 4, 6 -> 이걸 넣을 때 10 곱해서 넣는걸로하면될듯 
		for (int i=0; i<hmm.size(); i++) {
			temp += hmm.get(i) * Math.pow(10, i);
					// 아 제곱 
		}
		
		return (int) temp; 
	}
}
