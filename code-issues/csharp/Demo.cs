using System;
using System.Data.SqlClient;

namespace Demo
{
    public class Demo
    {
        // S2068: Hardcoded credential
        private const string Password = "csharp_secret_pass!";

        // S1144: Private method declared but never used
        private void UnusedPrivateMethod()
        {
            Console.WriteLine("This method is never called");
        }

        // S2077: SQL injection — user input concatenated into query string
        public void GetUser(string userId)
        {
            using var conn = new SqlConnection("Server=.;Database=app;Password=" + Password);
            conn.Open();
            var cmd = new SqlCommand("SELECT * FROM Users WHERE Id = '" + userId + "'", conn);
            cmd.ExecuteReader();
        }
    }
}
