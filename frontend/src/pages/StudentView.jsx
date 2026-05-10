import { useState, useEffect } from 'react'

export default function StudentView({ onBack }) {
  const [name, setName] = useState('')
  const [studentId, setStudentId] = useState(null)
  const [exercises, setExercises] = useState([])
  const [currentExerciseIdx, setCurrentExerciseIdx] = useState(0)
  const [submitted, setSubmitted] = useState(false)
  const [selectedAnswer, setSelectedAnswer] = useState(null)
  const [feedback, setFeedback] = useState(null)
  const [progress, setProgress] = useState({ completed: 0, correct: 0 })
  const [filter, setFilter] = useState('all')

  useEffect(() => {
    if (studentId) {
      fetchExercises()
      updateProgress()
    }
  }, [studentId, filter])

  const fetchExercises = async () => {
    try {
      const url = filter === 'all' ? '/api/exercises' : `/api/exercises?level=${filter}`
      const res = await fetch(url)
      const data = await res.json()
      setExercises(data)
      setCurrentExerciseIdx(0)
      setSubmitted(false)
    } catch (err) {
      console.error(err)
    }
  }

  const updateProgress = async () => {
    try {
      const res = await fetch(`/api/students/${studentId}/progress`)
      const data = await res.json()
      setProgress({
        completed: data.total || 0,
        correct: data.correct || 0
      })
    } catch (err) {
      console.error(err)
    }
  }

  const handleEnterStudent = async () => {
    if (!name.trim()) {
      alert('请输入名字')
      return
    }
    try {
      const res = await fetch('/api/students', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name })
      })
      const student = await res.json()
      setStudentId(student.id)
    } catch (err) {
      console.error(err)
    }
  }

  const handleSubmitAnswer = async () => {
    if (selectedAnswer === null) {
      alert('请选择一个答案')
      return
    }
    try {
      const res = await fetch('/api/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          studentId,
          exerciseId: exercises[currentExerciseIdx].id,
          selectedAnswer
        })
      })
      const result = await res.json()
      setFeedback(result)
      setSubmitted(true)
      updateProgress()
    } catch (err) {
      console.error(err)
    }
  }

  const handleNext = () => {
    if (currentExerciseIdx + 1 < exercises.length) {
      setCurrentExerciseIdx(currentExerciseIdx + 1)
      setSelectedAnswer(null)
      setSubmitted(false)
      setFeedback(null)
    } else {
      alert('本难度所有题目已完成！')
    }
  }

  if (!studentId) {
    return (
      <div className="container">
        <div className="login-box">
          <h2>欢迎使用德语听力练习平台</h2>
          <input
            type="text"
            placeholder="请输入您的名字"
            value={name}
            onChange={(e) => setName(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleEnterStudent()}
          />
          <button onClick={handleEnterStudent}>开始练习</button>
          <button onClick={onBack} className="btn-secondary">返回</button>
        </div>
      </div>
    )
  }

  if (exercises.length === 0) {
    return (
      <div className="container">
        <div className="loading">
          <p>加载题目中...</p>
          <button onClick={onBack}>返回</button>
        </div>
      </div>
    )
  }

  const currentExercise = exercises[currentExerciseIdx]
  const correctAnswerText = currentExercise.options[currentExercise.correctAnswer]
  const selectedAnswerText = selectedAnswer !== null ? currentExercise.options[selectedAnswer] : null

  return (
    <div className="container">
      <div className="header">
        <h1>👤 {name} 的听力练习</h1>
        <div className="stats">
          <span>完成: {progress.completed}</span>
          <span>正确: {progress.correct}</span>
          <span>正确率: {progress.completed > 0 ? Math.round((progress.correct / progress.completed) * 100) : 0}%</span>
        </div>
      </div>

      <div className="difficulty-filter">
        <button className={filter === 'all' ? 'active' : ''} onClick={() => setFilter('all')}>全部</button>
        <button className={filter === 'A1' ? 'active' : ''} onClick={() => setFilter('A1')}>A1</button>
        <button className={filter === 'A2' ? 'active' : ''} onClick={() => setFilter('A2')}>A2</button>
        <button className={filter === 'B1' ? 'active' : ''} onClick={() => setFilter('B1')}>B1</button>
      </div>

      <div className="exercise-card">
        <div className="exercise-info">
          <span className="level">{currentExercise.level}</span>
          <span className="progress">{currentExerciseIdx + 1}/{exercises.length}</span>
        </div>
        <h3>{currentExercise.title}</h3>
        <p className="question">{currentExercise.question}</p>

        <div className="audio-player">
          <audio controls>
            <source src={currentExercise.audioUrl} type="audio/mpeg" />
            您的浏览器不支持音频播放
          </audio>
        </div>

        <div className="options">
          {currentExercise.options.map((option, idx) => (
            <label key={idx} className={`option ${selectedAnswer === idx ? 'selected' : ''}`}>
              <input
                type="radio"
                name="answer"
                checked={selectedAnswer === idx}
                onChange={() => setSelectedAnswer(idx)}
                disabled={submitted}
              />
              {option}
            </label>
          ))}
        </div>

        {!submitted ? (
          <button onClick={handleSubmitAnswer} className="btn-submit">提交答案</button>
        ) : (
          <div className={`feedback ${feedback.isCorrect ? 'correct' : 'incorrect'}`}>
            <h4>{feedback.isCorrect ? '✅ 正确!' : '❌ 错误'}</h4>
            <p>正确答案: {correctAnswerText}</p>
            {feedback.explanation && <p className="explanation">{feedback.explanation}</p>}
            <button onClick={handleNext} className="btn-next">
              {currentExerciseIdx + 1 < exercises.length ? '下一题' : '完成'}
            </button>
          </div>
        )}
      </div>

      <button onClick={onBack} className="btn-secondary btn-back">返回菜单</button>
    </div>
  )
}
