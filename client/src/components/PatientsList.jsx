import { useEffect, useState } from "react";
import { getAllPatients } from "../api/patients.api";

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
        <div>
            {patients.map(patient => (
                <div key={patient.id}>
                    <p>{patient.full_name}</p>
                    <p>{patient.is_active ? "si" : "no"}</p>
                </div>
            ))}
        </div>
    )
}