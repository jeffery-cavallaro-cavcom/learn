package ch02;

/**
 * A program to determine the distance sound travels for a given number of seconds.  Sound travels at a speed of about
 * 1100 ft/sec.  This can be used to determine how far away a lightening strike is by timing the number of seconds
 * between sighting the strike and hearing the thunder.  The number of seconds is specified on the command line.
 */

public class Sound {
    private final static double SPEED_OF_SOUND = 1100.0;  // ft/sec

    public static void main(String [] args) {
        if (args.length != 1) {
            System.out.println("Usage: Sound secs");
            return;
        }

        double secs;
        try {
            secs = Double.parseDouble(args[0]);
        }
        catch (NumberFormatException nfe) {
            System.out.println("Input error: " + nfe.getMessage());
            return;
        }

        double distance = secs * SPEED_OF_SOUND;
        System.out.println(distance + " feet");
    }
}
