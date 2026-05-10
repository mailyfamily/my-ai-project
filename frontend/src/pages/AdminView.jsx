import { useState, useEffect } from 'react'

export default function AdminView({ onBack }) {
  const [report, setReport] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchReport()
  }, [])

  const fetchReport = async () => {
    try {
      setLoading(true)
      const res = await fetch('/api/admin/report?password=admin123')
      const data = await res.json()
      setReport(data)
    } catch (err) {
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container admin-view">
      <div className="header">
        <h1>📊 学生成绩报告</h1>
        <button onClick={fetchReport} className="btn-refresh">刷新数据</button>
      </div>

      {loading ? (
        <p>加载中...</p>
      ) : report.length === 0 ? (
        <p className="no-data">暂无学生数据</p>
      ) : (
        <div className="report-table">
          <table>
            <thead>
              <tr>
                <th>学生名字</th>
                <th>完成题数</th>
                <th>正确数</th>
                <th>正确率</th>
              </tr>
            </thead>
            <tbody>
              {report.map((student, idx) => {
                const total = student.total_answers || 0
                const correct = student.correct_answers || 0
                const percentage = total > 0 ? Math.round((correct / total) * 100) : 0
                return (
                  <tr key={idx}>
                    <td>{student.name}</td>
                    <td>{total}</td>
                    <td>{correct}</td>
                    <td className={`percentage ${percentage >= 70 ? 'good' : percentage >= 50 ? 'medium' : 'low'}`}>
                      {percentage}%
                    </td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        </div>
      )}

      <div className="summary">
        <h3>统计摘要</h3>
        <p>总学生数: {report.length}</p>
        <p>
          平均正确率: {
            report.length > 0
              ? Math.round(
                  (report.reduce((sum, s) => sum + (s.correct_answers || 0), 0) /
                    report.reduce((sum, s) => sum + (s.total_answers || 0), 0)) *
                    100
                )
              : 0
          }%
        </p>
      </div>

      <button onClick={onBack} className="btn-secondary btn-back">返回菜单</button>
    </div>
  )
}
