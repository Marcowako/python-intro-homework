import requests

def fetch_books(author):
    """Fetch raw book data from the Open Library search API for a given author."""
    url = "https://openlibrary.org/search.json"
    params = {"author": author}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_books(raw_data):
    """Turn raw API JSON into a list of dicts with just the fields we care about."""
    if not isinstance(raw_data, dict) or "docs" not in raw_data:
        print("Unexpected data format received from API.")
        return []

    books = []
    for entry in raw_data["docs"]:
        books.append({
            "title": entry.get("title", "Unknown"),
            "author": ", ".join(entry.get("author_name", ["Unknown"])),
            "year": entry.get("first_publish_year", "Unknown"),
            "subjects": entry.get("subject", [])[:3],
        })
    return books

def display_book(book):
    print(f"\n{book['title']}")
    print(f"  Author: {book['author']}")
    print(f"  First published: {book['year']}")
    if book["subjects"]:
        print(f"  Subjects: {', '.join(book['subjects'])}")

def filter_by_decade(books, decade_start):
    """Filter books first published within a given decade, e.g. 1990 for the 1990s."""
    decade_end = decade_start + 9
    results = []
    for b in books:
        year = b["year"]
        if isinstance(year, int) and decade_start <= year <= decade_end:
            results.append(b)
    return results

def main():
    print("Welcome to the Book Explorer!")
    author = input("Enter an author's name to search for: ").strip()

    if not author:
        print("You need to enter an author name.")
        return

    raw = fetch_books(author)
    if raw is None:
        print("Could not load book data. Exiting.")
        return

    books = parse_books(raw)
    if not books:
        print(f"No books found for author '{author}'.")
        return

    print(f"\nFound {len(books)} books by {author}.")
    decade_input = input("Filter by decade (e.g. 1990), or press Enter to see all: ").strip()

    if decade_input:
        try:
            decade_start = int(decade_input)
            matches = filter_by_decade(books, decade_start)
        except ValueError:
            print("That's not a valid year. Showing all results instead.")
            matches = books
    else:
        matches = books

    if not matches:
        print("No books matched that filter.")
        return

    for b in matches[:15]:
        display_book(b)

if __name__ == "__main__":
    main()
