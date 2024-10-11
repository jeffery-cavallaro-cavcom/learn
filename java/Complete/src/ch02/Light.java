package ch02;

/**
 * Calculates the distance traveled in  vacuum by light in 1000 days.
 */

public class Light {
    public static void main(String [] args) {
        int speed = 186000;  // miles per second
        int days = 1000;
        long seconds = days*24*60*60;
        long distance = speed*seconds;

        System.out.println(
            "Light travels " + distance + " miles in " + days + " days."
        );
    }
}
