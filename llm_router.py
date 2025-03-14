from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LLMRouter:
    def __init__(self):
        self.models = {
    "mistral": "mistralai/Mistral-7B-Instruct-v0.1"  # Fully open-source
    }

        self.tokenizers = {name: AutoTokenizer.from_pretrained(model) for name, model in self.models.items()}
        self.models = {name: AutoModelForCausalLM.from_pretrained(model, torch_dtype=torch.float16).to("cuda" if torch.cuda.is_available() else "cpu") for name, model in self.models.items()}

    def query_llm(self, model_name, prompt):
        if model_name not in self.models:
            return "❌ Model not available."

        tokenizer = self.tokenizers[model_name]
        model = self.models[model_name]

        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        output = model.generate(**inputs, max_new_tokens=200)
        return tokenizer.decode(output[0], skip_special_tokens=True)

# Example usage
router = LLMRouter()
print(router.query_llm("Llama", "Explain blockchain technology."))
