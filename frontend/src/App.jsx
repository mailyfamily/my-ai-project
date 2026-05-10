import { useState } from 'react'
import StudentView from './pages/StudentView'
import AdminView from './pages/AdminView'
import './App.css'

function App() {
  const [currentView, setCurrentView] = useState('menu')
  const [adminPassword, setAdminPassword] = useState('')
  const [showAdminLogin, setShowAdminLogin] = useState(false)

  const handleAdminLogin = (password) => {
    if (password === 'admin123') {
      setAdminPassword(password)
      setCurrentView('admin')
      setShowAdminLogin(false)
    } else {
      alert('密码错误')
    }
  }

  return (
    <div className="app">
      {currentView === 'menu' && !showAdminLogin && (
        <div className="menu">
          <h1>🎧 德语听力练习平台</h1>
          <p>学生练习 • 老师查看</p>
          <button onClick={() => setCurrentView('student')} className="btn-large">
            学生练习
          </button>
          <button onClick={() => setShowAdminLogin(true)} className="btn-large btn-secondary">
            老师查看
          </button>
        </div>
      )}

      {showAdminLogin && (
        <div className="admin-login">
          <h2>老师管理员登录</h2>
          <input
            type="password"
            placeholder="输入管理员密码"
            onKeyPress={(e) => {
              if (e.key === 'Enter') {
                handleAdminLogin(e.target.value)
                e.target.value = ''
              }
            }}
          />
          <button onClick={(e) => {
            const input = e.target.parentElement.querySelector('input')
            handleAdminLogin(input.value)
          }}>
            登录
          </button>
          <button onClick={() => setShowAdminLogin(false)} className="btn-secondary">
            返回
          </button>
        </div>
      )}

      {currentView === 'student' && (
        <StudentView onBack={() => setCurrentView('menu')} />
      )}

      {currentView === 'admin' && (
        <AdminView onBack={() => {
          setCurrentView('menu')
          setAdminPassword('')
        }} />
      )}
    </div>
  )
}

export default App
