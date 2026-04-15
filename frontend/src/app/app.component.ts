import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { FaqService } from './services/faq.service';

interface Message {
  type: 'user' | 'bot';
  content: string;
  relevantFaqs?: any[];
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  userQuestion: string = '';
  messages: Message[] = [];
  loading: boolean = false;

  constructor(private faqService: FaqService) { }

  sendQuestion() {
    if (!this.userQuestion.trim()) return;

    // Add user message
    this.messages.push({
      type: 'user',
      content: this.userQuestion
    });

    this.loading = true;

    // Query the backend
    this.faqService.queryFaq(this.userQuestion).subscribe(
      (response: any) => {
        this.messages.push({
          type: 'bot',
          content: response.answer,
          relevantFaqs: response.relevant_faqs
        });
        this.loading = false;
      },
      (error: any) => {
        this.messages.push({
          type: 'bot',
          content: 'Error: Unable to process your question.'
        });
        this.loading = false;
        console.error(error);
      }
    );

    this.userQuestion = '';
  }
}
