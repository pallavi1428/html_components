import json
from pathlib import Path

def transform_entry(original_entry):
    """Convert a single entry from original format to training format"""
    # Skip entries without proper descriptions
    if not original_entry.get("AI Generated Description") or not isinstance(original_entry["AI Generated Description"], dict):
        return None
        
    description = original_entry["AI Generated Description"].get("description", "")
    if not description:
        return None
    
    # Construct the new entry
    transformed = {
        "prompt": f"Create a {original_entry['Component Category'].lower()} with: {description}",
        "completion": original_entry["Code"],
        "metadata": {
            "category": original_entry["Component Category"],
            "tags": original_entry["AI Generated Description"].get("tags", []),
            "colors": original_entry["AI Generated Description"].get("colors", []),
            "original_filename": original_entry["File Name"],
            "path": original_entry.get("Path", ""),
            "screenshot": original_entry.get("Screenshot", "")
        }
    }
    
    return transformed

def convert_jsonl(input_path, output_path):
    """Convert entire JSONL file to training format"""
    input_path = Path(input_path)
    output_path = Path(output_path)
    
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            try:
                original_data = json.loads(line)
                transformed = transform_entry(original_data)
                
                if transformed:
                    outfile.write(json.dumps(transformed, ensure_ascii=False) + '\n')
                    
            except json.JSONDecodeError as e:
                print(f"Skipping invalid JSON line: {e}")

    print(f"Conversion complete. Output saved to {output_path}")
    print(f"Entries processed: {sum(1 for _ in open(output_path))}")

# Example usage
if __name__ == "__main__":
    input_file = r"C:\Users\PALLAVI\html_gen00\prompt.jsonl"
    output_file = r"C:\Users\PALLAVI\html_gen00\training_data.jsonl"
    
    convert_jsonl(input_file, output_file)