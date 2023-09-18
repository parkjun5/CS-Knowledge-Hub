package one;

public class newTest {
    public synchronized static void pong() {
        System.out.println("PONG: " + Thread.currentThread().getName());
    }
}
