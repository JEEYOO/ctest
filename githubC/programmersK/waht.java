package programmersKakao;

class waht {
    public static long solution(int w, int h) {
        long answer = 0;
        
        // 아 double, long 같은 게 문제라면 out of my control 이다 ㄹㅇ      // 당장 예제값도 다르다   
        long minus = 0;
        
        if (w>h) {
            long temp = (w/(long)h);
            System.out.println(temp);
            
            for (int i=0; i<h; i++){
                minus += (long)Math.ceil((i+1)*temp)- (long)Math.floor(i*temp);
            }
            answer = (long)(w*h) - (long)minus;
        } else if (w<h) {
            double temp = h/(double)w;
            System.out.println(temp);
            
            for (int i=0; i<w; i++){
                    minus += (long)Math.ceil((i+1)*temp)                              - (long)Math.floor(i*temp);
            }
            answer = (long)(w*h) - (long)minus;
        } else {
            answer = (long)(w*h) - (long)w;
        }
        
        return (long)answer;
    }
    
    public static void main(String[] args) {
    	solution(8,12);
    }
}