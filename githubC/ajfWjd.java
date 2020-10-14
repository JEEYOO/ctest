class Solution {
    public long solution(int w, int h) {
        long answer = 0;
        
        // 아 double, long 같은 게 문제라면 out of my control 이다 ㄹㅇ      // 당장 예제값도 다르다   
        long minus = 0;
        
        if (w>h) {
            double temp = (w/(double)h);
            for (int i=0; i<h; i++){
                minus += Math.ceil((i+1)*temp)                              - Math.floor(i*temp);
            }
            answer = w*h - minus;
        } else if (w<h) {
            long temp = (h/(long)w);
            for (int i=0; i<w; i++){
                    minus += Math.ceil((i+1)*temp)                              - Math.floor(i*temp);
            }
            answer = w*h - minus;
        } else {
            answer = w*h - w;
        }
        
        return answer;
    }
}
