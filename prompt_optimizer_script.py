# prompt_optimizer.py
import requests
import argparse
import re
from typing import List

OLLAMA_URL = "http://localhost:11434/api/generate"

def call_ollama(prompt: str, model: str = "llama2") -> str:
    payload = {"model": model, "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json()["response"]

def generate_responses(context: str, model: str, count: int = 5) -> List[str]:
    responses = []
    print(f"Generating {count} responses...")
    
    for i in range(count):
        response = call_ollama(context, model)
        responses.append(response.strip())
        print(f"{i+1}. Generated")
    
    return responses

def rank_responses(responses: List[str], model: str) -> int:
    prompt = "Rank these responses from best (1) to worst based on quality:\n\n"
    
    for i, r in enumerate(responses):
        prompt += f"Response {i+1}: {r[:150]}...\n\n"
    
    prompt += f"Reply with ONLY the best response number (1-{len(responses)}):"
    
    ranking = call_ollama(prompt, model)
    
    # Extract first number found (dynamic range based on count)
    pattern = rf'\b[1-{len(responses)}]\b'
    numbers = re.findall(pattern, ranking)
    if numbers:
        best_index = int(numbers[0]) - 1  # Convert to 0-based index
        # Ensure index is within valid range
        if 0 <= best_index < len(responses):
            return best_index
    
    print(f"Warning: AI ranking returned invalid index. Using first response as fallback.")
    return 0  # Default to first

def generate_best_prompt(best_response: str, model: str) -> str:
    truncated = best_response[:400] + "..." if len(best_response) > 400 else best_response
    
    prompt = f"""Generate the single best prompt that would get this quality response:

"{truncated}"

Reply with ONLY the optimized prompt, nothing else."""

    result = call_ollama(prompt, model)
    
    # Clean up the response - remove any extra formatting
    clean_result = result.strip()
    # Remove quotes if present
    clean_result = clean_result.strip('"\'')
    # Remove any "Best prompt:" or similar prefixes
    clean_result = re.sub(r'^(best prompt|optimized prompt|prompt):\s*', '', clean_result, flags=re.IGNORECASE)
    
    return clean_result

def main():
    parser = argparse.ArgumentParser(description="Prompt Optimizer")
    parser.add_argument("--model", default="llama3.1", help="Model to use")
    parser.add_argument("--input", required=True, help="Input prompt")
    parser.add_argument("--count", type=int, default=5, help="Number of responses to generate (default: 5)")
    args = parser.parse_args()

    print(f"Starting prompt optimization for: '{args.input}'")
    print(f"Using model: {args.model}")
    print(f"Generating {args.count} responses for comparison")
    print("-" * 50)
    
    # Generate responses
    responses = generate_responses(args.input, args.model, count=args.count)
    
    # Find best response
    print(f"\nRanking {len(responses)} responses...")
    best_index = rank_responses(responses, args.model)
    best_response = responses[best_index]
    
    print(f"\nBest Response (#{best_index + 1}):")
    print("-" * 40)
    print(best_response)
    
    # Generate THE best prompt
    print(f"\nGenerating optimized prompt...")
    best_prompt = generate_best_prompt(best_response, args.model)
    
    print(f"\nTHE Perfect Prompt:")
    print("-" * 40)
    print(f'"{best_prompt}"')
    
    print(f"\nOptimization complete! From '{args.input}' to professional prompt!")

if __name__ == "__main__":
    main()