import { useEffect, useState } from "react";
import { getAllPatients } from "../api/patients.api";
import { PatientCard } from "./PatientCard";

export function PatientsList() {
    const [patients, setPatients] = useState([]);
    useEffect(() => {
        async function loadPatients() {
            const res = await getAllPatients();
            setPatients(res.data);
        }
        loadPatients();
    }, [])
    return (
        <div className="row">
            {patients.map(patient => (
                <div key={patient.id} className="col-md-4 mb-4">
                    <PatientCard patient={patient} />
                </div>
            ))}
        </div>
    )
}