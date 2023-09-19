import r2pipe
import sys

def analyze_ipa(ipa_file, output_file):
    # Initialize Radare2
    r2 = r2pipe.open(ipa_file)

    # Analyze the binary
    r2.cmd("aaa")

    # Get symbolic links
    links = r2.cmd("izL").strip().split("\n")

    # Get leaked methods
    methods = r2.cmd("iL").strip().split("\n")

    # Get metadata
    metadata = r2.cmd("iI").strip().split("\n")

    # Get strings
    strings = r2.cmd("izz").strip().split("\n")

    # Get content of text and data sections
    text_section = r2.cmd("iS~.text").strip().split("\n")
    data_section = r2.cmd("iS~.data").strip().split("\n")

    # Close Radare2
    r2.quit()

    # Save the output to a file
    with open(output_file, "w") as f:
        f.write("Symbolic Links:\n")
        f.write("\n".join(links) + "\n\n")

        f.write("Leaked Methods:\n")
        f.write("\n".join(methods) + "\n\n")

        f.write("Metadata:\n")
        f.write("\n".join(metadata) + "\n\n")

        f.write("Strings:\n")
        f.write("\n".join(strings) + "\n\n")

        f.write("Text Section:\n")
        f.write("\n".join(text_section) + "\n\n")

        f.write("Data Section:\n")
        f.write("\n".join(data_section) + "\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python analyze_ipa.py <IPA_FILE> <OUTPUT_FILE>")
    else:
        ipa_file = sys.argv[1]
        output_file = sys.argv[2]
        analyze_ipa(ipa_file, output_file)
