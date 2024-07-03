# ArtifactAlchemy User Guide

ArtifactAlchemy (aalc) is a command-line tool for processing and splitting
concatenated Claude Artifacts into individual files.

## MacOS Install (Homebrew)

```bash
brew tap intertwine/artifactalchemy
brew install aalc
```

## MacOS Installation (Binary Download)

1. Download the `aalc-macos.zip` file from the [releases directory](https://github.com/intertwine/artifact-alchemy/releases/download/v0.1.0/aalc-macos.zip).
2. Unzip the file:

   ```sh
   unzip aalc-macos.zip
   ```

3. Move the binary to a directory in your PATH, e.g.:

   ```sh
   mv aalc /usr/local/bin/
   ```

4. Run the application:

   ```sh
   aalc --help
   ```

## Windows Installation (Binary Download)

1. Download the `aalc-windows.zip` file from the [releases directory](https://github.com/intertwine/artifact-alchemy/releases/download/v0.1.0/aalc-windows.zip).
2. Unzip the file using File Explorer or PowerShell:

   ```powershell
   Expand-Archive -Path aalc-windows.zip -DestinationPath C:\path\to\destination
   ```

3. Add the destination directory to your PATH:

   - Open System Properties -> Environment Variables -> Edit the PATH variable
   - Add the directory where `aalc.exe` is located

4. Run the application:

   ```cmd
   aalc --help
   ```

## Linux Installation (Binary Download)

1. Download the `aalc-linux.tar.gz` file from the [releases directory](https://github.com/intertwine/artifact-alchemy/releases/download/v0.1.0/aalc-linux.tar.gz).
2. Extract the file:

   ```sh
   tar -xzvf aalc-linux.tar.gz
   ```

3. Move the binary to a directory in your PATH, e.g.:

   ```sh
   sudo mv aalc /usr/local/bin/
   ```

4. Run the application:

   ```sh
   aalc --help
   ```

## Manual Installation (Rust / Cargo)

1. Ensure you have Rust installed on your system. If not, visit <https://www.rust-lang.org/tools/install> for installation instructions.

2. Install ArtifactAlchemy using cargo:

```bash
cargo install artifact-alchemy
```

## Usage

The basic syntax for using ArtifactAlchemy is:

```bash
aalc <input_file> <output_directory>
```

- `<input_file>`: Path to the concatenated markdown file containing artifacts
- `<output_directory>`: Directory where individual files will be created

Example:

```bash
aalc artifacts.md output_folder
```

## Input File Format

Your input file should be a markdown file with the following structure for each artifact:

```markdown
---
filename: path/to/filename.ext
language: language_name
---

Content of the artifact goes here,
preserving all formatting, line breaks,
and exact content.

---
```

## Output

ArtifactAlchemy will create individual files in the specified output directory, preserving the directory structure specified in the filenames.

## Tips

- Ensure your input file follows the correct format for each artifact.
- The output directory will be created if it doesn't exist.
- Existing files in the output directory with the same names will be overwritten.

## Troubleshooting

If you encounter any issues:

1. Ensure your input file is correctly formatted.
2. Check that you have write permissions in the output directory.
3. Verify that the filenames in your artifacts are valid for your operating system.

For more help, please open an issue on our GitHub repository.
