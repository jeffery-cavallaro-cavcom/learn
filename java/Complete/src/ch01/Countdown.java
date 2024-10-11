package ch01;

/**
 * Performs a countdown from 10 to 0.
 */

public class Countdown {
    public static void main(String [] args) {
        for (int i = 10; i > 0; --i) {
            System.out.println(i);
            try {
                Thread.sleep(1000);
            }
            catch (InterruptedException ie) {}
        }
        System.out.println("BOOM !!!");
    }
}
