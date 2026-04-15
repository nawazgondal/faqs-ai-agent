#!/bin/bash
# FAQS AI Agent - Linux/Mac Start Script

echo ""
echo "===================================="
echo "  FAQS AI Agent - System Startup"
echo "===================================="
echo ""

# Check if Ollama is running
if ! pgrep -x "ollama" > /dev/null; then
    echo "WARNING: Ollama is not running!"
    echo "Please start Ollama first: ollama serve"
    echo ""
    read -p "Press enter to continue..."
else
    echo "✓ Ollama is running"
fi

# Start Backend
echo ""
echo "Starting Backend (FastAPI)..."
cd backend
python main.py &
BACKEND_PID=$!
sleep 2

# Start Frontend
echo ""
echo "Starting Frontend (Angular)..."
cd ../frontend
npm start &
FRONTEND_PID=$!
sleep 2

echo ""
echo "===================================="
echo "Services Starting:"
echo ""
echo "Backend:  http://localhost:8000"
echo "Frontend: http://localhost:4200"
echo ""
echo "Docs:     http://localhost:8000/docs"
echo "===================================="
echo ""

# Wait for interrupt
wait
