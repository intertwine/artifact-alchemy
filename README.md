![Static Badge](https://img.shields.io/badge/Code_%26_Context-Exclusive-2980B9?labelColor=E67E22)
![Static Badge](https://img.shields.io/badge/AI_Drop-Week_2-2C3E50?labelColor=1ABC9C)

# ArtifactAlchemy

ArtifactAlchemy (aalc) is a command-line tool for processing and splitting concatenated Claude Artifacts into individual files.

This project is part of [Code & Context](https://codeandcontext.substack.com)'s [AI Drop of the Week](https://codeandcontext.substack.com/s/ai-drop-of-the-week).

## Installation

ArtifactAlchemy is available on macOS, Windows, and Linux. See the [User Guide](docs/user_guide.md) for installation instructions.

### Simple MacOS Homebrew Installation

```bash
brew tap intertwine/artifact-alchemy
brew install aalc
```

## Prompting Claude

In order to use ArtifactAlchemy, you must first prompt Claude to properly combine multiple
artifacts into a set of consolidated artifacts that you can copy and paste into a local text file for processing.

The following prompt works well on Claude 3.5 Sonnet:

````text
Claude, I need you to package the final versions of the artifacts you've created in this conversation
into a series of consolidated artifacts in markdown format that can be later processed by a text processing tool.

Please follow these instructions:

1. Create one consolidated markdown formatted artifact at a time, staying within your output limit.
2. Number each consolidated artifact sequentially (e.g., "Consolidated Artifacts 1", "Consolidated Artifacts 2", etc.).
3. For each individual artifact within a consolidated artifact, create a section with front matter and content.
4. Use "---" to separate the front matter from the content and to separate different artifacts.
5. In the front matter, include at least the "filename" field. Add other metadata fields if relevant.
6. Ensure that the content of each artifact is preserved exactly as it was created.
7. Do not split individual artifacts across multiple consolidated artifacts.
8. At the start of each consolidated artifact (before the first artifact), include a header indicating which consolidated artifact it is.
9. At the end of each consolidated artifact, indicate if there are more artifacts to follow.

Here's the structure to follow:

```
&lt;antArtifact identifier="consolidated-artifacts-X" type="text/markdown" title="Consolidated Artifacts X"&gt;
# Consolidated Artifacts X

---
filename: path/to/filename.ext
language: language_name
# Add any other relevant metadata fields here
---
Content of the artifact goes here,
preserving all formatting, line breaks,
and exact content.
---
filename: path/to/another_file.ext
language: another_language
---
Content of another artifact...
--- END OF CONSOLIDATED ARTIFACTS X ---
(More artifacts to follow / This is the final part)
&lt;/antArtifact&gt;
```

After creating each consolidated artifact:

1. Ask the user if they want you to continue with the next consolidated artifact.
2. If there are no more artifacts to package, inform the user that all artifacts have been processed.

Begin with creating Consolidated Artifacts 1. After you've reached a reasonable length (to avoid hitting your output limit), stop and ask to continue.

After all artifacts have been processed, provide this final instruction:
"All artifacts have been packaged. To use these with ArtifactAlchemy:
1. Save each consolidated artifact to a separate file (e.g., 'artifacts_1.md', 'artifacts_2.md', etc.)
2. Run ArtifactAlchemy on all the consolidated artifact files, pointing to the same output directory:

```sh
aalc artifacts_1.md artifacts_2.md artifacts_n.md output_folder
```

This will extract all artifacts to the specified output folder, maintaining their original structure."
````

## Usage

```bash
aalc <input_file_1> <input_file_2> <input_file_n> <output_directory>
```

- `<input_file_1>`, `<input_file_2>`, `<input_file_n>`: Paths to the concatenated markdown files containing artifacts
- `<output_directory>`: Directory where individual files will be created

## Example

```bash
aalc artifacts_1.md artifacts_2.md artifacts_n.md output_folder
```

## Features

- Processes markdown files with specially formatted artifacts
- Splits concatenated artifacts into individual files
- Preserves directory structure specified in artifact filenames
- Handles various file types and languages

## Contributing

Contributions are welcome! Please see our [Contributing Guide](docs/developer_guide.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
