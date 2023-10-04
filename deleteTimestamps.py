import re


def remove_timestamps(text):
    # Regular expression pattern to match timestamps in the format hh:mm
    pattern = r'\b\d{1,2}:\d{2}\b'
    # Use re.sub() to replace matched timestamps with an empty string
    result = re.sub(pattern, '', text)
    return result

def remove_empty_lines(text):
    # Remove empty lines using regex
    cleaned_text = re.sub(r'\n\s*\n', '\n', text)
    return cleaned_text.strip()  # Strip leading/trailing whitespace

finput = open("file.txt", "r")
foutput = open("output.txt", "a")

text = remove_timestamps(finput.read())
text = remove_empty_lines(text)
print(text)

foutput.write(text)
foutput.close()

print("OPERAZIONE COMPLETATA")
