package empty;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Main {
	  
	  public static int count = 0;
	
	  private static void solution(int sizeOfMatrix, int[][] matrix) {
		  	// 다른 거 찾아야하나?
		  
			// 구름이라는 곳은 있는 거를 쓰는 거도 테스트의 일부인가봉가 
			int temp = 0; // 각 영역의 크기  ... what is this for? 
			boolean[][] visited = new boolean[sizeOfMatrix][sizeOfMatrix];
			// 사실 이 문제는 전부 다 1이어서 더 쉽지
			ArrayList<Integer> answers = new ArrayList<>();
			for (int i=0; i<sizeOfMatrix; i++) {
				for (int k=0; k<sizeOfMatrix; k++) {
					if(matrix[i][k]==1) { //0,1 이 1이라면 
						findPath(i,k,matrix,visited); // 여기 
						if (count > 0) {
							answers.add(count);
							count =0;
						}
					}
					
				}
			} 
			
			int c = answers.size();
			if (c==0) {
				System.out.println(0); // 아 여기는 return 이 아니구만. void 이기도 하고 '출력'이라는 단어를 썼고 
			} else {
				Collections.sort(answers);
				System.out.println(c); 			// 할 때 예쁘게 크기
				System.out.print(answers.get(0));
				for (int m=1; m<c; m++) {//      딱 영역 하나하나씩 	<> 아니면 answers 안에 갯수도 넣어야하나?  \n 으로 값을 나누든 뭐든?
					System.out.print(" " +answers.get(m)); 
					// 아 마지막 띄어쓰기 때문에 [0] 하고   " [m]" 이 낫겠다. 
				}
			}
			

				                 
	  }
	  
	  public static void findPath(int a, int b, int[][] zerone, boolean[][] whatever) {
		  if (whatever[a][b]==true) { // 스타트가 좀 이상한데? 
			  return; // 아 여기서 멈춰야하는거아닌가? 
		  } else {
		  
		  int leng = zerone.length; 
		  
		  
		  whatever[a][b] = true; // 0 0
		  count++; // count 1
		  
		  // 오른
		  if ((a+1 < leng) && (whatever[a+1][b]==false && zerone[a+1][b] ==1)){ // 1,1
			  findPath(a+1, b, zerone, whatever);
		  }
		  
		  // 왼 
		  if ((b-1 >= 0) && (whatever[a][b-1]==false && zerone[a][b-1] ==1)){ // 여기 
			  findPath(a, b-1, zerone, whatever);
		  }
		  
		  // 위 
		  if ((a-1 >= 0) && (whatever[a-1][b]==false && zerone[a-1][b] ==1)){
			  findPath(a-1, b, zerone, whatever);
		  }
		  
		  // 아래 
		  if ((b+1 < leng) && (whatever[a][b+1]==false && zerone[a][b+1] ==1)){
			  findPath(a, b+1, zerone, whatever); // 여기 
		  }
		  
		  // return 하는 것은 없다. span 만을 남길뿐  
		  // 애당초 void 이기도 하
		  }
	  }
	  
	  // 심지어 이것도 어차피 solution의 (parameter) 는 가변적 
	  private static class InputData {
	    int sizeOfMatrix;
	    int[][] matrix;
	  }

	  
      // 이건 신경안써도되고 (고정) 걍 다 신경안써도되네 	  
	  

	  private static InputData processStdin() {
	    InputData inputData = new InputData();

	    try (Scanner scanner = new Scanner(System.in)) {
	      inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));      
	      
	      inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
	      for (int i = 0; i < inputData.sizeOfMatrix; i++) {
	        String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
	        for (int j = 0; j < inputData.sizeOfMatrix; j++) {
	          inputData.matrix[i][j] = Integer.parseInt(buf[j]);
	        }
	      }
	    } catch (Exception e) {
	      throw e;
	    }

	    return inputData;
	  }

	  public static void main(String[] args) throws Exception {
	    
		InputData inputData = processStdin();
		
	    solution(inputData.sizeOfMatrix, inputData.matrix);
	    /*
		Main solution = new Main();  
		int n = 6;
		int[][] picture = {
				{0,1,1,0,0,0},
				{0,1,1,0,1,1},
				{0,0,0,0,1,1},
				{0,0,0,0,1,1},
				{1,1,0,0,1,0},
				{1,1,1,0,0,0},
		};
		solution(n, picture);
		*/
	  }
}