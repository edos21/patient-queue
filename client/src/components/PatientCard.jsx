export function PatientCard({patient}) {
    return (
        <div className="card">
            <div className="card-body">
                <h5 className="card-title">{patient.full_name}</h5>
                <p className="card-text">{patient.current_station}</p>
            </div>
        </div>
    )
}