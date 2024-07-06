# Simple Rule-Based Chatbot

## Overview

This project involves the creation of a simple rule-based chatbot using Python. The chatbot is designed to respond to user inputs based on predefined rules and patterns. It demonstrates basic concepts of natural language processing (NLP) and conversation flow management.

## Features

- **Greeting Responses**: The chatbot can recognize greetings and respond accordingly.
- **Farewell Responses**: The chatbot can recognize farewells and respond appropriately.
- **Name Inquiry**: The chatbot can provide information about itself when asked.
- **Weather Inquiry**: The chatbot provides a default response for weather-related questions.
- **Capability Inquiry**: The chatbot explains its functionalities when queried.
- **Pattern Matching**: Utilizes regular expressions to identify patterns in user inputs.

## How It Works

1. **User Input Handling**: The user inputs a query, which is processed by the chatbot.
2. **Pattern Matching**: The chatbot uses regular expressions to match the input against predefined patterns.
3. **Response Generation**: Based on the matched pattern, the chatbot generates an appropriate response.
4. **Conversation Flow**: The conversation continues until the user decides to end it.

## Example Interaction

Chatbot: Hello! How can I help you today?
You: Hi
Chatbot: Hello! How can I help you today?
You: What is your name?
Chatbot: I am a simple rule-based chatbot created to assist you.
You: What can you do?
Chatbot: I can answer simple questions and have basic conversations with you.
You: What is the weather like?
Chatbot: I can't check the weather right now, but you can use a weather app or website.
You: Goodbye
Chatbot: Goodbye! Have a great day!

## Customization

You can easily customize the chatbot by adding more patterns and responses in the `chatbot_response` function. This allows you to expand the chatbot's capabilities and handle a wider range of queries.

