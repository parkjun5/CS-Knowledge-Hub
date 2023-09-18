package one;

import static one.newTest.pong;

public class ThreadSyncronized {
    public synchronized static void main(String[] args) {
        Thread thread = new Thread() {
            public void run() {
                pong();
            }
        };
        thread.start();
        System.out.println("PING: "  + Thread.currentThread().getName());
    }
}
