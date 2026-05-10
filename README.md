# 🎧 德语听力练习平台

一个为大学德语讲师设计的在线听力练习平台，支持学生练习和教师查看成绩。

## 功能特性

### 学生端
- 📝 输入名字快速进入
- 🎵 听力练习（A1、A2、B1三个难度）
- 📋 4选1单选题
- ✅ 即时反馈和答案解释
- 📊 实时显示学生成绩

### 教师端  
- 🔐 管理员密码登录（密码：admin123）
- 📊 查看所有学生成绩
- 📈 显示学生正确率
- 💯 统计平均成绩

## 快速开始

### 第一步：安装依赖

```bash
# 安装后端依赖
cd backend
npm install

# 安装前端依赖
cd ../frontend
npm install
```

### 第二步：启动应用

```bash
# 终端1 - 启动后端服务器
cd backend
npm start

# 终端2 - 启动前端开发服务器
cd frontend  
npm run dev
```

应用将在以下地址运行：
- 前端：http://localhost:3000
- 后端 API：http://localhost:5000

### 第三步：使用应用

1. **学生练习**
   - 点击"学生练习"
   - 输入你的名字
   - 选择难度等级（A1/A2/B1）
   - 点击"开始练习"
   - 听音频，选择答案
   - 提交获得即时反馈

2. **教师查看**
   - 点击"老师查看"
   - 输入管理员密码：`admin123`
   - 查看所有学生的成绩和进度

## 项目结构

```
德语听力平台/
├── backend/                  # Node.js后端
│   ├── server.js            # Express服务器
│   ├── db.js                # SQLite数据库
│   ├── data/
│   │   └── exercises.json   # 听力题库（15道题）
│   └── package.json
├── frontend/                # React前端
│   ├── src/
│   │   ├── App.jsx          # 主应用
│   │   ├── App.css          # 样式
│   │   └── pages/
│   │       ├── StudentView.jsx   # 学生练习页
│   │       └── AdminView.jsx     # 教师管理页
│   └── package.json
├── audios/                  # 音频文件目录
└── README.md
```

## 技术栈

- **前端**：React 19 + Vite
- **后端**：Node.js + Express 5
- **数据库**：SQLite
- **样式**：CSS3

## 数据库

应用使用SQLite存储：
- `students` 表 - 学生信息
- `responses` 表 - 学生答题记录

数据库文件自动创建在 `backend/data.db`

## 初始题库

内置15道初级德语听力题：
- **A1级**：5道基础题（问候、颜色、家庭等）
- **A2级**：5道初级题（工作、旅行、爱好等）  
- **B1级**：5道中级题（技术、环保、文化等）

## 生产部署

### 构建前端

```bash
cd frontend
npm run build
```

构建文件输出到 `frontend/dist`

### 部署到阿里云

推荐使用轻量应用服务器：
1. 创建Linux服务器（CentOS/Ubuntu）
2. 安装Node.js
3. 上传项目文件
4. 运行后端服务器

## 后期扩展

- [ ] 添加真实的德国之声音频
- [ ] 实现手机应用（PWA）
- [ ] 增加更多难度级别（C1、C2）
- [ ] 添加用户认证系统
- [ ] 导出学生成绩为PDF
- [ ] 实现教师手动添加题目

## 故障排除

**问题**：前端无法连接后端
- 确保后端运行在 5000 端口
- 检查 CORS 设置

**问题**：数据库错误
- 删除 `backend/data.db` 重新创建

**问题**：音频文件找不到
- 确保音频文件在 `audios/` 目录
- 检查文件格式为 `.mp3`

## 许可证

MIT
