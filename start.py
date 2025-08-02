import os
import uvicorn

if __name__ == "__main__":
    # Get the port from environment variable (GCP sets this)
    # If PORT doesn't exist, use 8000 as default
    port = int(os.getenv("PORT", 8000))  # This converts text to number!
    
    # Start your FastAPI app
    uvicorn.run(
        "main:app",        # This points to your main.py file
        host="0.0.0.0",    # Listen on all network interfaces
        port=port,         # Use the port number we got above
        workers=1          # Use 1 worker process
    )
