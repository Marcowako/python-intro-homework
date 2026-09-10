# Book Explorer CLI

A command-line tool that searches the Open Library API for books by a given
author and lets you filter results by decade of first publication.

## API Used
[Open Library Search API](https://openlibrary.org/developers/api) — no API key required.

## Installation
1. Clone this repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Running the program

## CLI Interaction
The program prompts for an author's name, fetches all matching books from
Open Library, then optionally lets you filter results to a specific decade
(e.g. entering "1990" shows books first published 1990-1999).
