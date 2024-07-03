# Release Guide

## 0.1.0 (2024-07-02)

Instructions for compiling the project for macOS (Intel and Apple Silicon),
Windows, and Linux.

## MacOS

```bash
# Add the target architectures
rustup target add aarch64-apple-darwin
rustup target add x86_64-apple-darwin

# Compile For Intel
cargo build --release --target x86_64-apple-darwin

# Compile for Apple Silicon
cargo build --release --target aarch64-apple-darwin

# Create a universal binary
mkdir -p target/universal-apple-darwin/release

lipo -create -output target/universal-apple-darwin/release/aalc \
    target/x86_64-apple-darwin/release/aalc \
    target/aarch64-apple-darwin/release/aalc

# Verify the binary
lipo -info target/universal-apple-darwin/release/aalc
# (Should return something like "Architectures in the fat file: target/universal-apple-darwin/release/aalc are: x86_64 arm64")

# Package the binary
zip releases/aalc-macos-universal.zip ./target/universal-apple-darwin/release/aalc 
```

## Windows

```bash
# (Optional - when building from MacOS)
brew install mingw-w64

# Add the target architecture
rustup target add x86_64-pc-windows-gnu

cargo build --release --target x86_64-pc-windows-gnu

zip releases/aalc-windows.zip ./target/x86_64-pc-windows-gnu/release/aalc.exe
```

## Linux

```bash
# (Optional - when building from MacOS)
docker run -it --platform linux/amd64 -v $(pwd)/:alchemy rust:latest
> cd alchemy
> cargo build --release --target x86_64-unknown-linux-gnu
> exit

# Add the target architecture (skip if using Docker from optional step above)
# rustup target add x86_64-unknown-linux-gnu
# cargo build --release --target x86_64-unknown-linux-gnu

# Package the binary
tar -czvf releases/aalc-linux.tar.gz ./target/x86_64-unknown-linux-gnu/release/aalc
```
