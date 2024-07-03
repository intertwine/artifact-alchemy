# ArtifactAlchemy Developer Guide

This guide is for developers who want to contribute to or extend ArtifactAlchemy.

## Project Structure

```text
artifact-alchemy/
├── src/
│   ├── main.rs
│   └── lib.rs
├── tests/
│   ├── integration_tests.rs
│   └── test_data/
├── docs/
├── scripts/
└── examples/
```

## Setting Up the Development Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/intertwine/artifact-alchemy.git
   cd artifact-alchemy
   ```

2. Build the project:

   ```bash
   cargo build
   ```

3. Run tests:

   ```bash
   cargo test
   ```

4. (Optional) Test the LLM prompt:

   ```bash
   python scripts/test_claude_prompt.py
   ```

## Making Contributions

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, concise commit messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## Coding Standards

- Follow the Rust style guide.
- Write unit tests for new functionality.
- Update documentation as necessary.

## Running Tests

- Run unit tests: `cargo test`
- Run integration tests: `cargo test --test integration_tests`

## Building Documentation

Generate documentation:

```bash
cargo doc --open
```

## Releasing New Versions

1. Update the version number in `Cargo.toml`.
2. Update the CHANGELOG.md file.
3. Commit these changes.
4. Tag the commit with the new version number.
5. Push the changes and the tag to GitHub.
6. Publish to crates.io: `cargo publish`

## Getting Help

If you need help or want to discuss development, please open an issue on GitHub.

Thank you for contributing to ArtifactAlchemy!
