# FAQS AI Agent - Frontend

This is the Angular chatbot UI for the FAQ AI Agent system.

## Components

- **app.component.ts** - Main chat component with message handling
- **app.component.html** - Chat UI template
- **app.component.css** - Styling with gradients and animations
- **faq.service.ts** - Backend API service

## Key Features

✅ Real-time chat interface
✅ Message history
✅ Related FAQs display
✅ Loading states
✅ Responsive design
✅ Modern gradient UI

## Running the Frontend

```bash
# Install dependencies
npm install

# Start development server
npm start
```

The application will be available at http://localhost:4200

## Build for Production

```bash
npm run build
```

Output will be in the `dist/` directory.

## Component Structure

```
AppComponent (Standalone)
├── Services
│   └── FaqService (HTTP calls to backend)
├── Template (Chat interface)
└── Styles (Modern gradient design)
```

## How to Use

1. Type a question in the input field
2. Press Enter or click Send
3. Wait for the AI response
4. View related FAQs below each response
5. Continue the conversation

## Configuration

To change the backend URL, edit `services/faq.service.ts`:

```typescript
private apiUrl = 'http://localhost:8000'; // Change this
```

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
