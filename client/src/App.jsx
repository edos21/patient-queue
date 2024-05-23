import { BrowserRouter, Routes, Route} from 'react-router-dom'
import { Navigation } from "./components/Navigation";
import { PatientsPage } from './pages/PatientsPage'
import { StationsPage } from './pages/StationsPage'
import { PatientsForm } from './pages/PatientsForm'

function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <div className="container mt-4">
        <Routes>
          <Route path="/patients" element={<PatientsPage />} />
          <Route path="/stations" element={<StationsPage />} />
          <Route path="/create-patient" element={<PatientsForm />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App;