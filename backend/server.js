const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const db = require('./db');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(bodyParser.json());

// Initialize database
db.init();

// API: Create or get student
app.post('/api/students', (req, res) => {
  const { name } = req.body;
  if (!name) return res.status(400).json({ error: 'Name required' });

  db.getOrCreateStudent(name).then(student => {
    res.json(student);
  });
});

// API: Get all students (for admin)
app.get('/api/students', (req, res) => {
  db.getAllStudents().then(students => {
    res.json(students);
  });
});

// API: Get student progress
app.get('/api/students/:id/progress', (req, res) => {
  db.getStudentProgress(req.params.id).then(progress => {
    res.json(progress);
  });
});

// API: Get all exercises
app.get('/api/exercises', (req, res) => {
  const { level } = req.query;
  const exercises = level ? db.getExercisesByLevel(level) : db.getAllExercises();
  res.json(exercises);
});

// API: Submit answer and get feedback
app.post('/api/submit', (req, res) => {
  const { studentId, exerciseId, selectedAnswer } = req.body;
  if (!studentId || !exerciseId || selectedAnswer === undefined) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  db.submitAnswer(studentId, exerciseId, selectedAnswer).then(result => {
    res.json(result);
  });
});

// API: Get admin report (all student data)
app.get('/api/admin/report', (req, res) => {
  const { password } = req.query;
  if (password !== 'admin123') {
    return res.status(403).json({ error: 'Invalid password' });
  }

  db.getAdminReport().then(report => {
    res.json(report);
  });
});

// Static files - audios
app.use('/audios', express.static(path.join(__dirname, '../audios')));

// Static files - frontend
app.use(express.static(path.join(__dirname, '../frontend/dist')));

// Fallback to index.html for SPA
app.use((req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/dist/index.html'));
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
