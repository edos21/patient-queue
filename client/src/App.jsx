import { BrowserRouter, Routes, Route} from 'react-router-dom'
import { Navigation } from "./components/Navigation";
import { PatientsPage } from './pages/PatientsPage'
import { PatientsForm } from './pages/PatientsForm'

function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/patients" element={<PatientsPage />} />
        <Route path="/create-patient" element={<PatientsForm />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;