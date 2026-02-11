📖 Notion Book Rater

<p align="center"> <img src="https://cdn-icons-png.flaticon.com/512/3429/3429149.png" width="120px" alt="Project Logo"/> </p>

<p align="center"> <em> A desktop tool to calculate weighted ratings for books and automatically sync them with your Notion database. </em> </p>

<p align="center"> <img src="https://img.shields.io/badge/License-MIT-E92063?style=flat-square&logo=opensourceinitiative&logoColor=white"/> <img src="https://img.shields.io/badge/Python-3.x-E92063?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/🛠_Status-Finished-E92063?style=flat-square"/> </p>

<p align="center"><em>Built with:</em></p> <p align="center"> <img src="https://img.shields.io/badge/Framework-Flet-E92063?style=flat-square&logo=flutter&logoColor=white"/> <img src="https://img.shields.io/badge/API-Notion-E92063?style=flat-square&logo=notion&logoColor=white"/> <img src="https://img.shields.io/badge/Editor-VS_Code-E92063?style=flat-square&logo=visualstudiocode&logoColor=white"/> </p>

<details><summary><b>📋 Table of Contents</b></summary>

    🧭 Overview

        Why this project?

    ⚙️ Features

    📁 Project Structure

    🧩 Get Started

        🛠️ Local Installation

    🧠 Usage

    📜 License

</details>

<a id="overview"></a>
🧭 Overview

Notion Book Rater is a simple and functional desktop application that helps readers provide fairer ratings for their books. Instead of a random score, it uses a weighted system to calculate the average and sends this data directly to a Notion integration via the official API.

<a id="why-project"></a>
ㅤ---

<details><summary><b>Why this project?</b></summary>

Often, upon finishing a book, it’s hard to decide on a final grade. This project solves that by:

    Standardizing evaluation: Focuses on three pillars (Writing, Flow, and Plot).

    Automating records: Avoids the need to open Notion and manually type every single grade.

    Python Practice: Combines the power of Flet (Flutter for Python) with external API integration.

</details>

<a id="features"></a>
⚙️ Features
	Category	Description
🧮	Weighted Calculation	Defined weights: Writing (3), Flow (2), and Plot/Clarity (5).
🎨	Modern Interface	Built with Flet, featuring real-time validation and dynamic result colors.
🔄	API Sync	Searches for the book by name/author in your database and updates the properties.
🛡️	Validation	Ensures grades are only numbers between 0 and 10.

<a id="project-structure"></a>
📁 Project Structure

The project is kept simple, with all files in the root directory for easy execution:
Bash

NotionBookRater/
├── main.py            # Entry point (runs the app)
├── interface.py       # UI construction and visual logic
├── calculus.py        # Math functions for averages and validation
├── notion_api.py      # Communication with Notion API
├── .env               # (Not included) Your private keys
└── requirements.txt   # Project dependencies

<a id="get-started"></a>
🧩 Get Started

<a id="installation"></a>
🛠️ Local Installation

    Clone the repository
    Bash

    git clone https://github.com/your-username/notion-book-rater.git
    cd notion-book-rater

    Install dependencies
    Bash

    pip install -r requirements.txt

    Configure environment variables Create a file named .env in the root directory and add:
    Code Snippet

    NOTION_TOKEN=your_token_here
    DATABASE_ID=your_database_id_here

    Run the project
    Bash

    python main.py

<a id="usage"></a>
🧠 Usage

    Enter the Book Name and Author (must match exactly what is in your Notion).

    Enter grades from 0 to 10 in the corresponding fields.

    Click Calculate to see the weighted average.

    If you are satisfied with the result, click Confirm and Send to update your Notion page automatically.

    Note: The result's color changes based on the score (Red < 3, Orange < 5, Yellow < 7, Green >= 7).

---

<a id="support-the-developers"></a>
## 👤 Author

Developed with ❤️ by **Turzimm** If this project helped you or inspired you in some way, consider giving it a ⭐!

* **Turzimm** - *Lead Developer* 📎 [GitHub Profile](https://github.com/TurzimmGit) | [LinkedIn](https://linkedin.com/in/artur-ferreira-sales-26a927370/)

---

<a id="license"></a>
📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.

<p align="left"> <a href="#top"> <img src="https://img.shields.io/badge/Back_to_Top_⭱-E92063?style=flat&logoColor=white" /> </a> </p>
