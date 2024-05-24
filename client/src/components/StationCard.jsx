import { callNextPatient, endPatientTurn } from '../api/stations.api';

export function StationCard({station, onUpdate}) {
    const handleNextPatient = async () => {
        try {
            const response = await callNextPatient(station.id);
            if (response.status == 200) {
                onUpdate();
            }
            alert(response.data.message);
        } catch (error) {
            alert(error.response.data.message);
            console.log(error)
        }
    };

    const handleEndTurn = async () => {
        try {
            const response = await endPatientTurn(station.id);
            if (response.status == 200) {
                onUpdate();
            }
            alert(response.data.message);
        } catch (error) {
            alert(error.response.data.message);
        }
    };
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
                    <button className="btn btn-success me-2" onClick={handleNextPatient}>Next </button>
                    <button className="btn btn-warning" onClick={handleEndTurn}>End Turn</button>
                </div>
            </div>
        </div>
    )
}