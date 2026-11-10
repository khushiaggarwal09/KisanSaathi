# 🌾 KisanSaathi

AI app jo fasal ki photo se bimaari pehchaanta hai aur Hindi mein seedha ilaaj batata hai.

## Features
- Patte ki photo upload karo
- AI (Gemini) bimaari pehchaanta hai
- Lakshan, ilaaj aur bachaav Hindi mein, saral bhasha mein

## Built with
Python, Streamlit, Gemini API

## Kaise chalayein
1. Gemini API key lo (free): https://aistudio.google.com/apikey
2. Packages install karo:
   ```
   pip install -r requirements.txt
   ```
3. API key set karo:
   - Windows: `set GEMINI_API_KEY=your_key`
   - Mac/Linux: `export GEMINI_API_KEY=your_key`
4. App chalao:
   ```
   streamlit run app.py
   ```

## Streamlit Cloud pe deploy
1. share.streamlit.io pe GitHub se login karo
2. Is repo ko select karo, main file `app.py`
3. Settings > Secrets mein likho: `GEMINI_API_KEY = "your_key"`

## Aage ke plans
- Aur fasalein aur bimariyan
- Punjabi, Marathi jaisi aur bhashayein
- Offline mode
