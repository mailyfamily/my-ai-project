#!/bin/bash

echo "🎧 德语听力练习平台 - 启动脚本"
echo "================================"

echo ""
echo "📍 后端服务器: http://localhost:5000"
echo "📍 前端应用: http://localhost:3000"
echo ""

cd /d/my-ai-project

echo "✅ 后端已在后台运行"
echo "✅ 启动前端开发服务器..."
echo ""

cd frontend
npm run dev

