use artifact_alchemy::process_artifacts;
use std::fs::{self, File};
use std::io::Write;

fn create_test_input(content: &str) -> (tempfile::TempDir, String) {
    let dir = tempfile::TempDir::new().unwrap();
    let input_path = dir.path().join("input.md");
    let mut file = File::create(&input_path).unwrap();
    write!(file, "{}", content).unwrap();
    (dir, input_path.to_str().unwrap().to_string())
}

#[test]
fn test_multiple_artifacts() {
    let content = r#"---
filename: file1.txt
---
Content of file 1
---
filename: subdir/file2.txt
---
Content of file 2
"#;
    let (dir, input_path) = create_test_input(content);
    let output_dir = dir.path().join("output");

    let input_files = vec![input_path.as_str()];
    let files_created = process_artifacts(&input_files, output_dir.to_str().unwrap()).unwrap();

    assert_eq!(files_created, 2);
    let file1 = fs::read_to_string(output_dir.join("file1.txt")).unwrap();
    let file2 = fs::read_to_string(output_dir.join("subdir/file2.txt")).unwrap();
    assert_eq!(file1.trim(), "Content of file 1");
    assert_eq!(file2.trim(), "Content of file 2");
}

#[test]
fn test_empty_input() {
    let (dir, input_path) = create_test_input("");
    let output_dir = dir.path().join("output");

    let input_files = vec![input_path.as_str()];
    let files_created = process_artifacts(&input_files, output_dir.to_str().unwrap()).unwrap();

    assert_eq!(files_created, 0);
    assert!(fs::read_dir(&output_dir).is_err() || output_dir.read_dir().unwrap().next().is_none());
}