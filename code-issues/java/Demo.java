package demo;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class Demo {

    // S2068: Hardcoded credential
    private static final String DB_PASSWORD = "SuperSecret123!";

    // S2189: Infinite loop — loop condition never changes
    public void infiniteLoop() {
        boolean running = true;
        while (running) {
            System.out.println("looping");
            // running is never set to false
        }
    }

    // S2077: SQL injection — user input concatenated directly into query
    public ResultSet getUser(String userId) throws Exception {
        Connection conn = DriverManager.getConnection("jdbc:h2:mem:test", "sa", DB_PASSWORD);
        Statement stmt = conn.createStatement();
        return stmt.executeQuery("SELECT * FROM users WHERE id = '" + userId + "'");
    }
}
