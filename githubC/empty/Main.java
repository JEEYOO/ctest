package empty;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Main {
	  
	  public static int count = 0;
	
	  private static void solution(int sizeOfMatrix, int[][] matrix) {
		  	
		  
			
			int temp = 0; 
			boolean[][] visited = new boolean[sizeOfMatrix][sizeOfMatrix];
			
			ArrayList<Integer> answers = new ArrayList<>();
			for (int i=0; i<sizeOfMatrix; i++) {
				for (int k=0; k<sizeOfMatrix; k++) {
					if(matrix[i][k]==1) { 
						findPath(i,k,matrix,visited); 
						if (count > 0) {
							answers.add(count);
							count =0;
						}
					}
					
				}
			} 
			
			int c = answers.size();
			if (c==0) {
				System.out.println(0); 
			} else {
				Collections.sort(answers);
				System.out.println(c); 			
				System.out.print(answers.get(0));
				for (int m=1; m<c; m++) {
					System.out.print(" " +answers.get(m)); 
					
				}
			}
			

				                 
	  }
	  
	  public static void findPath(int a, int b, int[][] zerone, boolean[][] whatever) {
		  if (whatever[a][b]==true) { 
			  return; 
		  } else {
		  
		  int leng = zerone.length; 
		  
		  
		  whatever[a][b] = true; 
		  count++; 
		  
		  // right
		  if ((a+1 < leng) && (whatever[a+1][b]==false && zerone[a+1][b] ==1)){ // 1,1
			  findPath(a+1, b, zerone, whatever);
		  }
		  
		  // left
		  if ((b-1 >= 0) && (whatever[a][b-1]==false && zerone[a][b-1] ==1)){ 
			  findPath(a, b-1, zerone, whatever);
		  }
		  
		  // upper
		  if ((a-1 >= 0) && (whatever[a-1][b]==false && zerone[a-1][b] ==1)){
			  findPath(a-1, b, zerone, whatever);
		  }
		  
		  // down
		  if ((b+1 < leng) && (whatever[a][b+1]==false && zerone[a][b+1] ==1)){
			  findPath(a, b+1, zerone, whatever); // 여기 
		  }
		  
		  // There is no return. Only span will be remained
		  
		  }
	  }
	  
	  
	  private static class InputData {
	    int sizeOfMatrix;
	    int[][] matrix;
	  }

	  
      
	  

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
