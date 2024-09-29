# URL_Shortener

## Overview

This URL Shortener is a Python application built using Tkinter for the graphical user interface. The app allows users to enter a long URL, which is then shortened using the pyshorteners library. Users can easily copy the shortened URL to the clipboard for further use. The application also includes validation to ensure that only valid URLs are processed, making it user-friendly and reliable.

## Features

- **GUI-based interface:** A simple and intuitive interface built with Tkinter.
- **URL Validation:** Validates the entered URL to ensure it's properly formatted before shortening.
- **URL Shortening:** Uses the pyshorteners library to shorten the provided URL.
- **Copy to Clipboard:** Allows users to copy the shortened URL directly to the clipboard with one click.
- **Error Handling:** Displays error messages for invalid URLs or if the shortening process fails.

## Prerequisites
Make sure you have Python installed on your machine. You will also need the following Python libraries:

- tkinter
- pyshorteners
- validators
- pyperclip

## Getting Started
1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Aleshini/Math_Quiz_Game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd url_shortener
   ```
3. Run the game:
   ```bash
   python url_short.py
   ```
4. The GUI will appear, allowing you to input a long URL, shorten it, and copy the result.

## Usage
- Enter Long URL: Type or paste a valid URL into the input field labeled "Enter Long URL."
- Shorten the URL: Click the "Short URL" button. If the URL is valid, the shortened version will appear in the field below.
- Copy the URL: Once the shortened URL is generated, click the "Copy Shortened URL" button to copy it to your clipboard for easy sharing.
   
## Contributing
If you'd like to contribute to this project, please fork the repository, make your changes, and create a pull request with a detailed description of your contributions.

## Acknowledgments
This project was developed by Shalini Juyal as part of a CodeClause project to demonstrate skills in Python GUI development and URL shortening using the pyshorteners library.
