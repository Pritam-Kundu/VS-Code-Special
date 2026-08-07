
// BRUTE FORCE APPROACH [O(n^2)]
/* 
public class Majority_Element {
    public static void main(String[] args) {
        int[] nums = {1,2,2,1,1,2,3,3,3,3,3,3,3};
        int n = nums.length;

        for(int i=0;i<n;i++){
            int freq = 0;
            for(int f=0;f<n;f++){
                if(nums[i] == nums[f]){
                    freq++;
                }
            }
            if(freq > (n/2)){
                System.out.println("Majority element is: "+nums[i]);
                break;
            }
        }
    }
}
*/





// OPTIMIZED APPROACH [O(nlogn)]

import java.util.Arrays;

public class Majority_Element {

    public static void main(String[] args) {
        int[] nums = {1,2,2,1,1,2,3,3,3,3,3,3,3};
        Arrays.sort(nums);
        int n = nums.length;
        int freq = 0;
        int ans = nums[0];

        for(int i=1; i<n; i++){
            if(nums[i] == nums[i-1]){
                freq++;
            }
            else{
                freq = 1;
                ans = nums[i];
            }

            if(freq > n/2){
                System.out.println("Majority Element is:"+ans);
                break;
            }

        }
    }
}