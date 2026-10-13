package demo;

import java.io.*;
import java.sql.*;
import java.util.*;
import java.security.MessageDigest;

public class BuggyService {

    public static String password = "admin123";
    private static final String SECRET = "sk_live_1234567890abcdef";
    public int counter;
    private List list = new ArrayList();

    public ResultSet findUser(Connection conn, String name) throws Exception {
        Statement st = conn.createStatement();
        return st.executeQuery("SELECT * FROM users WHERE name = '" + name + "'");
    }

    public String readFile(String path) throws IOException {
        FileInputStream in = new FileInputStream(path);
        byte[] b = new byte[1024];
        in.read(b);
        return new String(b);
    }

    public byte[] hash(String s) throws Exception {
        MessageDigest md = MessageDigest.getInstance("MD5");
        return md.digest(s.getBytes());
    }

    public boolean same(String a, String b) {
        return a == b;
    }

    public void swallow() {
        try {
            Object o = null;
            o.toString();
        } catch (Exception e) {
        }
    }

    public void catchThrowable() {
        try {
            System.out.println("x");
        } catch (Throwable t) {
            t.printStackTrace();
        }
    }

    public int risky(String s) {
        if (s.equals(null)) {
            return 0;
        }
        return Integer.parseInt(s);
    }

    public String concat(List<String> items) {
        String result = "";
        for (String i : items) {
            result += i;
        }
        return result;
    }

    public void unusedStuff() {
        int unused = 5;
        String s = "a";
        s = "b";
        System.out.println("done");
    }

    public synchronized void sync() {
        counter++;
    }

    public void duplicate1() {
        for (int i = 0; i < 10; i++) {
            System.out.println("value " + i);
        }
    }

    public void duplicate2() {
        for (int i = 0; i < 10; i++) {
            System.out.println("value " + i);
        }
    }

    public int nested(int x) {
        if (x > 0) {
            if (x > 1) {
                if (x > 2) {
                    if (x > 3) {
                        return 4;
                    }
                }
            }
        }
        return 0;
    }

    @Override
    public boolean equals(Object o) {
        return true;
    }

    public void leak() throws Exception {
        Connection c = DriverManager.getConnection("jdbc:mysql://localhost/db", "root", "root");
        c.createStatement();
    }
}
