package demo

// S2068: Hardcoded credential
val DB_PASSWORD = "kotlin_secret_pass!"

// S1481: Unused local variable
fun calculateDiscount(price: Double): Double {
    val unusedTaxRate = 0.15
    return price * 0.9
}

// S6511: Kotlin Elvis operator used with `throw` where a simple null check suffices,
// and exception type is too broad — throws Exception instead of a specific type
fun findUser(id: String?): String {
    return id ?: throw Exception("id must not be null")
}
