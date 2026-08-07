/* BRUTE FORCE APPROACH


public class Maximum_Subarray_Sum {
    public static void main(String[] args) {

        int arr[] = { 3, -4, 5, 4, -1, 7, -8 };
        int start, end;
        int n = arr.length;

        int max_sum = 0;

        for (start = 0; start < n; start++) {
            int current_sum = 0;                // Reset for every new start index
            for (end = start; end < n; end++) {

                current_sum += arr[end];
                if (current_sum > max_sum) {
                    max_sum = current_sum;
                }

            }

        }

        System.out.println("Maximum subarray sum: " + max_sum);

    }
}

*/



//KADANE'S ALGORITHM


public class Maximum_Subarray_Sum{
    public static void main(String[] args) {
        int arr[] = { 3, -4, 5, 4, -1, 7, -8 };
        int n = arr.length;
        int max_sum = Integer.MIN_VALUE;
        int current_sum = 0;

        for(int i=0;i<n;i++){
            current_sum += arr[i];

            max_sum = Math.max(current_sum, max_sum);

            if(current_sum < 0){
                current_sum = 0;
            }

        }
        System.out.println("Maximum subarray sum is: "+max_sum);

    }
}