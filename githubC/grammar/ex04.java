package grammar;

import java.util.Scanner;

public class ex04 {
	public static void main(String[] args) {
		System.out.println("메세지를 입력하십시오.");
		System.out.println("프로그램을 종료하려면 'q'를 입력하십시오.");
		
		// 입력 객체는 수동으로 생성한다.		
		Scanner Whatever2 = new Scanner(System.in); // SCV 객체 를 수동으로 설정해야한다. ★★★말 그대로 복사해주는 역할(?)★★★
		//System.in.Read()도 그렇고 System.in으로 시작하는 것 자체가 뉴스킬인가보다
		// 이름 짓는 것만으로는 쓰이지 못 하지. 
		String whatever;
		
		do {
			System.out.println(">>>>>>>>>");
			whatever = Whatever2.nextLine();  	// 입력 객체의 nextLine 메소드  percentS 와 같다.★★★문자열을 입력받을 때★★★	
			// 이 때 처음으로 쓰인 거																
		} while(!(whatever.equals("q"))); // 이걸로 봐서 whatever 역시 System.in.Read()처럼 값을 받는 다는 것을 알 수 있다.
		
		System.out.println();
		System.out.println("프로그램을 종료합니다.");
	}
}

