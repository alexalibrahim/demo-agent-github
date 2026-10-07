package demo

import (
	"crypto/md5"
	"fmt"
	"os/exec"
)

// S2068: Hardcoded credential
const dbPassword = "go_hardcoded_secret_321"

// S4790: Weak hashing algorithm — MD5 is cryptographically broken
func hashValue(input string) string {
	h := md5.New()
	h.Write([]byte(input))
	return fmt.Sprintf("%x", h.Sum(nil))
}

// S4036: OS command injection — input passed directly to shell command
func runReport(userInput string) ([]byte, error) {
	cmd := exec.Command("sh", "-c", "report.sh "+userInput)
	return cmd.Output()
}
