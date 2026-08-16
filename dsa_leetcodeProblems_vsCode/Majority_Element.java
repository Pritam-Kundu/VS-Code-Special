
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
/* 
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
*/



// Moore's Voting Algorithm [O(n)]

import java.util.*;

public class Majority_Element {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter size of the array:");
        int n = sc.nextInt();
        int[] nums = new int[n];

        // int[] nums = {1,2,3,1,3,2,3,3,3};
        for(int i=0;i<n;i++){
            nums[i] = sc.nextInt();
        }

        int freq = 0, ans = 0;
        for(int i=0;i<n;i++){
            if(freq == 0){
                ans = nums[i];
            }
            if (ans == nums[i]){
                freq++;
            }
            else{
                freq--;
            }
        }
        System.out.println("Majority element is:"+ans);

        //Chekcing whether the majority element exists or not
        // int count=0;
        // for(int i=0;i<n;i++){
        //     if(nums[i] == ans){
        //         count++;
        //     }
        // }
        // if(count > n/2){
        //     return ans;
        // }
        // else{
        //     return -1;
        // }
    }
}