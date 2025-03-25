# 🤖 CrewAI Blog Generation System

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Powered-orange)](https://github.com/joaomdmoura/crewAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Overview

A sophisticated multi-agent system leveraging CrewAI and advanced Language Models to autonomously research, plan, and generate high-quality blog content. This project demonstrates the power of collaborative AI agents working together to create engaging, factually accurate, and well-structured articles.

## ✨ Key Features

### 🎯 Intelligent Agent Collaboration
- **Content Planner Agent**: Strategically outlines articles considering:
  - Latest industry trends and developments
  - Key market players and innovations
  - Target audience preferences
  - SEO optimization opportunities

- **Content Writer Agent**: Crafts compelling content by:
  - Following the planner's strategic outline
  - Incorporating relevant research and data
  - Maintaining consistent tone and style
  - Creating engaging narratives

- **Editor Agent**: Ensures quality through:
  - Grammar and style verification
  - Fact-checking and source validation
  - Content flow optimization
  - SEO best practices implementation

### 🛠️ Technical Capabilities
- Flexible LLM integration (Mistral, HuggingFace, etc.)
- Modular agent architecture for easy customization
- Asynchronous task processing
- HTML output generation
- Environment-based configuration

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip package manager
- API key for your chosen LLM provider

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CrewAI_BlogGen.git
   cd CrewAI_BlogGen
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and preferences
   ```

## 💡 Usage

### Basic Usage
```bash
python main.py
```

Follow the interactive prompts:
1. Choose your LLM model when prompted (mistral/huggingface/openrouterai)
2. Enter your blog topic
3. Wait for the AI agents to collaborate and generate your content

The system will automatically:
- Generate a comprehensive blog post
- Save it as an HTML file in the `output` directory
- Include SEO optimization and proper formatting

### Sample Output

Here's an example of the AI-generated content on "QA Transformation using AI":

![Sample Blog Output](assets/qa_transformation.png)

The system generates well-structured blog posts with:
- Clear section hierarchy
- Professional formatting
- SEO optimization
- Comprehensive coverage of the topic
- Citations and references

## 📁 Project Structure

```
CrewAI_BlogGen/
├── agents/                 # Agent definitions and behaviors
│   ├── __init__.py
│   ├── editor.py          # Content editing agent
│   ├── planner.py         # Content planning agent
│   └── writer.py          # Content writing agent
├── assets/                # Image assets and screenshots
│   └── Blog_output.png    # Sample blog output
├── models/                # LLM integration and configuration
│   ├── __init__.py
│   ├── config/           # Model configuration
│   │   ├── huggingface.py
│   │   ├── mistral.py
│   │   ├── openai.py
│   │   └── openrouterai.py
│   └── llm.py           # LLM setup and management
├── output/               # Generated blog content
│   └── templates/       # HTML templates
│       ├── blog_template.html
│       ├── AI_in_healthcare.html
│       └── QA_transformation_using_AI.html
├── tasks/                # Task definitions and workflows
│   ├── __init__.py
│   ├── edit_task.py
│   ├── plan_task.py
│   └── write_task.py
├── venv/                 # Virtual environment
├── .env                 # Environment variables
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
├── main.py            # Main execution script
├── README.md          # Project documentation
└── requirements.txt   # Project dependencies
```

## 🎯 Example Output

The system generates comprehensive blog posts with:
- Well-structured content hierarchy
- SEO-optimized headings and meta descriptions
- Internal and external citations
- Engaging introductions and conclusions
- Professional formatting and styling

Example topics successfully covered:
- "The Future of AI in Healthcare"
- "Sustainable Technology Trends"
- "Blockchain in Finance"
- "Machine Learning Best Practices"

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the multi-agent framework
- Mistral AI for the language model capabilities
- All contributors and maintainers

## 📧 Contact

For questions and support, please open an issue in the GitHub repository.

---
Built with ❤️ using CrewAI and Mistral