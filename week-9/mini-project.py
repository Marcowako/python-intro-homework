import sys
import requests


def fetch_countries():
    url = "https://restcountries.com/v3.1/all?fields=name,capital,region,population"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(
                f"Error: Unable to fetch data (Status code: {response.status_code})"
            )
            sys.exit(1)

        raw_data = response.json()
        countries = []

        for item in raw_data:
            # Extract common name safely
            name = item.get("name", {}).get("common", "Unknown")

            # Handle missing capital list (some countries don't have a capital listed)
            capitals = item.get("capital")
            capital = capitals[0] if capitals and len(capitals) > 0 else "N/A"

            region = item.get("region", "N/A")
            population = item.get("population", 0)

            countries.append(
                {
                    "name": name,
                    "capital": capital,
                    "region": region,
                    "population": population,
                }
            )

        return countries

    except requests.exceptions.RequestException as e:
        print(f"Error: Could not reach the server. Details: {e}")
        sys.exit(1)


def search_by_name(countries):
    term = input("Search: ").strip().lower()
    matches = [c for c in countries if term in c["name"].lower()]

    if not matches:
        print("No matching countries found.\n")
        return

    for c in matches:
        pop_fmt = f"{c['population']:,}"
        print(
            f"{c['name']} — Capital: {c['capital']} | Region: {c['region']} | Population: {pop_fmt}"
        )
    print()


def filter_by_region(countries):
    region_input = input("Enter region (e.g., Africa, Asia, Europe): ").strip().lower()
    matches = [c for c in countries if c["region"].lower() == region_input]

    if not matches:
        print(f"No countries found in region '{region_input}'.\n")
        return

    # Sort matching countries by population in descending order
    matches.sort(key=lambda x: x["population"], reverse=True)

    for c in matches:
        pop_fmt = f"{c['population']:,}"
        print(
            f"{c['name']} — Capital: {c['capital']} | Region: {c['region']} | Population: {pop_fmt}"
        )
    print()


def main():
    countries = fetch_countries()

    while True:
        print("=== Country Explorer ===")
        print("1. Search by name")
        print("2. Filter by region")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            search_by_name(countries)
        elif choice == "2":
            filter_by_region(countries)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()