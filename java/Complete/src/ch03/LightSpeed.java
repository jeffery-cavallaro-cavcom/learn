package ch03;

/**
 * Calculates the distance (in miles) that light can travel in a given number
 * of days.  The number of days is obtained from the command line and defaults
 * to 1.
 */

public class LightSpeed {
    private static final long SECS_PER_DAY = 86400;
    private static final long C_MILES_PER_SEC = 186_000;
    private static final long DEFAULT_DAYS = 1;

    private static long getDays(String [] args) {
        long days = DEFAULT_DAYS;
        if (args.length > 0) {
            try {
                days = Long.valueOf(args[0]);
            }
            catch (NumberFormatException error) {
                System.err.println(
                    "Invalid days value, using " + DEFAULT_DAYS
                );
                days = DEFAULT_DAYS;
            }
        }
        return days;
    }

    public static void main(String [] args) {
        long days = getDays(args);
        long miles = days * SECS_PER_DAY * C_MILES_PER_SEC;
        System.out.println(
            "In " + days + " day(s) light travels about " + miles + " miles"
        );
    }
}
