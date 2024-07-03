# ArtifactAlchemy

ArtifactAlchemy (aalc) is a command-line tool for processing and splitting concatenated Claude Artifacts into individual files.

## Installation

See the [User Guide](docs/user_guide.md) for installation instructions.

## Prompting Claude

In order to use ArtifactAlchemy, you must first prompt Claude to properly combine multiple
artifacts into a single artifact that you can copy and paste into a local text file for processing.

The following prompt works well on Claude 3.5 Sonnet:

````text
Claude, I need you to package all the artifacts you've created in this conversation into a single markdown file
that can be processed by a text processing tool. Please follow these instructions:

1. Combine all artifacts into a single markdown document.
2. For each artifact, create a section with front matter and content.
3. Use "---" to separate the front matter from the content and to separate different artifacts.
4. In the front matter, include at least the "filename" field. You can add other metadata fields if relevant.
5. Ensure that the content of each artifact is preserved exactly as it was created.
6. Do not include any explanatory text or comments outside of the artifact sections.

Here's the structure to follow for each artifact:

```markdown
---
filename: path/to/filename.ext
language: language_name
# Add any other relevant metadata fields here
---
Content of the artifact goes here,
preserving all formatting, line breaks,
and exact content.

---
```

Please package all artifacts from our conversation using this format. After packaging, provide the entire markdown content in a single code block, without any additional commentary.
````

## Usage

```bash
aalc <input_file> <output_directory>
```

- `<input_file>`: Path to the concatenated markdown file containing artifacts
- `<output_directory>`: Directory where individual files will be created

## Example

```bash
aalc artifacts.md output_folder
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
