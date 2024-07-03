---
filename: project/src/lib.rs
language: rust
---
pub mod math {
    pub fn add(a: i32, b: i32) -> i32 {
        a + b
    }

    pub fn subtract(a: i32, b: i32) -> i32 {
        a - b
    }
}

---
filename: project/tests/math_tests.rs
language: rust
---
use project::math;

#[test]
fn test_add() {
    assert_eq!(math::add(2, 3), 5);
}

#[test]
fn test_subtract() {
    assert_eq!(math::subtract(5, 3), 2);
}

---
filename: project/docs/API.md
language: markdown
---
# Math Module API

## Functions

### add(a: i32, b: i32) -> i32

Adds two integers and returns the result.

### subtract(a: i32, b: i32) -> i32

Subtracts the second integer from the first and returns the result.

---
filename: project/.gitignore
language: gitignore
---
/target
**/*.rs.bk
Cargo.lock