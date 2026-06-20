## Llama 3.2 Results

Deployment:
- Local via Ollama

Testing:
- Direct Ollama execution succeeded.
- OpenClaw integration failed due to memory allocation errors.

Observed Error:
- "llama-server reported out-of-memory during startup"
- "failed to allocate CPU buffer"

Conclusion:
Llama 3.2 worked when executed directly through Ollama but could not be reliably used through OpenClaw on the available hardware configuration.

under screenshots: 
models.png shows the OpenClaw model selector with GPT-5.5 and Llama 3.2 available. 
models_status.png shows the configured models from the OpenClaw CLI.
llama_failure.png shows Llama 3.2 failed inside OpenClaw due to memory allocation issues. 