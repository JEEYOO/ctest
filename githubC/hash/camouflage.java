package hash;

import java.util.*;

class camouflage {
    public int solution(String[][] clothes) {
        int answer = 0;
        // value 4개가 headgear, eyewear, face...  말을 안해준거같은데 
        int b = clothes.length;
        
        // frequency 로 할까? <> 근데 각각 구분을 어캐함 
        // 옷 이름은 버려야함. <종류, 갯수> 로 새로 짜야함. 
        
        HashMap<String, Integer> what = new HashMap<String, Integer>();
        for (int i=0; i<b; i++){
            if (!what.containsKey(clothes[i][1])) {// Map 에 대해서 너무 모른다. 문법 
                what.put(clothes[i][1], 1);
            } else { // 안에 있다면 
                // +1 해라 라고 하고싶은데 
                Integer thisisIT = what.get(clothes[i][1]);
                what.put(clothes[i][1], ++thisisIT);
            }
        }// 이제 what 안에 예쁘게 만들어졌겠찌 
        
        
        // 종류로 곱셈
        Collection<Integer> example = what.values(); // 값만 뽑아내기 
        int c = example.size();
        switch(c) {
            case 1 :
                answer += b; // 1번방법
                break;
            case 2 :
                answer = 1;
                for (Integer newm : example) { // 2번방법에다가 
                    answer *= newm;   
                }
                answer += b; // 1번방법더하기
                break;
            case 3 : // 사실상 others? 뭐 3개 아님 4개긴한데..
                      //  2개짜리를 재귀로 만들어버릴까 
                int f=1;
                for (Integer e:example){
                    f*=e;
                }			
                answer+=f;  // 3개 곱하기 
                answer+=temp2(example); // 3개중 2개  
                answer += b;  // 한 개 
                break;
            case 4:      
                int g=1;
                for (Integer e:example){
                    g*=e;
                }
                answer += g; // 4개곱하기 
                answer += temp3(example);
                answer += temp2(example);
                answer += b;
                break;
        }   
        
        return answer;
    }
    
    public int temp2(Collection<Integer> comeArray) {
        int temper=0;
        // 2개일때
        ArrayList<Integer> temp = (ArrayList<Integer>) comeArray;
        										// 4개라 생각하자 
        for (int i=0; i<comeArray.size(); i++){ // 0일 때   | 1일때  2일때 
            for (int k=1+i; k<comeArray.size(); k++){ // k=1,2,3 | 2,3 | 3  
                temper+= temp.get(i)*temp.get(k);
            }
        }
        
        return temper;
    }
    
    public int temp3(Collection<Integer> comeArray) {
        int temper=0;
        // 3개일때
        // 뭐지? remove 인가? 
        for (int i=0; i<comeArray.size(); i++){
            ArrayList<Integer> tempp = (ArrayList<Integer>) comeArray;  // 형변환을 이렇게 억지로하다니 ㅋㅋㅋ 
            //ArrayList<Integer> temp2 = (ArrayList<Integer>) comeArray;
            tempp.remove(i); // 이거 설마 곂치는 거 다 없애나? temp2.get(i) 
            int d = 1;
            for (Integer wkatl : tempp){
                d *= wkatl;
            }
            temper +=d;
        }
        
        return temper;
    }
    
    
}
