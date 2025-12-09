import pefile
import sys

## Use py on command line to run not python3, idk why

def inspectHeaders(sample):
    pe = pefile.PE(sample)

    print("Entry point: ", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
    print("Image Base: ", hex(pe.OPTIONAL_HEADER.ImageBase))

    print("\nImported DLLS and functions: ")
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print(" ", entry.dll.decode())
        for imp in entry.imports[:5]:
            print("     -", imp.name.decode() if imp.name else "None")

if __name__ == "__main__":
    inspectHeaders(sys.argv[1])

# This program looks at the header of a PE file and shows which APIs are imported
# which can then be used to intuit the capabilities of the ile,
# For instance, Proccess Monitor uses the WS2_32.dll, meaning it has access to API
# features like listen, send and socket. This shows us at a quick glance that 
# it has network capabilities.

