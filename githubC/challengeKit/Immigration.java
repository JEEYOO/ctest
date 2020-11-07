package challengeKit;

public class Immigration {
	public long solution(int n, int[] times) {
        // n이 기다리는사람, times의 length가 심사관 수고 각각걸리는시간
        
        long answer = 0;// 근데 이거 왜 long 이지? 구하는 방법이 특이한거같은데
        
        // 7 14 21 곱하면서 n하나씩 제거하면되겠다.
        // 10 20 -> 여기서 마무리 +
        
        
        if (n<=times.length) { /* times이거 오름차순으로 되어있나? */
            return times[n-1];
        } else {
            n -= times.length; // 남은 사람들만 추려내고 
            // *2를 하고 제일 낮은놈처리하고, 처리했으면 *3 (곱하면서 n하나씩 제거)
            
            /*근데 [] 도 전체 곱하기를 하면 적용이 되나? */
            int[] newArray = TimeMaker(times);
            while (n!=0) {
                int least = newArray[0];
                int save = 0;
                for (int k=0; k<newArray.length; k++) { // 딱 하나 고르는과정 
                    if (least > newArray[k]) {
                        least = newArray[k];
                        save = k;
                    } else if (least == newArray[k] && times[k] < times[save])                      { 
                        save = k;        
                    } 
                    /*같은거 있을때? times[k]를 보면되겠네  
                    하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가
                    서 심사를 받을 수도 있습니다.
                     */
                }
                // newArray[k] = times[]  이거 3배, 나아가서 계속 배수는 어떻게만들지..                       여기서 막히네  각 k별로 다르게 하는거를 어떻게 저장해. Map? 
                n--;
            }
        }
        
        
        
        //answer는 있는 값을 더하기보다는 max 값을 계속 바꾸는 식으로 
        return answer;
    }
    
    public int[] TimeMaker(int[] whatever) { // 처음에만 해놓으면 나머지는 각각처리하면되니
        int[] newever = new int[whatever.length];
        for (int i=0; i<whatever.length;i++) {
            newever[i] = whatever[i]*2;
        }
        
        return newever;
    }
}
