package grammar;
import java.util.*;

public class binarySearch2 {

	private static int[] arr = {5,7,6,1,3,9,0,12,100};

	public static void main(String[] args) {
		//Arrays.sort(arr);
	
		for(int i=0;i<arr.length;i++) {
			System.out.print(arr[i]+"\t");
		}
		
		System.out.println();
		
		int a = Arrays.binarySearch(arr, 6);
		int b = Arrays.binarySearch(arr, 12);
		
		System.out.print("배열에서의 6과 12의 위치 : ");
		System.out.println(a +", "+ b);
	}
}


