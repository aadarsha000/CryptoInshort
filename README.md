# Crypto InShort - Read News in 60 Words

## Overview
Crypto InShort is a Django-based web application that provides users with concise and summarized cryptocurrency news articles. Each news article is condensed into 60 words, allowing users to stay informed about the latest trends and updates in the crypto world without spending too much time reading lengthy articles.

## Features
- **Summarized News**: Get the latest cryptocurrency news summarized in just 60 words.
- **User-Friendly Interface**: Clean and intuitive design for easy navigation.
- **Real-Time Updates**: Regularly updated news feed to keep you informed.
- **Search Functionality**: Search for specific news articles or topics.
- **Responsive Design**: Access the platform on any device, whether it's a desktop, tablet, or mobile phone.

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- pip (Python package installer)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/aadarsha000/CryptoInshort.git
   cd crypto-inshort
   ```

2. **Create a Virtual Environment**
   ```bash
   poetry install
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   Open your browser and go to `http://127.0.0.1:8000/` to view the application.

## Usage
- **Home Page**: The home page displays the latest summarized news articles.
- **Search**: Use the search bar to find specific news articles or topics.
- **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/` to manage news articles and users.

## Contributing
We welcome contributions! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to all the contributors who have helped in building and improving this project.
- Special thanks to the Django community for providing excellent documentation and resources.

## Contact
For any questions or suggestions, please feel free to reach out to us at [your-email@example.com](mailto:your-email@example.com).

---

**Happy Reading!** Stay updated with the latest in the crypto world with Crypto InShort.
