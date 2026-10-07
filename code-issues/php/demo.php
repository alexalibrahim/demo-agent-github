<?php

// S1192: String literal duplicated more than 3 times
function logEvents(): void {
    echo "Event received";
    echo "Event received";
    echo "Event received";
    echo "Event received";
}

// S1481: Unused local variable
function calculateTax(float $price): float {
    $unusedRate = 0.05;
    return $price * 0.2;
}

// S3776: Cognitive complexity too high — deeply nested conditions
function evaluate($a, $b, $c, $d, $e): bool {
    if ($a) {
        if ($b) {
            if ($c) {
                if ($d) {
                    if ($e) {
                        if ($a && $b) {
                            return true;
                        }
                    }
                }
            }
        }
    }
    return false;
}
