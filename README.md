# ShareVault

**ShareVault** is a modern web application built with Django, designed to offer a secure and efficient way to manage and share files with clients. It comes equipped with a comprehensive admin panel that provides tools for user management, file assignment, and automated access control based on payment status.

## Features

- **Secure File Management**: Admins can upload, manage, and assign files to specific users. Files are stored securely, and access is controlled automatically based on payment verification.
  
- **User Management**: Administrators can create and manage users, each of whom can only access files assigned to them. Users have restricted access, ensuring that they can only view their own files.

- **Automated Access Control**: ShareVault automatically restricts access to files if the associated payment is not completed within the specified time frame. Clients can regain access once payment is confirmed.

- **Dark Mode**: The application includes a dark theme to reduce eye strain and enhance the user experience, especially in low-light environments.

- **Multi-language Support**: ShareVault supports multiple languages, including full support for Polish, making it accessible to a broader audience.

- **Progress Tracking**: A progress bar is displayed during file uploads, providing users with real-time feedback on the status of their upload.

## Installation

To get started with ShareVault, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/sharevault.git
2. **Navigate to the project directory:**
   ```bash
   cd sharevault
3. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
5. **Apply the database migrations:**
   ```bash
   python manage.py migrate
6. **Run the development server:**
   ```bash
   python manage.py runserver

## Configuration
Time Zone: Ensure the time zone in settings.py is set for accurate time management.
Database: Configure the database connection in settings.py using the appropriate credentials and settings.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any enhancements, bug fixes, or improvements.

## Contact
For any inquiries or issues, please open a GitHub issue or contact me directly at [smolinski.patryk@mensa.org.pl].
