# Marketing Crew

The Marketing Crew project is designed to automate and streamline marketing strategies. It utilizes a modular, agent-based architecture to handle various marketing tasks such as market research, content creation, and SEO optimization. This project leverages the CrewAI framework alongside external LLMs for content generation and planning.

## Folder Structure

```
Marketing_crew/
├── config/
│   ├── agents.yaml      # Configuration for agents (roles, goals, backstories)
│   └── tasks.yaml       # Configuration for marketing tasks
├── crew.py              # Main file defining agents and tasks for the marketing crew
└── README.md            # This file
```

## Setup

1. **Clone the repository:**  
   Clone or download the project files to your local machine.

2. **Create and activate a virtual environment:**  
   On Windows:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**  
   Install the necessary packages using pip:
   ```
   pip install -r requirements.txt
   ```
   Ensure that you have the following dependencies installed:
   - CrewAI
   - pydantic
   - python-dotenv

4. **Environment Variables:**  
   Create a `.env` file in the project root if it doesn't exist and add your Perplexity API key:
   ```
   PERPLEXITY_API_KEY=your_api_key_here
   ```
   The `crew.py` script loads environment variables on startup.

## Configuration

Update the `agents.yaml` and `tasks.yaml` files located in the `config` folder with the desired configurations for your agents and tasks.

## Running the Project

To run the Marketing Crew tasks:
1. Open a terminal in the project directory.
2. Execute the following command:
   ```
   python Marketing_crew/crew.py
   ```
   The script will initialize the marketing crew, set up agents, and execute the defined tasks sequentially.

## Customization

- **Agents:**  
  Modify roles, goals, backstories, and tools within `crew.py` to adjust agent behavior.
  
- **Tasks:**  
  Update task configurations in `tasks.yaml` and adjust how tasks invoke different agents.

- **LLM Configuration:**  
  Ensure that the LLM settings in `crew.py` (e.g., model, temperature) are aligned with your project requirements.

## Troubleshooting

- **API Key Issues:**  
  Verify that your Perplexity API key is correctly set in the `.env` file.
  
- **Dependency Issues:**  
  Make sure all required packages are installed. Use `pip install -r requirements.txt` to resolve any missing packages.


## Contributing

Contributions are welcome! Feel free to submit pull requests or raise issues for any bugs or enhancement ideas.

---

For more information on how to use and configure CrewAI, please refer to the [CrewAI Documentation](https://crew.ai).

Happy coding!
