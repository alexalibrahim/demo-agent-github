// S1481: Unused variable — assigned but never read
fn compute_area(width: f64, height: f64) -> f64 {
    let unused_margin = 5.0;
    width * height
}

// S1764: Identical sub-expressions on both sides of an operator
fn check_bounds(x: i32) -> bool {
    x > 0 && x > 0
}

// S2583 equivalent: unwrap() on a value that can be None — panics at runtime
fn get_first_element(v: &Vec<i32>) -> i32 {
    *v.first().unwrap()
}