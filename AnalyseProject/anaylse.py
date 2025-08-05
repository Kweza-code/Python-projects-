file_name = input("Please enter the path to the .txt file: ")

try:
    with open(file_name, "r", encoding="UTF-8") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

except FileNotFoundError:
    print("❌ File not found. Please check the path and try again.")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")