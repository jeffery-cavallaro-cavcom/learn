package ch03;

/**
 * Creates and displays an array of 10 random integers and their average.
 */

import java.util.Random;

public class RandArray {
    private static final int NVALUES = 10;
    private static final int MAXVALUE = 100;

    private static Random randNumGen = new Random();

    public static void main(String [] args) {
        int [] values = new int[NVALUES];
        int sum = 0;
        for (int i = 0; i < values.length; ++i) {
            int value = randNumGen.nextInt(MAXVALUE);
            values[i] = value;
            sum += value;
        }
        for (int i : values) {
            System.out.println(i);
        }
        double average = ((double) sum) / values.length;
        System.out.println("Average = " + average);
    }
}
