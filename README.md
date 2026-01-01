# 📚 Tech-Doc-Translator-ELI5

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red)
![AI](https://img.shields.io/badge/AI-Powered-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Tech-Doc-Translator-ELI5** is a specialized NLP tool designed to democratize access to complex technical documentation. It utilizes a **multi-agent LLM architecture** to process technical text through two simultaneous pipelines: maintaining technical precision while offering simplified conceptual explanations.

---

## 🚀 Key Features

* **Dual-Perspective Analysis:** Processes input text simultaneously through two distinct AI personas (Expert Engineer & Pedagogical Assistant).
* **High-Fidelity Translation:** Preserves critical terminology (e.g., API, Container, Thread) to maintain technical accuracy.
* **ELI5 (Explain Like I'm 5) Summarization:** Converts complex jargon into relatable metaphors and plain language using advanced reasoning capabilities.
* **Hybrid Architecture:** Leverages the strengths of both **Open Source** and **Commercial** state-of-the-art inference engines for optimal performance.
* **Responsive UI:** Built with Streamlit for a clean, side-by-side comparison interface.

---

## 🛠️ System Architecture

The application employs a parallel processing workflow:

1.  **Input Layer:** Captures raw technical text via the user interface.
2.  **Semantic Routing:** The system dispatches the context to two specialized agents.
    * **Agent A (The Engineer):** Optimized for low temperature (0.1) to ensure deterministic and accurate translations.
    * **Agent B (The Teacher):** Optimized for higher creativity to generate analogies and simplified summaries.
3.  **Visualization:** Merges the asynchronous outputs into a unified view for comparative analysis.

---

## 📸 Screenshots

### Dual-Mode Analysis Interface
*(Place your screenshot of the running app here)*
![App Interface](https://via.placeholder.com/800x400?text=App+Interface+Screenshot)

---

## 💻 Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Tech-Doc-Translator-ELI5.git](https://github.com/YOUR_USERNAME/Tech-Doc-Translator-ELI5.git)
    cd Tech-Doc-Translator-ELI5
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables**
    Create a `.env` file or set up your API keys (The system supports flexible integration with major LLM providers).

4.  **Run the Application**
    ```bash
    streamlit run app.py
    ```

---

## 🎯 Use Cases

* **For Junior Developers:** Quickly grasp complex architectural concepts in documentation.
* **For Technical Writers:** Compare formal documentation with simplified versions for different audiences.
* **For Non-Technical Stakeholders:** Understand project requirements without getting lost in jargon.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](issues).

---

**Developed by Onur YERLİKAYA**
