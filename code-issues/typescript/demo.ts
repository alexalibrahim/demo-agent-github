// S2068: Hardcoded credential
const API_SECRET: string = "my_api_secret_key_789";

// S4325: Type assertion that removes undefined/null — bypasses type safety
function getLength(value: string | undefined): number {
    return (value as string).length;
}

// S3358: Nested ternary operators — hard to read and error-prone
function classify(score: number): string {
    return score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : score >= 60 ? "D" : "F";
}

export { getLength, classify };
