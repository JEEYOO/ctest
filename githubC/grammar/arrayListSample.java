package grammar;

import java.util.ArrayList;

public class arrayListSample {
	public static void main(String[] args)
    {
        ArrayList<Integer> arrayList = new ArrayList<>();
        ArrayList<Integer> arrayList2 = new ArrayList<>();
 
        arrayList.add(1);
        arrayList.add(2);
        arrayList.add(3);
 
        arrayList2.add(10);
        arrayList2.add(30);
        arrayList2.add(20);
 
        arrayList.addAll(arrayList2); // addAll에 대하여 
 
        for(int i : arrayList)
        {
            System.out.println(i);
        }
    }
}
