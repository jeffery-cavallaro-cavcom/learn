package ch01;

/**
 * Performs a countdown from 10.
 */

public class Bomb {
    public static void main(String [] args) {
        try {
            for (int i = 10; i > 0; --i) {
                System.out.println(i);
                Thread.sleep(1000);
            }
        }
        catch (InterruptedException ie) {
            System.err.println("Interrupted");
        }
        System.out.println("BOOM !!!");
    }
}
