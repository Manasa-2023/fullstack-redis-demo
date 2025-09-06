
# CI/CD Pipeline with GitHub Actions & Docker

This project demonstrates a complete **CI/CD pipeline** using **GitHub Actions, Docker, and Docker Hub**, focused on local deployment without any cloud provider.

It consists of a simple **Fullstack Redis Demo Application**:
- Backend (Node.js + Express)
- Frontend (React)
- Redis for in-memory data storage

---

## Features

- Automatic **CI/CD pipeline** using GitHub Actions  
- Build and push Docker images to Docker Hub  
- Expose APIs: `/health`, `/counter`
- Styled frontend showing Health Status and Counter value  
- Automated backend tests using **Jest**  

---

## How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/Manasa-2023/fullstack-redis-demo.git
   ```

2. Navigate to the project folder:
   ```bash
   cd fullstack-redis-demo/Project-1-CICD-Pipeline
   ```

3. Build and start services:
   ```bash
   docker compose up --build -d
   ```

4. Open in browser:
   - Frontend: [http://localhost:3000](http://localhost:3000)  
   - Backend Health API: [http://localhost:5000/health](http://localhost:5000/health)  
---

## Docker Hub Images

- Backend Image:  
  [https://hub.docker.com/r/manasan1310/fullstack-redis-demo-backend](https://hub.docker.com/r/manasan1310/fullstack-redis-demo-backend)

- Frontend Image:  
  [https://hub.docker.com/r/manasan1310/fullstack-redis-demo-frontend](https://hub.docker.com/r/manasan1310/fullstack-redis-demo-frontend)

---

## CI/CD Pipeline Steps

1. Checkout source code  
2. Install backend dependencies and run tests with Jest  
3. Build Docker images (backend & frontend)  
4. Push Docker images to Docker Hub automatically on each GitHub commit

Pipeline runs visible here:  
 [GitHub Actions Workflows](https://github.com/Manasa-2023/fullstack-redis-demo/actions)

---

## Conclusion

This project shows a practical CI/CD pipeline implementation using GitHub Actions and Docker.  
It ensures automated builds, tests, and deployments locally, making the development process fast, reliable, and reproducible.
