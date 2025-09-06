# Running Project-2 (Incident Management)

1. Clone the repo:
   git clone https://github.com/Manasa-2023/fullstack-redis-demo
2. Navigate to the project folder:
   cd fullstack-redis-demo/Project-2-Incident-Management
3. Copy the example environment file:
   cp .env.example .env
4. Fill in your own test Gmail credentials in .env:
   MAIL_USERNAME=<your-test-email>
   MAIL_PASSWORD=<your-app-password>
5. Install dependencies:
   pip install -r requirements.txt
6. Run the app:
   python app.py
7. Open browser:
   http://localhost:5000/
8. Test the functionality:
    1. Add new incidents.
    2. Resolve existing incidents.
    3. Emails will be sent to the address in MAIL_USERNAME.