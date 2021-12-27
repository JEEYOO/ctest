class Solution {
    public int distance(int a, int b) {
        int dis = Math.abs(a-b)%3 + Math.abs(a-b)/3; 
        return dis;
    }
    
    public String solution(int[] numbers, String hand) {
        
        String answer = "";
        int lhand=10, rhand=12;
        
        for (int i=0; i<numbers.length; i++) {
            if (numbers[i]==1 || numbers[i]==4 || numbers[i]==7) {
                answer += "L"; // answer = L
                lhand = numbers[i]; // lhand = 7
            } else if (numbers[i]==3 || numbers[i]==6 || numbers[i]==9) {
                answer += "R";
                rhand = numbers[i];
            } else {
                
                // 0
              
                if (i==0) { 
                    switch (hand) {
                        case "right":    
                            answer += "R";
                            rhand = numbers[i];
                            break;
                        case "left":
                            answer += "L";
                            lhand = numbers[i];
                            break;
                    }
                } else {
                
                    if (numbers[i]==0) {
                        numbers[i] = 11;
                    }
                    
                     
                    
                        int rdis= distance(numbers[i], rhand);      
                        int ldis= distance(numbers[i], lhand);
                        
                        
                         
                        if (rdis==ldis) {
                            switch (hand) {
                                case "right":    
                                    answer += "R";
                                    rhand = numbers[i];
                                    break;
                                case "left":
                                    answer += "L";
                                    lhand = numbers[i];
                                    break;
                            }
                        } else if (rdis > ldis) {
                            answer += "L";
                            lhand = numbers[i];
                        } else {
                            answer += "R";
                            rhand = numbers[i];
                        }
                    }
                }    // 0은 11로 보고. 
                    // 3으로 나눠서 차수!
                    
                    
                    // 똑같을 때 (if 안에 넣어야 할 듯)
                    
            }   
        
        
        return answer;
    }
}
