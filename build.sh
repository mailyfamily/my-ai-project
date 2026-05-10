#!/bin/bash
set -e

export NODE_ENV=development

echo "Installing backend dependencies..."
cd backend
npm ci
cd ..

echo "Installing frontend dependencies..."
cd frontend
npm ci
cd ..

echo "Building frontend..."
cd frontend
npx vite build
cd ..

echo "Build complete!"
