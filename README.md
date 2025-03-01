# CrewAI Blog Research and Writing System

## Overview
This project implements a multi-agent system using CrewAI to:
- Plan (Content Planner)
- Write (Content Writer)
- Edit (Editor)

The system leverages the Mistral LLM to create high-quality blog posts efficiently. The agents collaborate to generate content that is engaging, factually accurate, and aligned with the organization's style.

## Features
- **Content Planning**: The Content Planner agent outlines blog articles based on the latest trends, key players, and noteworthy news.
- **Content Writing**: The Content Writer agent crafts insightful and structured articles using the planner's outline.
- **Content Editing**: The Editor agent ensures the final content is polished, grammatically correct, and adheres to journalistic best practices.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/CrewAI_BlogGen.git
   cd CrewAI_BlogGen
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the `.env` file:
   - Create a `.env` file in the root directory of the project.
   - Add your Mistral API key to the `.env` file:
     ```env
     MISTRAL_API_KEY=your_mistral_api_key
     ```

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```

2. Follow the prompts to choose the LLM model and enter the topic for the blog post.

3. The system will generate a blog post and save it as an HTML file in the `output` directory.

## Example
Here is an example of how to use the system:

```bash
$ python main.py
Choose LLM model (mistral / huggingface / llama): mistral
Enter a topic: AI in QA
```

The generated blog post will be saved as `output/AI_in_QA.html`.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.