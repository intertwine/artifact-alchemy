---
filename: src/main.rs
language: rust
---
fn main() {
    println!("Hello from the main function!");
    greet("World");
}

fn greet(name: &str) {
    println!("Hello, {}!", name);
}

---
filename: tests/test_greet.rs
language: rust
---
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_greet() {
        // This test is just a placeholder
        assert!(true);
    }
}

---
filename: README.md
language: markdown
---
# Complex Project Example

This is an example of a more complex project structure using ArtifactAlchemy.

## Files

- `src/main.rs`: Main Rust source file
- `tests/test_greet.rs`: Test file for the greet function
- `config.json`: Configuration file

## Usage

Compile and run the main.rs file to see the greeting.

---
filename: config.json
language: json
---
{
  "greeting": "Hello",
  "default_name": "World"
}