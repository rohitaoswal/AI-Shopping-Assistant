🛍️ AI Shopping Assistant

This is a simple AI shopping assistant built using LangChain, Streamlit, Ollama, and Tavily. 
It lets users search for products on 🛒 Amazon, Flipkart, Myntra, and Ajio by asking questions in natural language.

--------------------------
✨ Features:
--------------------------
- 💬 Ask shopping-related queries 
- 🔎 Searches Amazon, Flipkart, Myntra, Ajio using Tavily
- 🤖 Uses local LLM (gemma2:2b via Ollama)
- 🖥️ Chat interface built with Streamlit

--------------------------
🎯 Use Case:
--------------------------

The AI Shopping Assistant acts like a personal fashion search agent:

- 👜 Ask it to find products you want to shop  
- 🛍️ It searches live product listings on Amazon, Flipkart, Myntra, and Ajio  
- 🔗 It gives you direct product links to the most relevant items  
- 🧠 You can refine your search by chatting naturally  

--------------------------
⚙️ How to Run:
--------------------------
1. Clone the project folder

2. Install required libraries:

   pip install -r requirements.txt

3. Create a .env file with:

   TAVILY_API_KEY=your_tavily_key_here

4. Make sure Ollama is installed and run:

   ollama run gemma2:2b

5. Start the app:

   streamlit run shopping_app.py

  
📌This project is intended for educational and demonstration purposes only. Product results depend on third-party website indexing and may not always reflect real-time availability or pricing.

--------------------------
Made by: Rohita Oswal
--------------------------
