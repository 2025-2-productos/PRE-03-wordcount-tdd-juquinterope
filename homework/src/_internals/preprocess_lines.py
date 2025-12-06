def preprocess_lines(lines):
    processed = []
    for line in lines:
        stripped = line.strip().lower()
        if stripped:  # Filtrar líneas vacías
            processed.append(stripped)
    return processed