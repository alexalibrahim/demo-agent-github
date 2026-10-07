// S2068: Hardcoded password
const DB_PASSWORD = "hardcoded_secret_456";

// S1854: Dead store — value assigned but never used before reassignment
function processOrder(order) {
    let total = 0;
    total = order.price * order.quantity;  // first assignment is dead
    total = order.price * order.quantity * 1.1;
    return total;
}

// S3776: Cognitive complexity too high — deeply nested conditions
function evaluate(a, b, c, d, e) {
    if (a) {
        if (b) {
            if (c) {
                if (d) {
                    if (e) {
                        if (a && b) {
                            if (c || d) {
                                return true;
                            }
                        }
                    }
                }
            }
        }
    }
    return false;
}

module.exports = { processOrder, evaluate };
