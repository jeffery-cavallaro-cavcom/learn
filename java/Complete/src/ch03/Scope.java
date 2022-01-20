package ch03;

/**
 * Demonstrates the block scope of variables.
 */

public class Scope {
    public static void main(String [] args) {
        int x = 42;
        for (int i = 0; i < 5; ++i) {
            int y = 1;  // initialized on each iteration.
            System.out.println("i=" + i + " x=" + x + " y=" + y);
            y = 100;
            --x;
            System.out.println("i=" + i + " x=" + x + " y=" + y);
        }
        System.out.println("x=" + x);
    }
}
