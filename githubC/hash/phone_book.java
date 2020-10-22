package hash;

public class phone_book {
	public boolean solution(String[] phone_book) { // 양방향이엇구만 
        boolean answer = true;
        // 있으면 false 네 
        String b = phone_book[0];
        int a = b.length(); // 캐릭터 길이를 어떻게하더라 
        for (int i=1; i<phone_book.length; i++) { // String whatever : phone_book 되긴 되네. 이경우는 i=1로 시작해야하니까 패스
            if(b.equals(phone_book[i].substring(0,a))) {   
                return false;
}                        
        }
        
        return answer;
    }
}
