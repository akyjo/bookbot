def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    # print(file_contents)
    wordcount = len(file_contents.split())

    print(f"Report of {path_to_file}.")
    print(f"{wordcount} words found.")

    counts = count_chars(file_contents)

    lst = []
    for k, v in counts.items():
        if k.isalpha():
            lst.append({"name": k, "num": v})
    lst.sort(reverse=True, key=lambda x: x["num"])
    for letter in lst:
        print(f"The '{letter["name"]}' char appears {letter["num"]}")
    print("End of report.")


def count_chars(st: str) -> dict:
    counts = {}
    for c in st.lower():
        if c in counts.keys():
            counts[c] += 1
        else:
            counts[c] = 1
    return counts


if __name__ == "__main__":
    main()
