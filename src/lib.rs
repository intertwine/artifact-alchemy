use std::fs::{self, File};
use std::io::{BufRead, BufReader, Write};
use std::path::Path;

pub fn process_artifacts(input_file: &str, output_dir: &str) -> std::io::Result<usize> {
    let file = File::open(input_file)?;
    let reader = BufReader::new(file);

    let mut filename = String::new();
    let mut content = String::new();
    let mut in_frontmatter = false;
    let mut files_created = 0;

    for line in reader.lines() {
        let line = line?;
        if line == "---" {
            if !in_frontmatter {
                // Start of a new artifact
                if !filename.is_empty() && !content.is_empty() {
                    write_file(&filename, &content, output_dir)?;
                    files_created += 1;
                    filename.clear();
                    content.clear();
                }
                in_frontmatter = true;
            } else {
                // End of frontmatter
                in_frontmatter = false;
            }
        } else if in_frontmatter {
            if line.starts_with("filename:") {
                filename = line.trim_start_matches("filename:").trim().to_string();
            }
        } else if !in_frontmatter {
            content.push_str(&line);
            content.push('\n');
        }
    }

    // Handle the last file
    if !filename.is_empty() && !content.is_empty() {
        write_file(&filename, &content, output_dir)?;
        files_created += 1;
    }

    Ok(files_created)
}


fn write_file(filename: &str, content: &str, output_dir: &str) -> std::io::Result<()> {
    let full_path = Path::new(output_dir).join(filename);
    if let Some(parent) = full_path.parent() {
        fs::create_dir_all(parent)?;
    }
    let mut file = File::create(&full_path)?;
    file.write_all(content.as_bytes())?;
    println!("  🧪 Created artifact: {}", full_path.display());
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::io::Write;

    fn create_test_input(content: &str) -> (tempfile::TempDir, String) {
        let dir = tempfile::TempDir::new().unwrap();
        let input_path = dir.path().join("input.md");
        let mut file = File::create(&input_path).unwrap();
        writeln!(file, "{}", content).unwrap();
        (dir, input_path.to_str().unwrap().to_string())
    }

    #[test]
    fn test_single_artifact() {
        let content = r#"---
filename: test.txt
---
This is a test file.
"#;
        let (dir, input_path) = create_test_input(content);
        let output_dir = dir.path().join("output");

        let files_created = process_artifacts(&input_path, output_dir.to_str().unwrap()).unwrap();

        assert_eq!(files_created, 1);
        let created_file = fs::read_to_string(output_dir.join("test.txt")).unwrap();
        assert_eq!(created_file.trim(), "This is a test file.");
    }

    // Add more tests here...
}
