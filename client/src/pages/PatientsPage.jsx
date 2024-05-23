import { PatientsList } from "../components/PatientsList"

export function PatientsPage(){
    return (
        <div>
            <h1 className="mb-4">Patients List</h1>
            <PatientsList />
        </div>
    )
}