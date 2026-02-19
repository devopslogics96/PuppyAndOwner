# PuppyPal - Puppy & Owner Management Application

A Flask-based web application for managing puppies and their owners. Track your puppies' information and register owners with a simple, user-friendly interface.

## 🐕 Features

- **View All Puppies**: Browse a complete list of all registered puppies
- **Add Puppies**: Register new puppies with name and breed information
- **Register Owners**: Assign owners to puppies and store their contact information
- **Puppy Details**: View detailed information about each puppy and its owners
- **Responsive Navigation**: Easy-to-use menu for seamless navigation

## 📋 Project Structure

```
├── app.py                  # Main Flask application with routes and models
├── models.py              # Database models (alternative/backup models)
├── puppyform.py           # Form definitions (alternative/backup forms)
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage - list all puppies
│   ├── add_puppy.html    # Form to add a new puppy
│   ├── add_owner.html    # Form to register an owner
│   └── puppy_detail.html # Puppy details page with owners
├── instance/             # Instance folder (SQLite database storage)
└── README.md            # This file
```

## 🗄️ Database Schema

### Puppy Model
- `id` (Integer, Primary Key)
- `name` (String, Required) - Puppy's name
- `breed` (String) - Puppy's breed
- `owners` - Relationship to Owner model (One-to-Many)

### Owner Model
- `id` (Integer, Primary Key)
- `name` (String, Required) - Owner's name
- `email` (String) - Owner's email address
- `puppy_id` (Integer, Foreign Key) - Reference to associated puppy

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd d:\MyWorkSpace\python\test
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install flask flask-sqlalchemy flask-wtf wtforms
   ```

### Running the Application

1. **Navigate to the project directory:**
   ```bash
   cd d:\MyWorkSpace\python\test
   ```

2. **Run the Flask application:**
   ```bash
   python app.py
   ```

3. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

The application will automatically create the SQLite database (`puppypal.db`) on first run.

## 📖 Usage Guide

### Home Page (`/`)
- Displays a list of all registered puppies
- Click on any puppy to view detailed information
- Use the navigation menu to add puppies or owners

### Add Puppy (`/add-puppy`)
- Fill in the puppy's name (required)
- Optionally enter the puppy's breed
- Click "Add Puppy" to register
- You'll be redirected to the home page

### Add Owner (`/add-owner`)
- Enter the owner's name (required)
- Optionally enter the owner's email
- Select a puppy from the dropdown list
- Click "Register Owner" to complete registration
- You'll be redirected to the home page

### Puppy Details (`/puppy/<id>`)
- View complete information about a specific puppy
- See all owners associated with that puppy
- Navigate back to home using the menu

## 🛠️ Technology Stack

- **Backend Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Form Handling**: Flask-WTF and WTForms
- **Template Engine**: Jinja2
- **Python Version**: 3.7+

## ⚙️ Configuration

The application uses the following configuration (in `app.py`):
- **SECRET_KEY**: Set to `"dev"` (should be changed for production)
- **Database**: SQLite at `sqlite:///puppypal.db`
- **Debug Mode**: Enabled by default for development

## 📝 API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Display all puppies |
| `/add-puppy` | GET, POST | Add a new puppy |
| `/add-owner` | GET, POST | Register a new owner |
| `/puppy/<id>` | GET | View puppy details and owners |

## 🐛 Troubleshooting

- **Database Not Creating**: Ensure the `instance/` folder exists and is writable
- **Form Validation Error**: Check that required fields (puppy name, owner name) are filled
- **Port 5000 Already in Use**: Change port in `app.py` with `app.run(port=5001, debug=True)`
- **Missing Dependencies**: Run `pip install -r requirements.txt` (create file with all dependencies listed)

## 📦 Future Enhancements

- Add ability to edit/delete puppies and owners
- Add search functionality
- Implement user authentication
- Add puppy photos
- Email notifications for owner registration
- Age and health tracking for puppies
- Adoption history tracking

## 📄 License

This project is open source and available for educational purposes.

## 👤 Notes

- The application uses Flask's development server (not suitable for production)
- No user authentication is implemented
- Database is stored locally as a SQLite file in the `instance/` folder
