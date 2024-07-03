"""
This script tests the response from the Claude prompt.
"""

import unittest
import re
import os


class ClaudePromptTester(unittest.TestCase):
    """
    This class tests the response from the Claude prompt.
    """

    def setUp(self):
        """
        This method sets up the test case.
        """
        # Ensure the file path is correct
        file_path = os.path.join(os.path.dirname(__file__), "response.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            self.simulated_claude_response = file.read()

        self.simulated_claude_responses = [
            """
```markdown
# Consolidated Artifacts 1

---
filename: test1.py
language: python
---
def hello_world():
    print("Hello, World!")

---
filename: docs/README.md
language: markdown
---
# Project Documentation

This is a sample README file.

--- END OF CONSOLIDATED ARTIFACTS 1 ---
(More artifacts follow in the next part)
```
""",
            """
```markdown
# Consolidated Artifacts 2

---
filename: src/main.rs
language: rust
---
fn main() {
    println!("Hello from Rust!");
}

--- END OF CONSOLIDATED ARTIFACTS 2 ---
(This is the final part)
```

To use these packaged files with ArtifactAlchemy:
1. Save the content of each consolidated file to separate files (e.g., 'artifacts_1.md', 'artifacts_2.md', etc.)
2. Run ArtifactAlchemy on each file: aa artifacts_1.md output_folder, aa artifacts_2.md output_folder, etc.
3. All artifacts will be extracted to the same output folder, maintaining their original directory structure.
"""
        ]

    def test_artifact_structure(self):
        """
        This method tests the structure of the artifacts in the response.
        """
        content = self.simulated_claude_response.strip()
        markdown_block = re.search(r"```markdown\n(.*?)\n```", content, re.DOTALL)
        self.assertIsNotNone(markdown_block, "Markdown code block not found")

        markdown_content = markdown_block.group(1).strip()
        artifacts = re.split(r"\n---\n(?=filename:)", markdown_content)

        for artifact in artifacts:
            artifact = artifact.strip()
            if artifact.startswith("---"):
                artifact = artifact[3:].strip()

            # Debug print to check the artifact content
            print(f"Artifact: {artifact}")

            try:
                # Adjust the splitting pattern to handle the front matter correctly
                front_matter_match = re.match(
                    r"(filename: .*\nlanguage: .*)\n---\n(.*)", artifact, re.DOTALL
                )
                self.assertIsNotNone(
                    front_matter_match,
                    f"Artifact does not match expected format: {artifact}",
                )
                front_matter = front_matter_match.group(1).strip()
                content = front_matter_match.group(2).strip()
            except ValueError as e:
                print(f"Error splitting artifact: {artifact}")
                raise e

            # Debug print to check the front matter and content
            print(f"Front matter: {front_matter}")
            print(f"Content: {content}")

            self.assertIn(
                "filename:",
                front_matter,
                f"Front matter should contain filename: {front_matter}",
            )
            self.assertIn(
                "language:",
                front_matter,
                f"Front matter should contain language: {front_matter}",
            )
            self.assertTrue(content.strip(), f"Content should not be empty: {artifact}")

    def test_markdown_code_block(self):
        """
        This method tests if the response contains a markdown code block.
        """
        self.assertIn("```markdown", self.simulated_claude_response)
        self.assertIn("```", self.simulated_claude_response)

    def test_usage_instructions(self):
        """
        This method tests if the response contains usage instructions.
        """
        self.assertIn(
            "To use this packaged file with ArtifactAlchemy:",
            self.simulated_claude_response,
        )
        self.assertIn(
            "1. Save the content above to a file", self.simulated_claude_response
        )
        self.assertIn("2. Run ArtifactAlchemy:", self.simulated_claude_response)

    def test_consolidated_structure(self):
        """
        This method tests the structure of the consolidated artifacts in the response.
        """
        for i, response in enumerate(self.simulated_claude_responses, 1):
            content = response.strip()
            markdown_block = re.search(r"```markdown\n(.*?)\n```", content, re.DOTALL)
            self.assertIsNotNone(
                markdown_block,
                f"Markdown code block not found in Consolidated Artifacts {i}",
            )

            markdown_content = markdown_block.group(1).strip()
            self.assertTrue(
                markdown_content.startswith(f"# Consolidated Artifacts {i}"),
                f"Consolidated Artifacts {i} should start with the correct header",
            )

            artifacts = re.split(r"\n---\n(?=filename:)", markdown_content)

            for artifact in artifacts[1:]:  # Skip the header
                if "END OF CONSOLIDATED ARTIFACTS" in artifact:
                    continue

                artifact = artifact.strip()
                front_matter_match = re.match(
                    r"(filename: .*\nlanguage: .*)\n---\n(.*)", artifact, re.DOTALL
                )
                self.assertIsNotNone(
                    front_matter_match,
                    f"Artifact does not match expected format: {artifact}",
                )
                front_matter = front_matter_match.group(1).strip()
                content = front_matter_match.group(2).strip()

                self.assertIn(
                    "filename:",
                    front_matter,
                    f"Front matter should contain filename: {front_matter}",
                )
                self.assertIn(
                    "language:",
                    front_matter,
                    f"Front matter should contain language: {front_matter}",
                )
                self.assertTrue(
                    content.strip(), f"Content should not be empty: {artifact}"
                )

            self.assertIn(
                f"--- END OF CONSOLIDATED ARTIFACTS {i} ---",
                markdown_content,
                f"Consolidated Artifacts {i} should have a proper ending",
            )

    def test_final_instructions(self):
        """
        This method tests if the response contains final instructions.
        """
        final_response = self.simulated_claude_responses[-1]
        self.assertIn(
            "To use these packaged files with ArtifactAlchemy:",
            final_response,
        )
        self.assertIn(
            "1. Save the content of each consolidated file",
            final_response,
        )
        self.assertIn(
            "2. Run ArtifactAlchemy on each file:",
            final_response,
        )
        self.assertIn(
            "3. All artifacts will be extracted to the same output folder",
            final_response,
        )


if __name__ == "__main__":
    unittest.main()
