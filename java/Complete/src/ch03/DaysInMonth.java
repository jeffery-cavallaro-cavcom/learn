package ch03;

/**
 * Displays the number of days in each month.
 */

public class DaysInMonth {
    private static class MonthDays {
        private String name;
        private int days;

        public MonthDays(String name, int days) {
            this.name = name;
            this.days = days;
        }

        public String getName() {
            return name;
        }

        public int getDays() {
            return days;
        }
    }

    private static final MonthDays [] daysInMonth = {
        new MonthDays("January", 31),
        new MonthDays("February", 28),
        new MonthDays("March", 31),
        new MonthDays("April", 30),
        new MonthDays("May", 31),
        new MonthDays("June", 30),
        new MonthDays("July", 31),
        new MonthDays("August", 31),
        new MonthDays("September", 30),
        new MonthDays("October", 31),
        new MonthDays("November", 30),
        new MonthDays("December", 31)
    };

    public static void main(String [] args) {
        for (MonthDays month : daysInMonth) {
            System.out.println(
                month.getName() + " has " + month.getDays() + " days"
            );
        }
    }
}
