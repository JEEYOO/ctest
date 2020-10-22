package hash;

public class dhkswPlayer2 { // 뭐가 잘못되었음 아 해결 ㅇㅋ 11 번째줄 completion.length 로 해야 줄어드는 거 확인 가능 
							// https://dreamhollic.tistory.com/entry/알고리즘-문제-풀이5-완주하지-못한-선수-JAVA     의 두번째 방법도 아직임
							// 아 https://wooaoe.tistory.com/54 보고 이해 끝 
	public static String solution(String[] participant, String[] completion) {
		String answer = "";
		
		for (int i =0; i<participant.length; i++) {
			boolean flag = true; //왜 블로그에선 boolean 도 안했냐? 
			for (int k =0; k<completion.length; k++) { //String whatever : participant
				if( participant[i].equals(completion[k]) ) {
					completion[k]= null; // 바로 null 로 만들어보리는거
					flag = false;
					break; // 이것 역시 핵심 
				}
			}
			if (flag) {
				answer += participant[i];
			}
		}	
		//System.out.println(answer);	
		return answer;
	}
	
	public static void main(String[] args) {
		String[] a = {"mislav", "stanko", "mislav", "ana"};
		String[] b = {"stanko", "ana", "mislav"};
		System.out.println(solution(a,b));
	}
}
