
# Running Project-2 (Incident Management)

1. Clone the repo:
   ```bash
   git clone https://github.com/Manasa-2023/fullstack-redis-demo
   ```

2. Navigate to the project folder:
   ```bash
   cd fullstack-redis-demo/Project-2-Incident-Management
   ```

3. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

4. Fill in your own test Gmail credentials in `.env`:
   ```
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_16_char_app_password
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the app:
   ```bash
   python app.py
   ```

7. Open browser:
   http://localhost:5000/

8. Test the functionality:
   - Add new incidents.
   - Resolve existing incidents.
   - Emails will be sent to the address in MAIL_USERNAME.
