const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const exercises = require('./data/exercises.json');

const DB_PATH = path.join(__dirname, 'data.db');
let db = null;

const dbModule = {
  init() {
    db = new sqlite3.Database(DB_PATH, (err) => {
      if (err) console.error(err);
      else console.log('Connected to SQLite database');
    });

    db.serialize(() => {
      db.run(`
        CREATE TABLE IF NOT EXISTS students (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
      `);

      db.run(`
        CREATE TABLE IF NOT EXISTS responses (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          student_id INTEGER NOT NULL,
          exercise_id INTEGER NOT NULL,
          selected_answer INTEGER NOT NULL,
          is_correct BOOLEAN,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
          FOREIGN KEY (student_id) REFERENCES students(id)
        )
      `);
    });
  },

  getOrCreateStudent(name) {
    return new Promise((resolve) => {
      db.all('SELECT * FROM students WHERE name = ?', [name], (err, rows) => {
        if (err) {
          console.error(err);
          resolve(null);
        } else if (rows && rows.length > 0) {
          resolve(rows[0]);
        } else {
          db.run('INSERT INTO students (name) VALUES (?)', [name], function(err) {
            if (err) {
              console.error(err);
              resolve(null);
            } else {
              resolve({ id: this.lastID, name });
            }
          });
        }
      });
    });
  },

  getAllStudents() {
    return new Promise((resolve) => {
      db.all('SELECT * FROM students ORDER BY created_at DESC', (err, rows) => {
        resolve(err ? [] : rows || []);
      });
    });
  },

  getStudentProgress(studentId) {
    return new Promise((resolve) => {
      db.all(
        `SELECT * FROM responses WHERE student_id = ? ORDER BY created_at`,
        [studentId],
        (err, rows) => {
          if (err) return resolve({});
          const progress = { total: rows?.length || 0, correct: 0, byLevel: {} };
          rows?.forEach(r => {
            if (r.is_correct) progress.correct++;
          });
          resolve(progress);
        }
      );
    });
  },

  getAllExercises() {
    return exercises;
  },

  getExercisesByLevel(level) {
    return exercises.filter(e => e.level === level);
  },

  submitAnswer(studentId, exerciseId, selectedAnswer) {
    const exercise = exercises.find(e => e.id === exerciseId);
    const isCorrect = exercise && exercise.correctAnswer === selectedAnswer;

    return new Promise((resolve) => {
      db.run(
        'INSERT INTO responses (student_id, exercise_id, selected_answer, is_correct) VALUES (?, ?, ?, ?)',
        [studentId, exerciseId, selectedAnswer, isCorrect],
        function(err) {
          if (err) {
            console.error(err);
            resolve({ error: 'Failed to submit' });
          } else {
            resolve({
              isCorrect,
              correctAnswer: exercise?.correctAnswer,
              explanation: exercise?.explanation || ''
            });
          }
        }
      );
    });
  },

  getAdminReport() {
    return new Promise((resolve) => {
      db.all(`
        SELECT
          s.id, s.name,
          COUNT(r.id) as total_answers,
          SUM(CASE WHEN r.is_correct THEN 1 ELSE 0 END) as correct_answers
        FROM students s
        LEFT JOIN responses r ON s.id = r.student_id
        GROUP BY s.id, s.name
        ORDER BY s.created_at DESC
      `, (err, rows) => {
        if (err) {
          console.error(err);
          resolve([]);
        } else {
          resolve(rows || []);
        }
      });
    });
  }
};

module.exports = dbModule;
