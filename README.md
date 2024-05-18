
# Rentify

Rentify is a Django-based web application for managing property listings and interests.

## Table of Contents

- [Project Description](#project-description)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Development Server](#running-the-development-server)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Description

Rentify is a platform designed to help users manage property listings, express interest in properties, and connect with sellers. It allows users to list their properties with details such as area, number of bedrooms, bathrooms, amenities, nearby hospitals, colleges, and price. Users can also express their interest in properties listed by others.

## Setup

### Prerequisites

- Python 3.x
- Django (installed automatically via `requirements.txt`)
- Other dependencies listed in `requirements.txt`

### Installation

1. Download and extract the ZIP file containing the Rentify project.

2. Navigate to the project directory in your terminal or command prompt.

3. Install dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Configure the Django settings:

   - Create a `.env` file in the root of your project.
   - Add necessary configuration variables such as `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, etc.

### Running the Development Server

1. Activate the virtual environment (if you're using one):

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

2. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

   The development server will start running at http://127.0.0.1:8000/.

## Usage

After setting up the project and running the development server, you can access Rentify in your web browser. You can create a new account, list properties, express interest in properties listed by others, and manage your property listings.

## Contributing

We welcome contributions from the community! If you have any ideas, bug reports, or feature requests, please feel free to submit them through the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
