package challengeKit;

public class Knumber {
	public int[] solution(int[] array, int[][] commands) {
        int a = commands.length;// 이중배열이니까 size인가?ㄴㄴㄴ length네?!
        int[] answer = new int[a]; // 어 이거 사이즈 안해줘도되나? add 는 안통하잖아 
        
        for (int h=0; h<a; h++) {
        	answer[h]=numMaker(array, commands[h]);
        }
        
        return answer;
    }
    
    public int numMaker(int[] list, int[] command) {
        int b = command[1]-command[0]+1; 
    	int[] temp = new int[b];
        // slice(command[0],command[1]+1); 앗 이거 없는데 ?
        for (int k=0; k<b; k++) { // 그럼 뭐 직접만들어야지 후비작 
        	temp[k] = list[command[0]-1+k]; 
        }
        // temp.sort();
        return temp[command[2]-1];
    }
}
