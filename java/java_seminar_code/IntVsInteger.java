package one;

import java.util.function.Function;

public class IntVsInteger {
    public static void main(String[] args) {
        // AutoBoxing
        Integer case1 = 3;
        Integer case31 = 1200;

        Integer case2 = new Integer(3);

        boolean answer1 = (case1 == case2);
        System.out.println("answer1 = " + answer1);

        // false
        int case3 = 3;
        Integer case4 = 3;
        boolean answer2 = (case3 == case4);
        System.out.println("answer2 = " + answer2);

        // true
        Integer case5 = new Integer(3);
        Integer case6 = new Integer(3);
        boolean answer3 = (case5 == case6);
        System.out.println("answer3 = " + answer3);

        // false
        Integer case7 = 128;
        Integer case8 = 128;
        boolean answer4 = (case7 == case8);
        System.out.println("answer4 = " + answer4);


        // tue
        Integer case9 = 128;
        int case10 = 128;
        boolean answer5 = (case9 == case10);
        System.out.println("answer5 = " + answer5);
    }
}
