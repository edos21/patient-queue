export function StationCard({station}) {
    return (
        <div className="card mb-3">
            <div className="card-body d-flex justify-content-between align-items-center">
                <div>
                    <h5 className="card-title">{station.name}</h5>
                    <p className="card-text">
                        {station.current_patient ? `Current Patient: ${station.current_patient}` : "No current patient"}
                    </p>
                </div>
                <div>
                    <button className="btn btn-success me-2">Next </button>
                    <button className="btn btn-warning">End Turn</button>
                </div>
            </div>
        </div>
    )
}