import unittest
import re
import os


class ClaudePromptTester(unittest.TestCase):
    def setUp(self):
        # Ensure the file path is correct
        file_path = os.path.join(os.path.dirname(__file__), "response.txt")
        with open(file_path, "r") as file:
            self.simulated_claude_response = file.read()

    def test_artifact_structure(self):
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
        self.assertIn("```markdown", self.simulated_claude_response)
        self.assertIn("```", self.simulated_claude_response)

    def test_usage_instructions(self):
        self.assertIn(
            "To use this packaged file with ArtifactAlchemy:",
            self.simulated_claude_response,
        )
        self.assertIn(
            "1. Save the content above to a file", self.simulated_claude_response
        )
        self.assertIn("2. Run ArtifactAlchemy:", self.simulated_claude_response)


if __name__ == "__main__":
    unittest.main()
