import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Sample {
   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

      // int[] rollNo = new int[5];
      // rollNo[0] = 10;
      // rollNo[1] = 20;
      // rollNo[2] = 30;
      // rollNo[3] = 40;
      // rollNo[4] = 50;
      // System.out.println(rollNo[3]);

      // int[] rollNo = new int[]{10,20,30,40};

      // int[] roll = {10,20,30,40,50};
      // System.out.println(roll[3]);

      // int[] arr = new int[5];
      // // input
      // for (int i = 0; i < (arr.length); i++) {
      // arr[i] = Integer.parseInt(br.readLine());
      // }
      // output
      // for(int i=0;i<(arr.length);i++){
      // System.out.println(i+"th element: "+arr[i]);
      // }
      // for(int num : arr){
      // System.out.println(num);
      // }

      // System.out.println(Arrays.toString(arr));

      int[] nums = { 10, 20, 30, 40, 50 };
      System.out.println(Arrays.toString(nums));
      change(nums);
      System.out.println(Arrays.toString(nums));
   }

   static void change(int[] arr) {
      arr[0] = 90;
   }
}