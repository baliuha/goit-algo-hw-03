# goit-algo-hw-03

### task1.py
Recursively copies all files from a source directory to a destination directory, organizing them into subdirectories by file extension.
- Walks through the source directory recursively
- For each file, extracts its extension (e.g., `.txt`, `.pdf`)
- Copies files into destination for each extension (e.g., `txt/`, `pdf/`, `no_extension/`)
```bash
python task1.py <source_directory> [destination_directory]
```

### task2.py
Renders a Koch snowflake fractal using the Turtle graphics module.
- Prompts for a recursion depth (0–6)
- Draws a three-sided Koch snowflake using recursive line subdivision
```bash
python task2.py
```