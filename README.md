# Prompt Optimizer

A Python-based tool for optimizing prompts using local Llama models. Supports multiple backends and optimization strategies.

## Features

- Multiple backend support (Ollama, llama-cpp-python, Transformers)
- Built-in optimization strategies (clarity, creativity, structure, conciseness)
- Optimization history tracking
- Configurable evaluation metrics
- Professional logging and error handling

## Installation

### Prerequisites
- Python 3.8+
- One of the following backends:

#### Option 1: Ollama (Recommended)
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a model
ollama pull llama2

# Install Python package
pip install ollama
```

#### Option 2: llama-cpp-python
```bash
pip install llama-cpp-python
# Download model file (.gguf format) to ./models/
```

#### Option 3: Transformers
```bash
pip install transformers torch
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Quick Start

```python
from prompt_optimizer import PromptOptimizer

# Initialize with Ollama
optimizer = PromptOptimizer(backend='ollama', model_name='llama2')

# Optimize a prompt
original = "Write a story about a dog"
result = optimizer.optimize_prompt(original, optimization_type='clarity')

print("Original:", result.original_prompt)
print("Optimized:", result.optimized_prompt)
print("Score:", result.score)
```

## Usage

### Command Line Interface
```bash
# Basic usage
python prompt_optimizer.py --prompt "Your prompt here"

# Specify optimization type
python prompt_optimizer.py --prompt "Your prompt" --type clarity

# Use different model and generate multiple optimizations
python prompt_optimizer_script.py --model llama3.3 --input "help me code" --count 4

# Use different backend
python prompt_optimizer.py --backend llama_cpp --model llama-2-7b-chat

# Batch processing
python prompt_optimizer.py --input prompts.txt --output results.json
```

### Python API

#### Initialize Optimizer
```python
# Ollama backend
optimizer = PromptOptimizer(backend='ollama', model_name='llama2')

# llama-cpp backend
optimizer = PromptOptimizer(backend='llama_cpp', model_name='llama-2-7b-chat')

# Transformers backend
optimizer = PromptOptimizer(backend='transformers', model_name='Llama-2-7b-chat-hf')
```

#### Optimization Types
- `clarity`: Make prompts clearer and more specific
- `creativity`: Enhance creative and imaginative outputs
- `structure`: Improve organization and logical flow
- `conciseness`: Reduce length while maintaining effectiveness

#### Batch Processing
```python
prompts = ["Prompt 1", "Prompt 2", "Prompt 3"]
results = optimizer.batch_optimize(prompts, optimization_type='clarity')
```

#### History and Analysis
```python
# View optimization history
history = optimizer.get_history()

# Export results
optimizer.export_history('optimization_results.json')

# Load previous results
optimizer.load_history('optimization_results.json')
```

## Configuration

Create a `config.json` file to customize optimization strategies:

```json
{
  "optimization_strategies": {
    "clarity": {
      "system_prompt": "Custom system prompt for clarity optimization",
      "temperature": 0.3,
      "max_tokens": 500
    }
  },
  "model_path": "./models/your-model.gguf",
  "evaluation_criteria": {
    "clarity_keywords": ["clear", "specific", "precise"]
  }
}
```

## File Structure

```
prompt-optimizer/
├── prompt_optimizer.py      # Main optimizer class
├── cli.py                  # Command line interface
├── config.json             # Configuration file
├── requirements.txt        # Python dependencies
├── tests/                  # Unit tests
├── examples/              # Usage examples
└── docs/                  # Additional documentation
```

## Backend Comparison

| Backend | Pros | Cons | Best For |
|---------|------|------|----------|
| Ollama | Easy setup, model management | Less control | Beginners, quick prototyping |
| llama-cpp | Full control, no external service | Complex setup | Production, performance critical |
| Transformers | Most flexible, research features | High memory usage | Research, experimentation |

## Requirements

```
ollama>=0.1.0
llama-cpp-python>=0.2.0
transformers>=4.30.0
torch>=2.0.0
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License

## Support

For issues and questions, please open a GitHub issue or contact the development team.