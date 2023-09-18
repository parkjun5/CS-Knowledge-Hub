package one;

import java.util.HashMap;

public class CalculatorTest {

    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        int add = calculator.add(1, 2);

        int d = calculator.add(1, Integer.MAX_VALUE);
        boolean b = d == Integer.MIN_VALUE;
        System.out.println("d == Integer.MIN_VALUE = " + b );
        System.out.println("d = " + d);
        HashMap<String, Integer> stringIntegerHashMap = new HashMap<>(100, 0.8f);
    }


    static class Calculator {
        int add(int a, int b) {
            return a + b;
        }
    }
}