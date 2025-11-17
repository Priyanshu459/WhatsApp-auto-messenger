# WhatsApp Auto Message Scheduler 📱⏰

A Python application that allows you to schedule WhatsApp messages to be sent automatically at a specific date and time using the Twilio API.

## 🌟 Features

- Schedule WhatsApp messages for future delivery
- Interactive command-line interface
- Date and time validation
- Automatic message sending at scheduled time
- Error handling and user feedback

## 📋 Prerequisites

Before you begin, ensure you have the following:

- Python 3.7 or higher installed
- A Twilio account (free trial available)
- Twilio WhatsApp Sandbox configured

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/whatsapp-auto-message.git
cd whatsapp-auto-message
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

## 🔧 Configuration

### Setting Up Twilio

1. **Create a Twilio Account**
   - Visit [Twilio's website](https://www.twilio.com/try-twilio)
   - Sign up for a free account

2. **Get Your Credentials**
   - Go to your [Twilio Console](https://console.twilio.com/)
   - Copy your `Account SID` and `Auth Token`

3. **Configure WhatsApp Sandbox**
   - Navigate to Messaging > Try it out > Send a WhatsApp message
   - Follow the instructions to join your WhatsApp Sandbox
   - Send the provided code to the Twilio WhatsApp number

4. **Update Configuration**
   
   Create a `.env` file in the project root:
   
   ```env
   TWILIO_ACCOUNT_SID=your_account_sid_here
   TWILIO_AUTH_TOKEN=your_auth_token_here
   TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
   ```

   **Important:** Never commit your `.env` file to GitHub!

5. **Update the Code**
   
   Replace the hardcoded credentials in `whatsapp_auto_message.py` with environment variables:
   
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   
   account_sid = os.getenv('TWILIO_ACCOUNT_SID')
   auth_token = os.getenv('TWILIO_AUTH_TOKEN')
   ```

## 📦 Requirements

Create a `requirements.txt` file:

```
twilio==8.11.0
python-dotenv==1.0.0
```

## 💻 Usage

### Running the Application

```bash
python whatsapp_auto_message.py
```

### Step-by-Step Guide

1. **Enter Recipient Name**
   ```
   Enter the recipient name: John Doe
   ```

2. **Enter Phone Number**
   ```
   Enter the recipient whatsapp number with country code: +1234567890
   ```
   Note: Include the country code (e.g., +91 for India, +1 for USA)

3. **Enter Your Message**
   ```
   Enter the message you want to send: Hello! This is a scheduled message.
   ```

4. **Schedule Date**
   ```
   Enter the date to send the message (YYYY-MM-DD): 2025-11-20
   ```

5. **Schedule Time**
   ```
   Enter the time to send message (HH:MM in 24 hours format): 15:30
   ```

6. **Confirmation**
   ```
   Message scheduled to be sent to John Doe at 2025-11-20 15:30:00
   ```

The program will wait until the scheduled time and automatically send the message.

## 📁 Project Structure

```
whatsapp-auto-message/
│
├── whatsapp_auto_message.py    # Main application file
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (create this)
├── .gitignore                   # Git ignore file
├── README.md                    # This file
└── LICENSE                      # License file
```

## 🔒 Security Best Practices

### 1. Create a `.gitignore` file:

```gitignore
# Environment variables
.env

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

### 2. Never Commit Sensitive Data

- ❌ Don't hardcode credentials in your code
- ✅ Use environment variables
- ✅ Add `.env` to `.gitignore`
- ✅ Provide a `.env.example` file

### 3. Create `.env.example`:

```env
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
```

## ⚠️ Important Notes

### Limitations

- **Twilio Sandbox**: Free tier has limitations. You can only send messages to numbers that have joined your sandbox.
- **Scheduling**: The program must remain running until the scheduled time. For production use, consider using task schedulers or cloud functions.
- **Time Zones**: Ensure your system time is correct for accurate scheduling.

### WhatsApp Sandbox Restrictions

- Messages can only be sent to pre-approved numbers
- The recipient must send the join code to your Twilio number first
- Sandbox is for testing purposes only

### Upgrading from Sandbox

For production use:
1. Request WhatsApp Business API access from Twilio
2. Complete the approval process
3. Get your own WhatsApp Business number

## 🐛 Troubleshooting

### Common Issues

1. **"An error occurred" message**
   - Check your Twilio credentials
   - Verify the recipient has joined your sandbox
   - Ensure phone number format is correct (+countrycode+number)

2. **Authentication Error**
   - Verify your Account SID and Auth Token
   - Check if credentials are correctly loaded from `.env`

3. **Message Not Sending**
   - Confirm the recipient is registered in your sandbox
   - Check Twilio console for error logs
   - Verify your Twilio account has sufficient credits

4. **Time Already Passed Error**
   - Make sure you enter a future date and time
   - Check your system clock is accurate

## 🛠️ Improvements & Future Features

Potential enhancements:
- [ ] Support for multiple recipients
- [ ] Recurring messages
- [ ] Message templates
- [ ] GUI interface
- [ ] Database integration for message history
- [ ] Cloud deployment (AWS Lambda, Google Cloud Functions)
- [ ] Timezone support
- [ ] Message confirmation and status tracking

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- [Twilio](https://www.twilio.com/) for providing the WhatsApp API
- Python community for excellent libraries
- All contributors to this project

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check [Twilio's documentation](https://www.twilio.com/docs/whatsapp)
- Review [Twilio's WhatsApp Sandbox guide](https://www.twilio.com/docs/whatsapp/sandbox)

## ⚖️ Disclaimer

This tool is for educational and personal use only. Make sure to comply with:
- WhatsApp's Terms of Service
- Twilio's Acceptable Use Policy
- Local spam and messaging regulations
- Recipient consent requirements

**Never use this tool for spam or unsolicited messages.**

---

**Happy Coding! 🎉**

If you find this project helpful, please consider giving it a ⭐ on GitHub!
