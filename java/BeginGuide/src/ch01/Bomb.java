package ch01;

public class Bomb {
    public static void main(String [] args) {
        for (int i = 10; i > 0; --i) {
            System.out.println(i);
            try {
                Thread.sleep(1000);
            }
            catch (InterruptedException ignored) {
            }
        }
        System.out.println("BOOM!");
    }
}
