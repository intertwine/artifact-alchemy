use std::env;
use std::process;
use artifact_alchemy::process_artifacts;
use current_platform::{COMPILED_ON, CURRENT_PLATFORM};

const VERSION: &str = env!("CARGO_PKG_VERSION");

fn print_version() {
    println!("ArtifactAlchemy (aalc) v{}", VERSION);
    println!("Compiled on {}", COMPILED_ON);
    println!("Running on {}", CURRENT_PLATFORM);
}

fn print_usage() {
    println!("ArtifactAlchemy (aalc) v{}", VERSION);
    println!("Usage: aalc <input_file> <output_directory>");
    println!("  <input_file>: Path to the concatenated markdown file");
    println!("  <output_directory>: Directory where individual files will be created");
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 3 {
        print_version();
        print_usage();
        process::exit(1);
    }

    let input_file = &args[1];
    let output_dir = &args[2];

    println!("🧪 ArtifactAlchemy v{} 🧪", VERSION);
    println!("Transmuting artifacts from {} into {}", input_file, output_dir);

    match process_artifacts(input_file, output_dir) {
        Ok(files_created) => {
            println!("✨ Transmutation complete! {} artifacts created.", files_created);
        },
        Err(e) => {
            eprintln!("Error during transmutation: {}", e);
            process::exit(1);
        }
    }
}
