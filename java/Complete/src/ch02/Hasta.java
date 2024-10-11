package ch02;

/**
 * Demonstrates unicode characters.
 */

public class Hasta {
    public static void main(String [] args) {
        char [] text = {
            0xA1, 'H', 'a', 's', 't', 'a', ' ',
            'M', 'a', 0xF1, 'a', 'n', 'a', '!'
        };

        for (char c : text) {
            System.out.print(c);
        }
        System.out.println();
    }
}
