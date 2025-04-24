
# Conversational AI Project

## Setup

1. Clone the repository:
   ```
   git clone <https://github.com/Devilthelegend/conversation_ai/>
   cd conversational_ai
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

4. Run the Gradio UI:
   ```
   python frontend/app.py
   ```

5. Docker (Optional):
   - Build the Docker image:
     ```
     docker build -t conversational-ai .
     ```
   - Run the Docker container:
     ```
     docker run -p 8000:8000 conversational-ai
     ```

## Demo

A brief demo of the app in action can be found here:
1 vs code: [https://drive.google.com/file/d/1VMKp_NCRoDCPf-XYi8e5stGNBq1jkhTR/view?usp=drive_link]
2. output: [https://drive.google.com/file/d/1jobAy_SVWj0Xcczfq0H94YYdfZDYd8TF/view?usp=sharing]
    
