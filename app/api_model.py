from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langchain_core.prompts import PromptTemplate
import uvicorn
from huggingface_hub import cached_assets_path

assets_path = cached_assets_path(library_name="datasets", namespace="SQuAD", subfolder="download")
cache_path = assets_path / "cache.json"

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Cargar el tokenizador y el modelo de HuggingFace
try:
    print("Loading tokenizer and model...")
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    print("Tokenizer and model loaded successfully.")
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    raise

# Configurar Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Modelo de datos para la consulta
class Query(BaseModel):
    text: str

# Función para enviar la consulta al modelo de lenguaje
def get_response(query: str) -> str:
    try:
        print(f"Generating response for query: {query}")
        prompt_template = PromptTemplate(input_variables=["query"], template="User: {query}\nAssistant:")
        formatted_prompt = prompt_template.format(query=query)
        inputs = tokenizer.encode(formatted_prompt, return_tensors="pt")
        outputs = model.generate(inputs, max_length=150, num_beams=5, early_stopping=True)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Generated response: {response}")
        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        raise

# Endpoint para la página de inicio
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint para enviar consultas
@app.post("/query")
def query_model(query: Query):
    try:
        print(f"Received query: {query.text}")
        response = get_response(query.text)
        return {"response": response}
    except Exception as e:
        print(f"Error in query_model: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Ejecutar Uvicorn cuando se llama directamente a main.py
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

