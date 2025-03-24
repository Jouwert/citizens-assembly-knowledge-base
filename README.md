# Citizens' Assembly Knowledge Base and Chatbot

A comprehensive knowledge base and interactive chatbot for information about citizens' assemblies worldwide.

## Project Overview

This project aims to create a modular website with a chatbot that answers questions about citizens' assemblies worldwide. The development follows an iterative approach, with each iteration building upon previous work.

## Project Structure

- `/data`: Resources and database files
- `/src`: Source code
- `/docs`: Documentation
- `/tests`: Testing code

## Iteration 1: Resource Collection and Knowledge Base

### Completed Tasks

1. **Resource Collection**
   - Collected 25 high-quality resources about citizens' assemblies worldwide
   - Ensured diversity in geographic regions (UK, Ireland, France, Canada, Poland, Taiwan, Australia, Mexico, global initiatives)
   - Included various resource types (academic papers, case studies, government reports, websites)
   - Covered diverse topics (climate change, abortion, electoral reform, judicial reform, gender equality, biodiversity, drug policy)
   - Structured data in JSON format with comprehensive metadata

2. **Database Setup**
   - Created code for a vector database using ChromaDB
   - Implemented embeddings generation using sentence-transformers
   - Enabled semantic searching of the knowledge base

### Resources

The knowledge base includes 25 resources with the following metadata:
- Title
- Author/Organization
- Publication date
- URL
- Type of resource
- Geographic focus
- Key topics
- Brief summary

### Database Implementation

The vector database is implemented using:
- ChromaDB for the vector database
- Sentence Transformers for generating embeddings (all-MiniLM-L6-v2 model)
- JSON for structured data storage

## Getting Started

### Prerequisites

- Python 3.10+
- Required packages: `chromadb`, `sentence-transformers`

### Installation

1. Clone this repository
2. Install required packages:
   ```bash
   pip install chromadb sentence-transformers

# Future Iterations
## Iteration 2: Backend Development

### Task 1: Backend API
Create a Flask or FastAPI backend with endpoints for:
- Resource retrieval by ID
- Semantic search across resources
- Question answering based on the knowledge base
- Basic analytics (most viewed resources, common questions)

Implement:
- Rate limiting
- Error handling
- Basic logging
- Documentation for all endpoints

### Task 2: Integration Testing
Develop tests to verify:
- Database connections work properly
- Embeddings are being generated correctly
- Search functionality returns relevant results
- API endpoints return expected responses

## Iteration 3: Frontend Development

### Task 1: User Interface
Create a responsive web interface with:
- Clean, accessible design following modern web standards
- Search functionality for direct resource access
- Chatbot interface that's prominently featured
- Resource browser with filtering capabilities
- About page explaining citizens' assemblies

Use a modern JavaScript framework (React, Vue, or Svelte).

### Task 2: Chatbot Implementation
Implement a chatbot that:
- Answers questions using the knowledge base
- Provides citations to source materials
- Handles conversation context
- Offers suggestions for related queries
- Has a clear, user-friendly interface

## Iteration 4: Integration and Deployment

### Task 1: Full System Integration
- Connect frontend to backend API
- Implement proper error handling across the stack
- Ensure responsive design works on all device sizes
- Add analytics to track usage patterns

### Task 2: Deployment Preparation
- Containerize the application with Docker
- Create deployment scripts
- Document deployment process
- Set up environment variables for configuration

### Task 3: Testing and Refinement
- Conduct comprehensive testing of the entire system
- Fix any bugs or issues
- Optimize performance
- Document all known limitations

## Throughout All Iterations

For each iteration:
1. Create a new branch in GitHub
2. Document progress in README and specific documentation files
3. Commit code frequently with clear commit messages
4. Create a pull request when the iteration is complete
5. Tag the repository with version numbers after each major milestone

## Specific Requirements

1. Follow ethical principles for AI systems:
   - Transparency about data sources
   - Privacy-preserving design
   - Avoiding political bias in resource selection
   - Accessibility for all users

2. Code quality standards:
   - Clean, well-documented code
   - Comprehensive test coverage
   - Security best practices
   - Proper error handling

3. User experience priorities:
   - Fast response times
   - Intuitive interface
   - Clear attribution of information
   - Educational approach to information delivery