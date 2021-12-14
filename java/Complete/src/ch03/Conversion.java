package ch03;

/**
 * Demonstrates explicit narrowing conversions.
 */

public class Conversion {
    public static void main(String [] args) {
        int i = 1000;
        byte b = (byte) i;  // 1000-4*256=-24
        System.out.println("i=" + i + ", b=" + b);

        i = -1000;
        b = (byte) i;  // -1000+4*256=24
        System.out.println("i=" + i + ", b=" + b);

        double d = 3.14;
        i = (int) d;  // 3
        System.out.println("d=" + d + ", i=" + i);
    }
}
