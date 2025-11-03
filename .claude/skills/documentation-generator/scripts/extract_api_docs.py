#!/usr/bin/env python3
"""
API Documentation Extractor - Generates API documentation from code
"""

import os
import re
from pathlib import Path


def extract_api_endpoints(source_dir):
     """Extract API endpoints from source code."""
     endpoints = []

     # Walk through source directory
     for root, dirs, files in os.walk(source_dir):
          for file_name in files:
               if file_name.endswith(('.ts', '.js', '.py')):
                    file_path = Path(root) / file_name
                    
                    # Read file content
                    try:
                         with open(file_path, 'r', encoding='utf-8') as f:
                              content = f.read()
                              
                              # Extract REST API routes
                              rest_patterns = [
                              r'@GET\s*\(\s*["\']([^"\']+)["\']',
                              r'@POST\s*\(\s*["\']([^"\']+)["\']',
                              r'@PUT\s*\(\s*["\']([^"\']+)["\']',
                              r'@DELETE\s*\(\s*["\']([^"\']+)["\']',
                              r'app\.get\s*\(\s*["\']([^"\']+)["\']',
                              r'app\.post\s*\(\s*["\']([^"\']+)["\']',
                              r'app\.put\s*\(\s*["\']([^"\']+)["\']',
                              r'app\.delete\s*\(\s*["\']([^"\']+)["\']',
                              r'router\.get\s*\(\s*["\']([^"\']+)["\']',
                              ]
                              
                              for pattern in rest_patterns:
                                   matches = re.finditer(pattern, content)
                                   for match in matches:
                                        endpoint = {
                                             "method": pattern.split('@')[1].split('(')[0],
                                             "path": match.group(1),
                                             "file": str(file_path)
                                   }
                                   endpoints.append(endpoint)
                    except Exception as e:
                         print(f"Warning: Could not read file {file_path}: {e}")
          
          return endpoints


def generate_api_documentation(endpoints):
    """Generate API documentation from extracted endpoints."""
    
    docs = """# API Documentation

## Endpoints

"""

    for endpoint in endpoints:
        docs += f"""### {endpoint["method"].upper()} {endpoint["path"]}

```http
{endpoint["method"].upper()} /api{endpoint["path"]}
```

"""

    return docs


def main():
    """Main function for API documentation extraction."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Extract API documentation from code')
    parser.add_argument('--source-dir', required=True, help='Source code directory')
    parser.add_argument('--output', default='docs/api.md', help='Output file path')
    
    args = parser.parse_args()
    
    print(f"🔍 Extracting API endpoints from: {args.source_dir}")
    
    # Extract endpoints
    endpoints = extract_api_endpoints(args.source_dir)
    
    # Generate API documentation
    api_docs = generate_api_documentation(endpoints)
    
    # Write to output file
    output_path = Path(args.output)
    with open(output_path, 'w', encoding='utf-8') as f:
            f.write(api_docs)
    
    print(f"✅ Generated API documentation at: {output_path}")


if __name__ == "__main__":
    main()