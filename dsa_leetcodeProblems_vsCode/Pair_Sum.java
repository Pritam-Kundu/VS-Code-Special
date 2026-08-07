// BRUTE FORCE APPROACH

/*
public class Pair_Sum {
    public static void main(String[] args) {

        int[] arr = {2,7,11,13};
        int n = arr.length;
        int target = 13;

        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                if((arr[i]+arr[j]) == target){
                    System.out.println("The pair is: "+arr[i]+" & " + arr[j]);
                }  
            }
        }
    }
}

*/


// OPTIMAL APPROACH(Works only for sorted array)

public class Pair_Sum {
    public static void main(String[] args) {
        
        int[] arr = {2,7,11,13};
        int n = arr.length;
        int target = 24;
        int i=0;
        int j = n-1;

        while(i<j){
            int ps = arr[i] + arr[j];

            if(ps > target){
                j--;
            }
            else if(ps < target){
                i++;
            }
            else{
                System.out.println("The pair is: "+arr[i]+" & "+arr[j]);
                break;
            }
        }
    }
}