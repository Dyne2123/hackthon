import { useState } from 'react'
import { BrowserRouter,Routes,Route } from 'react-router-dom'
import HomePage from './pages/homePage'
import Validator from './editor/valaditor_editor'
import StudentPage from './pages/studentPage'
import Register from './authentication/register'
import Login from './authentication/login'

function App() {
  const [value, setValue] = useState('')

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage/>}/>
        <Route path="/validator" element={<Validator/>}/>
        <Route path="/register" element={<Register/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/student_page" element={<StudentPage/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
